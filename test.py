#coding:utf8
from PyQt4 import QtGui, QtCore  
import sys  
import demoui  
from CoreManager import CoreManager

class Test(QtGui.QWidget, demoui.Ui_Form):  
    def __init__(self, parent=None):  
        super(Test, self).__init__(parent)
        self.setupUi(self)  
        self._connect_init()

        self.linphone = CoreManager(self.preview_view_winId,
                                    self.remote_view_winId,
                                    self.registration_cb,
                                    self.incoming_cb)

        #test
        self.username_input.setText(QtCore.QString(u'1111'))
        self.password_input.setText(QtCore.QString(u'123'))
        self.domain_input.setText(QtCore.QString(u'192.168.123.97'))
        self.transport_combo.setCurrentIndex(2)
        self.save_event()

    def _connect_init(self):
        self.connect(self.call_btn, QtCore.SIGNAL('clicked()'), self.call_event)
        self.connect(self.accept_btn, QtCore.SIGNAL('clicked()'), self.accept_event)
        self.connect(self.hangup_btn, QtCore.SIGNAL('clicked()'), self.hangup_event)
        self.connect(self.refresh_btn, QtCore.SIGNAL('clicked()'), self.refresh_event)
        self.connect(self.save_account_btn, QtCore.SIGNAL('clicked()'), self.save_event)
        self.connect(self.register_check, QtCore.SIGNAL('stateChanged(int)'), self.register_check_event)

    def call_event(self):
        number = self.text_convert(self.call_input.text())
        if number == '':
            return
        self.linphone.call(number)

    def accept_event(self):
        self.linphone.accept()

    def hangup_event(self):
        self.linphone.hangup()

    def register_check_event(self):
        if self.register_check.isChecked():
            self.linphone.register()
        else:
            self.linphone.unregister()

    def refresh_event(self):
        self.linphone.refresh_register()

    def save_event(self):
        username = self.text_convert(self.username_input.text())
        password = self.text_convert(self.password_input.text())
        domain = self.text_convert(self.domain_input.text())
        transport = self.text_convert(self.transport_combo.currentText())
        self.linphone.set_account(username, password, domain, transport)
        
    def incoming_cb(self, number):
        self.incoming_display.setText(QtCore.QString(number))

    def registration_cb(self, state):
        self.register_state_display.setText(QtCore.QString(state))
        
    def text_convert(self, qstring):
        return unicode(qstring.toUtf8(),'utf8', 'ignore').encode('utf8')

    @property
    def remote_view_winId(self):
        return int(self.remote_view.winId())

    @property
    def preview_view_winId(self):
        return int(self.preview_view.winId())
  
app=QtGui.QApplication(sys.argv)  
dialog=Test()  
dialog.show()  
sys.exit(app.exec_())