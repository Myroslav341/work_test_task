# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'resize_window.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class NewDialogResize(QtWidgets.QDialog):
    def __init__(self, parent):
        super(NewDialogResize, self).__init__(parent)
        self.setupUi(self)

    def setupUi(self, Dialog):
        Dialog.setObjectName("Resize window")
        self.setFixedSize(190, 100)
        font = QtGui.QFont()
        font.setPointSize(8)
        Dialog.setFont(font)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 10, 54, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(10, 40, 54, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.spin_row = QtWidgets.QSpinBox(Dialog)
        self.spin_row.setGeometry(QtCore.QRect(90, 7, 90, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.spin_row.setFont(font)
        self.spin_row.setObjectName("spin_row")
        self.spin_row.setMinimum(1)

        self.spin_col = QtWidgets.QSpinBox(Dialog)
        self.spin_col.setGeometry(QtCore.QRect(90, 37, 90, 22))
        self.spin_col.setMinimum(1)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.spin_col.setFont(font)
        self.spin_col.setObjectName("spin_col")
        self.close_button = QtWidgets.QPushButton(Dialog)
        self.close_button.setGeometry(QtCore.QRect(10, 70, 80, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.close_button.setFont(font)
        self.close_button.setObjectName("pushButton")
        self.apply_button = QtWidgets.QPushButton(Dialog)
        self.apply_button.setGeometry(QtCore.QRect(100, 70, 80, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.apply_button.setFont(font)
        self.apply_button.setObjectName("pushButton_2")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)


    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Resize window"))
        self.label.setText(_translate("Dialog", "Rows"))
        self.label_2.setText(_translate("Dialog", "Columns"))
        self.close_button.setText(_translate("Dialog", "Apply"))
        self.apply_button.setText(_translate("Dialog", "Close"))