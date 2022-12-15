# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1096, 624)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(710, 10, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(260, 10, 411, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.toolButton = QtWidgets.QToolButton(Dialog)
        self.toolButton.setGeometry(QtCore.QRect(680, 10, 22, 21))
        self.toolButton.setObjectName("toolButton")
        self.label_OriginalPhoto = QtWidgets.QLabel(Dialog)
        self.label_OriginalPhoto.setGeometry(QtCore.QRect(10, 60, 521, 541))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_OriginalPhoto.sizePolicy().hasHeightForWidth())
        self.label_OriginalPhoto.setSizePolicy(sizePolicy)
        self.label_OriginalPhoto.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_OriginalPhoto.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_OriginalPhoto.setText("")
        self.label_OriginalPhoto.setScaledContents(True)
        self.label_OriginalPhoto.setObjectName("label_OriginalPhoto")
        self.label_Binary = QtWidgets.QLabel(Dialog)
        self.label_Binary.setGeometry(QtCore.QRect(560, 60, 521, 241))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_Binary.sizePolicy().hasHeightForWidth())
        self.label_Binary.setSizePolicy(sizePolicy)
        self.label_Binary.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_Binary.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_Binary.setText("")
        self.label_Binary.setScaledContents(True)
        self.label_Binary.setObjectName("label_Binary")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(180, 10, 81, 20))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(10, 40, 81, 20))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(560, 40, 81, 20))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(560, 430, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Adobe Arabic")
        font.setPointSize(14)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_Result = QtWidgets.QLabel(Dialog)
        self.label_Result.setGeometry(QtCore.QRect(680, 410, 311, 61))
        font = QtGui.QFont()
        font.setFamily("Adobe Arabic")
        font.setPointSize(40)
        font.setBold(True)
        font.setWeight(75)
        self.label_Result.setFont(font)
        self.label_Result.setText("")
        self.label_Result.setObjectName("label_Result")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton.setText(_translate("Dialog", "Open"))
        self.toolButton.setText(_translate("Dialog", "..."))
        self.label_3.setText(_translate("Dialog", "圖片位址："))
        self.label_4.setText(_translate("Dialog", "原圖："))
        self.label_5.setText(_translate("Dialog", "車牌："))
        self.label_6.setText(_translate("Dialog", "辨識結果："))


