#coding:utf8
import linphone
import logging
from threading import Thread, Event

class Timer(Thread):
    """Call a function after a specified number of seconds:

            t = Timer(30.0, f, args=[], kwargs={})
            t.start()
            t.cancel()     # stop the timer's action if it's still waiting

    """

    def __init__(self, interval, function, args=[], kwargs={}):
        Thread.__init__(self)
        self.daemon = True
        self.interval = interval
        self.function = function
        self.args = args
        self.kwargs = kwargs
        self.finished = Event()
        self.run_flag = False

    def cancel(self):
        """Stop the timer if it hasn't finished yet"""
        self.finished.set()
        self.run_flag = False

    def run(self):
        self.run_flag = True
        while self.run_flag:
            self.finished.wait(self.interval)
            if not self.finished.is_set():
                self.function(*self.args, **self.kwargs)
            
class CoreManager:
    def __init__(self, preview_winId=0, video_winId=0,
                registration_state_changed_handler=None,
                incoming_handler=None):
        logging.basicConfig(level=logging.INFO)
        # def log_handler(level, msg):
        #     method = getattr(logging, level)
        #     method(msg)
        # linphone.set_log_handler(log_handler)

        self.domain = None
        self.registration_state_changed_handler = registration_state_changed_handler
        self.incoming_handler = incoming_handler


        self.core = linphone.Factory.get().create_core(self.get_cbs(), None, None)
        self.core.ipv6_enabled = False
        self.core.sip_transports = linphone.SipTransports(-1, -1, -1, 0)
        self.core.native_preview_window_id = preview_winId
        self.core.native_video_window_id = video_winId
        self.core.use_preview_window(True)
        self._set_default_proxy()

        self._current_call = None
        self._registration_state = linphone.RegistrationState._None

        self._timer = None
        self._setup_loop()

    def set_account(self, username, password, domain, transport='udp'):
        if username and password and domain \
            and username == '' and password == '' and domain == '':
            return False
        
        for auth_info in self.core.auth_info_list:
            self.core.remove_auth_info(auth_info)

        self.domain = domain
        auth = self.core.create_auth_info(username, None, password, None, None, domain)
        self.core.add_auth_info(auth)    

        self.core.default_proxy_config.edit()
        id_address = self.create_address(username, domain)
        id_address.transport = {
            'udp': linphone.TransportType.Udp,
            'tcp': linphone.TransportType.Tcp,
            'tls': linphone.TransportType.Tls
        }.get(transport.lower(), 'udp')
        self.core.default_proxy_config.identity_address = id_address
        self.core.default_proxy_config.server_addr = "sip:%s" % domain
        self.core.default_proxy_config.done()
        return True

    def register(self):
        self.core.default_proxy_config.edit()
        self.core.default_proxy_config.register_enabled = True
        self.core.default_proxy_config.done()

    def refresh_register(self):
        self.core.refresh_registers()

    def unregister(self):
        self.core.default_proxy_config.edit()
        self.core.default_proxy_config.register_enabled = False
        self.core.default_proxy_config.done()

    def _set_default_proxy(self):
        proxy_cfg = self.core.create_proxy_config()
        proxy_cfg.expires = 60
        proxy_cfg.register_enabled = False

        #identity_address and server_addr is necessary, or it can't add to core
        proxy_cfg.identity_address = self.create_address(None, '255.255.255.255')
        proxy_cfg.server_addr = "sip:255.255.255.255"
        
        self.core.add_proxy_config(proxy_cfg)
        self.core.default_proxy_config = proxy_cfg

    def _setup_loop(self):
        self._timer = Timer(0.02, self.core.iterate)
        self._timer.start()

    def get_cbs(self):
        cbs = linphone.Factory.get().create_core_cbs()
        cbs.authentication_requested = self.authentication_requested_cb
        # cbs.call_encryption_changed = self.call_encryption_changed_cb
        # cbs.call_log_updated = self.call_log_updated_cb
        cbs.call_state_changed = self.call_state_changed_cb
        # cbs.call_stats_updated = self.call_stats_updated_cb
        cbs.registration_state_changed = self.registration_state_changed_cb
        return cbs

    def create_address(self, username, domain):
        address = self.core.create_address("sip:%s@%s" % (username, domain)) if domain else None
        if not address:
            return address
        
        return address

    def call(self, number):
        if self._current_call:
            logging.info('A call is proccessing!')
            return
        addr = self.create_address(number, self.domain)
        if addr:
            self._current_call = self.core.invite_address(addr)
        else:
            logging.warning('call addr is none')

    def hangup(self):
        if not self._current_call:
            logging.error('No call is proccessing!')
            return
        self._current_call.terminate()

    def accept(self):
        if not self._current_call:
            logging.error('No call is proccessing!')
            return
        self._current_call.accept()

    ''' linphone devices property'''
    @property
    def sound_capture_devices(self):
        return [device for device in self.core.sound_devices if self.core.sound_device_can_capture(device)]

    @property
    def sound_play_devices(self):
        return [device for device in self.core.sound_devices if self.core.sound_device_can_playback(device)]

    @property
    def video_devices(self):
        return self.core.video_devices

    @property
    def capture_device(self):
        return self.core.capture_device

    @capture_device.setter
    def capture_device(self, device):
        if not device in self.sound_devices:
            raise Exception('%s not found!' % device)
        if not self.core.sound_device_can_capture(device):
            raise Exception('%s not a sound capture device!' % device)
        self.core.capture_device = device

    @property
    def playback_device(self):
        return self.core.playback_device

    @playback_device.setter
    def playback_device(self, device):
        if not device in self.sound_devices:
            raise Exception('%s not found!' % device)
        if not self.core.sound_device_can_playback(device):
            raise Exception('%s not a sound play device' % device)
        self.core.playback_device = device

    @property
    def ringer_device(self):
        return self.core.ringer_device

    @ringer_device.setter
    def ringer_device(self, device):
        if not device in self.sound_devices:
            raise Exception('%s not found!' % device)
        if not self.core.sound_device_can_playback(device):
            raise Exception('%s not a sound play device' % device)
        self.core.ringer_device = ringer_device

    @property
    def video_device(self):
        return self.core.video_device

    @video_device.setter
    def video_device(self, device):
        if not device in self.video_devices:
            raise Exception('%s not found!' % device)
        self.core.video_device = video_device

    def reload_sound_devices(self):
        self.core.reload_sound_devices()

    def reload_video_devices(self):
        self.core.reload_video_devices

    
    ''' linphone callbacks '''
    def authentication_requested_cb(self, core, auth_info, method):
        '''
            auth_info: LinphoneAuthInfo
            method: LinphoneAuthMethod
        '''
        logging.info('authentication_requested_cb: %s' % method)
        pass

    def call_encryption_changed_cb(self, core, call, is_encrypt, auth_token):
        '''
            call: LinphoneCall
            is_encrpy: bool
            auth_token: string
        '''
        logging.info('call_encryption_changed_cb active')
        pass

    def call_log_updated_cb(self, core, newcl):
        '''
            newcl: LinphoneCallLog
        '''
        logging.info('call_log_updated_cb active')
        pass

    def call_state_changed_cb(self, core, call, state, message):
        '''
            call: LinphoneCall
            state: LinphoneCallState
            message: string
        '''
        remote_address = call.remote_address_as_string
        if state == linphone.CallState.IncomingReceived:
            logging.info("incoming call from " + remote_address)
            if self._current_call:
                #only accpet on call
                call.decline(linphone.Reason.Busy)
                return
            self._current_call = call

            if self.incoming_handler:
                number = call.remote_address.username
                self.incoming_handler(u'%s 来电' % number)

        elif state == linphone.CallState.OutgoingRinging:
            logging.info("outgoing ringing")
        elif state == linphone.CallState.Connected:
            logging.info(remote_address + " connected")
        elif state == linphone.CallState.Released:
            if id(call) ==  id(self._current_call):
                self._current_call = None
                logging.info("terminate current call: " + remote_address)

                if call.dir == linphone.CallDir.Incoming and self.incoming_handler:
                    self.incoming_handler(u'')
            else:
                logging.info("terminate another call: " + remote_address) 
        elif state == linphone.CallState.Error:
            logging.error("call encoutered an error: %s" % message)
        else:
            logging.debug("call_state_changed: %s, %s" % (state, message)) 
            
    def call_stats_updated_cb(self, core, call, stats):
        '''
            call: LinphoneCall
            stats: LinphoneCallStats
        '''
        # logging.warning('call_state_updated_cb active')
        pass

    def registration_state_changed_cb(self, core, cfg, state, message):
        '''
            cfg: LinphoneProxyConfig
            state: LinphoneRegistratinState
            message: string
        '''
        if self._registration_state != state:
            logging.info("registration_state_changed: %s, %s" % (state, message))
            self._registration_state = state

            if self.registration_state_changed_handler:
                message = {
                    linphone.RegistrationState._None: u'初始化',
                    linphone.RegistrationState.Progress: u'注册中',
                    linphone.RegistrationState.Ok: u'注册成功',
                    linphone.RegistrationState.Cleared: u'取消注册成功',
                    linphone.RegistrationState.Failed: u'注册失败'
                }[state]
                self.registration_state_changed_handler(message)

    def test(self):
        # print len(self.core.auth_info_list)
        self.unregister()

if __name__ == '__main__':
    import time
    domain = '192.168.123.97'
    # domain = '120.24.77.46'
    c = CoreManager()
    c.set_account('1111', '123', domain)
    c.register()
    # time.sleep(1)
    # c.test()
    # time.sleep(1)
    while True:
        try:
            command = raw_input()
        except:
            break

        if command in ('exit',' '):
            break
        elif command.find('call ') != -1:
            _, number = command.split(' ')
            c.call(number)
        elif command == 'hangup':
            c.hangup()
        elif command == 'accept':
            c.accept()
        elif command == 'test':
            c.test()

