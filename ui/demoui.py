# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demo.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(1024, 800)
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(9, 9, 36, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.remote_view = QtGui.QFrame(Form)
        self.remote_view.setGeometry(QtCore.QRect(440, 40, 561, 421))
        self.remote_view.setFrameShape(QtGui.QFrame.StyledPanel)
        self.remote_view.setFrameShadow(QtGui.QFrame.Raised)
        self.remote_view.setObjectName(_fromUtf8("remote_view"))
        self.preview_view = QtGui.QFrame(Form)
        self.preview_view.setGeometry(QtCore.QRect(810, 500, 191, 161))
        self.preview_view.setFrameShape(QtGui.QFrame.StyledPanel)
        self.preview_view.setFrameShadow(QtGui.QFrame.Raised)
        self.preview_view.setObjectName(_fromUtf8("preview_view"))
        self.call_btn = QtGui.QPushButton(Form)
        self.call_btn.setGeometry(QtCore.QRect(320, 10, 75, 23))
        self.call_btn.setObjectName(_fromUtf8("call_btn"))
        self.hangup_btn = QtGui.QPushButton(Form)
        self.hangup_btn.setGeometry(QtCore.QRect(320, 50, 75, 23))
        self.hangup_btn.setObjectName(_fromUtf8("hangup_btn"))
        self.accept_btn = QtGui.QPushButton(Form)
        self.accept_btn.setGeometry(QtCore.QRect(320, 90, 75, 23))
        self.accept_btn.setObjectName(_fromUtf8("accept_btn"))
        self.incoming_display = QtGui.QLabel(Form)
        self.incoming_display.setGeometry(QtCore.QRect(20, 70, 251, 31))
        self.incoming_display.setText(_fromUtf8(""))
        self.incoming_display.setObjectName(_fromUtf8("incoming_display"))
        self.call_input = QtGui.QLineEdit(Form)
        self.call_input.setGeometry(QtCore.QRect(60, 10, 241, 31))
        self.call_input.setObjectName(_fromUtf8("call_input"))
        self.line = QtGui.QFrame(Form)
        self.line.setGeometry(QtCore.QRect(410, 10, 16, 781))
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.username_input = QtGui.QLineEdit(Form)
        self.username_input.setGeometry(QtCore.QRect(80, 590, 113, 20))
        self.username_input.setObjectName(_fromUtf8("username_input"))
        self.password_input = QtGui.QLineEdit(Form)
        self.password_input.setGeometry(QtCore.QRect(80, 620, 113, 20))
        self.password_input.setText(_fromUtf8(""))
        self.password_input.setEchoMode(QtGui.QLineEdit.Password)
        self.password_input.setObjectName(_fromUtf8("password_input"))
        self.domain_input = QtGui.QLineEdit(Form)
        self.domain_input.setGeometry(QtCore.QRect(80, 650, 113, 20))
        self.domain_input.setObjectName(_fromUtf8("domain_input"))
        self.label_5 = QtGui.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(20, 590, 51, 16))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_6 = QtGui.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(20, 620, 54, 12))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.label_7 = QtGui.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(20, 650, 54, 12))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.save_account_btn = QtGui.QPushButton(Form)
        self.save_account_btn.setGeometry(QtCore.QRect(210, 590, 75, 23))
        self.save_account_btn.setObjectName(_fromUtf8("save_account_btn"))
        self.refresh_btn = QtGui.QPushButton(Form)
        self.refresh_btn.setGeometry(QtCore.QRect(30, 730, 75, 23))
        self.refresh_btn.setObjectName(_fromUtf8("refresh_btn"))
        self.label_8 = QtGui.QLabel(Form)
        self.label_8.setGeometry(QtCore.QRect(20, 710, 91, 16))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.register_state_display = QtGui.QLabel(Form)
        self.register_state_display.setGeometry(QtCore.QRect(120, 710, 131, 16))
        self.register_state_display.setObjectName(_fromUtf8("register_state_display"))
        self.register_check = QtGui.QCheckBox(Form)
        self.register_check.setGeometry(QtCore.QRect(210, 630, 71, 16))
        self.register_check.setObjectName(_fromUtf8("register_check"))
        self.transport_combo = QtGui.QComboBox(Form)
        self.transport_combo.setGeometry(QtCore.QRect(90, 680, 69, 22))
        self.transport_combo.setObjectName(_fromUtf8("transport_combo"))
        self.transport_combo.addItem(_fromUtf8(""))
        self.transport_combo.addItem(_fromUtf8(""))
        self.transport_combo.addItem(_fromUtf8(""))
        self.label_9 = QtGui.QLabel(Form)
        self.label_9.setGeometry(QtCore.QRect(20, 680, 61, 16))
        self.label_9.setObjectName(_fromUtf8("label_9"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.label.setText(_translate("Form", "呼叫：", None))
        self.call_btn.setText(_translate("Form", "call", None))
        self.hangup_btn.setText(_translate("Form", "hangup", None))
        self.accept_btn.setText(_translate("Form", "accept", None))
        self.label_5.setText(_translate("Form", "username:", None))
        self.label_6.setText(_translate("Form", "password:", None))
        self.label_7.setText(_translate("Form", "domain:", None))
        self.save_account_btn.setText(_translate("Form", "保存", None))
        self.refresh_btn.setText(_translate("Form", "刷新", None))
        self.label_8.setText(_translate("Form", "register state:", None))
        self.register_state_display.setText(_translate("Form", "初始化", None))
        self.register_check.setText(_translate("Form", "连接", None))
        self.transport_combo.setItemText(0, _translate("Form", "udp", None))
        self.transport_combo.setItemText(1, _translate("Form", "tcp", None))
        self.transport_combo.setItemText(2, _translate("Form", "tls", None))
        self.label_9.setText(_translate("Form", "transport:", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

