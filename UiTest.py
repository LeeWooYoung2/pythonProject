# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UiTest.ui',
# licensing of 'UiTest.ui' applies.
#
# Created: Wed Nov  7 15:18:09 2018
#      by: pyside2-uic  running on PySide2 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setGeometry(800, 200, 261, 191)
        Form.resize(425, 160)
        
        self.formLayout = QtWidgets.QHBoxLayout(Form)
        self.formLayout.setObjectName("formLayout")

        self.mainHLayout = QtWidgets.QHBoxLayout()
        
        self.mainHLayout.setObjectName("mainHLayout")
        self.accumulatebtn = QtWidgets.QPushButton(Form)
        self.accumulatebtn.setObjectName("accumulatebtn")
        self.mainHLayout.addWidget(self.accumulatebtn)
        
        self.pointInputVLayout = QtWidgets.QVBoxLayout()
        self.pointInputVLayout.setObjectName("pointInputVLayout")
        self.plusBtn = QtWidgets.QPushButton(Form)
        self.plusBtn.setObjectName("plusBtn")
        self.pointInputVLayout.addWidget(self.plusBtn)
        self.pointBtn = QtWidgets.QPushButton(Form)
        self.pointBtn.setObjectName("pointBtn")
        self.pointInputVLayout.addWidget(self.pointBtn)
        self.minusBtn = QtWidgets.QPushButton(Form)
        self.minusBtn.setObjectName("minusBtn")
        self.pointInputVLayout.addWidget(self.minusBtn)

        self.mainHLayout.addLayout(self.pointInputVLayout)

        self.setupVLayout = QtWidgets.QVBoxLayout()
        self.setupVLayout.setObjectName("setupVLayout")
        self.quitBtn = QtWidgets.QPushButton(Form)
        self.quitBtn.setObjectName("quitBtn")
        self.setupVLayout.addWidget(self.quitBtn)
        self.bodyBtn = QtWidgets.QPushButton(Form)
        self.bodyBtn.setObjectName("bodyBtn")
        self.setupVLayout.addWidget(self.bodyBtn)

        self.subBodyHLayout = QtWidgets.QHBoxLayout()
        self.subBodyHLayout.setObjectName("subBodyHLayout")
        self.refreshBtn = QtWidgets.QPushButton(Form)
        self.refreshBtn.setObjectName("refreshBtn")
        self.subBodyHLayout.addWidget(self.refreshBtn)
        self.settingsBtn = QtWidgets.QPushButton(Form)
        self.settingsBtn.setObjectName("settingsBtn")
        self.subBodyHLayout.addWidget(self.settingsBtn)
        self.setupVLayout.addLayout(self.subBodyHLayout)

        self.mainHLayout.addLayout(self.setupVLayout)

        self.useBtn = QtWidgets.QPushButton(Form)
        self.useBtn.setObjectName("useBtn")
        self.mainHLayout.addWidget(self.useBtn)

        self.formLayout.addLayout(self.mainHLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtWidgets.QApplication.translate("Form", "Form", None, -1))
        self.accumulatebtn.setText(QtWidgets.QApplication.translate("Form", "적립", None, -1))
        self.plusBtn.setText(QtWidgets.QApplication.translate("Form", "+", None, -1))
        self.pointBtn.setText(QtWidgets.QApplication.translate("Form", "P", None, -1))
        self.minusBtn.setText(QtWidgets.QApplication.translate("Form", "-", None, -1))
        self.quitBtn.setText(QtWidgets.QApplication.translate("Form", "X", None, -1))
        self.bodyBtn.setText(QtWidgets.QApplication.translate("Form", "BERITH", None, -1))
        self.refreshBtn.setText(QtWidgets.QApplication.translate("Form", "refresh", None, -1))
        self.settingsBtn.setText(QtWidgets.QApplication.translate("Form", "settings", None, -1))
        self.useBtn.setText(QtWidgets.QApplication.translate("Form", "사용/조회", None, -1))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

