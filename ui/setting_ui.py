# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'setting.ui'
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

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(408, 289)
        self.verticalLayout = QtGui.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.transport_combo = QtGui.QComboBox(Dialog)
        self.transport_combo.setObjectName(_fromUtf8("transport_combo"))
        self.transport_combo.addItem(_fromUtf8(""))
        self.transport_combo.addItem(_fromUtf8(""))
        self.transport_combo.addItem(_fromUtf8(""))
        self.gridLayout.addWidget(self.transport_combo, 3, 1, 1, 1)
        self.domain_input = QtGui.QLineEdit(Dialog)
        self.domain_input.setObjectName(_fromUtf8("domain_input"))
        self.gridLayout.addWidget(self.domain_input, 2, 1, 1, 1)
        self.label_7 = QtGui.QLabel(Dialog)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.gridLayout.addWidget(self.label_7, 2, 0, 1, 1)
        self.label_6 = QtGui.QLabel(Dialog)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout.addWidget(self.label_6, 1, 0, 1, 1)
        self.username_input = QtGui.QLineEdit(Dialog)
        self.username_input.setObjectName(_fromUtf8("username_input"))
        self.gridLayout.addWidget(self.username_input, 0, 1, 1, 1)
        self.label_5 = QtGui.QLabel(Dialog)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout.addWidget(self.label_5, 0, 0, 1, 1)
        self.password_input = QtGui.QLineEdit(Dialog)
        self.password_input.setText(_fromUtf8(""))
        self.password_input.setEchoMode(QtGui.QLineEdit.Password)
        self.password_input.setObjectName(_fromUtf8("password_input"))
        self.gridLayout.addWidget(self.password_input, 1, 1, 1, 1)
        self.label_9 = QtGui.QLabel(Dialog)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.gridLayout.addWidget(self.label_9, 3, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Save)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)
        self.buttonBox.raise_()

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.transport_combo.setItemText(0, _translate("Dialog", "udp", None))
        self.transport_combo.setItemText(1, _translate("Dialog", "tcp", None))
        self.transport_combo.setItemText(2, _translate("Dialog", "tls", None))
        self.label_7.setText(_translate("Dialog", "domain:", None))
        self.label_6.setText(_translate("Dialog", "password:", None))
        self.label_5.setText(_translate("Dialog", "username:", None))
        self.label_9.setText(_translate("Dialog", "transport:", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

