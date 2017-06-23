from ui import setting_ui
from PyQt4 import QtCore, QtGui

class Setting(QtGui.QDialog, setting_ui.Ui_Dialog):  
    def __init__(self, parent=None):  
        super(Setting, self).__init__(parent)
        self.setupUi(self)  

    def _get_widget_text(self, widget_name, text_name = 'text'):
        if not hasattr(self, widget_name):
            raise Exception('Setting has no %s widget!' % widget_name)

        widget = getattr(self, widget_name)
        if not hasattr(widget, text_name):
            raise Exception('%s has no method %!' % (widget_name, text_name))

        qstring = getattr(widget, text_name)()
        return unicode(qstring.toUtf8(),'utf8', 'ignore').encode('utf8')
        
    @property
    def username(self):
        return self._get_widget_text('username_input')

    @property
    def password(self):
        return self._get_widget_text('password_input')

    @property
    def domain(self):
        return self._get_widget_text('domain_input')

    @property
    def transport(self):
        return self._get_widget_text('transport_combo', 'currentText')

if __name__ == '__main__':
    import sys
    app = QtGui.QApplication(sys.argv)
    ui = Setting()
    ui.show()  
    app.exec_()
    print ui.transport
    sys.exit()