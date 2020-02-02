# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'confirm_window.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class NewDialogConfirm(QtWidgets.QDialog):
    def __init__(self, parent):
        super(NewDialogConfirm, self).__init__(parent)
        self.setupUi(self)

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        self.setFixedSize(324, 80)
        font = QtGui.QFont()
        font.setPointSize(10)
        Dialog.setFont(font)
        self.confirm_button = QtWidgets.QPushButton(Dialog)
        self.confirm_button.setGeometry(QtCore.QRect(20, 45, 82, 25))
        self.confirm_button.setObjectName("pushButton")
        self.close_button = QtWidgets.QPushButton(Dialog)
        self.close_button.setGeometry(QtCore.QRect(220, 45, 82, 25))
        self.close_button.setObjectName("pushButton_2")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(50, 0, 221, 21))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(100, 20, 131, 16))
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Confirm"))
        self.confirm_button.setText(_translate("Dialog", "Confirm"))
        self.close_button.setText(_translate("Dialog", "Close"))
        self.label.setText(_translate("Dialog", "You will lost some data if confirm"))
        self.label_2.setText(_translate("Dialog", "table size changes"))
