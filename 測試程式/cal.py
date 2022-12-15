# -*- coding: utf-8 -*-
"""
Created on Thu May  2 18:36:19 2019

@author: ggghh
"""

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPalette, QBrush, QPixmap, QImage
from test import Ui_Dialog as UID
import numpy as np
from tkinter import filedialog
import os
#import cv2
import sys
import tkinter

file_path = ''
newpath = ''

class NewUi(UID):       
    def setupFunction(self):
        self.toolButton.clicked.connect(self.get_file)
        self.pushButton.clicked.connect(self.show_file)
        
    def get_file(self):
        
        root = tkinter.Tk()
        root.withdraw()

        file_path = filedialog.askopenfilename()
        global newpath
        self.lineEdit.setText(file_path)        
        newpath = file_path.replace('/',r'\\')
        
    def show_file(self):
        global newpath
        #img = cv2.imread(newpath)
        #img = QImage(newpath)
        pixMap = QPixmap(newpath).scaled(self.label_OriginalPhoto.width(),self.label_OriginalPhoto.height())
        self.label_OriginalPhoto.setPixmap(pixMap)
        #cv2.imshow('test',img)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)  # 创建一个QApplication，也就是你要开发的软件app
    MainWindow = QtWidgets.QMainWindow()    # 创建一个QMainWindow，用来装载你需要的各种组件、控件
    ui = NewUi()                    # ui是Ui_MainWindow()类的实例化对象
    ui.setupUi(MainWindow)                  # 执行类中的setupUi方法，方法的参数是第二步中创建的QMainWindow
    ui.setupFunction()
    MainWindow.show()                       # 执行QMainWindow的show()方法，显示这个QMainWindow
    sys.exit(app.exec_())                   # 使用exit()或者点击关闭按钮退出QApplication
    
    