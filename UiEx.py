# -*- coding: utf-8 -*-

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import sys

import ControllerTest

class Main(QDialog):
    def __init__(self, parent): 
        super(Main, self).__init__() 
        self.ui()
        self.parent = parent

    def ui(self): 
        # 이런 코드등으로 윈도우 스타일을 지정할수 있습니다.
        self.setWindowFlags(Qt.FramelessWindowHint) 
        #self.setWindowFlags(Qt.X11BypassWindowManagerHint) 
        
        # 타이틀
        self.setWindowTitle("Test") 
        
        # 아이콘
        ## self.setWindowIcon(QIcon('image/icon.png'))  # icon.png 대신 원하는 아이콘을

        # 배경 사진
        # palette = QPalette()
        # palette.setBrush(QPalette.Background,QBrush(QPixmap("image/background.jpg")))
        # self.setPalette(palette) 

        # 배경 색칠 
        self.teb_gb_co = QPalette() 
        self.teb_gb_co.setColor(QPalette.Background, QColor(46, 204, 113)) 
        self.setPalette(self.teb_gb_co) 

        #윈도우 크기 
        self.setGeometry(800, 50, 400, 500) 
        
        image = 'image/round.png' 
        self.round_image = QLabel(self) 
        self.round_image.setGeometry(153, 35 , 100, 100) 
        self.round_image.setPixmap(QPixmap(image)) 

        # 사진 
        image = 'image/charity.png' 
        self.python_image = QLabel(self) 
        self.python_image.setGeometry(170, 50 , 60, 60) 
        self.python_image.setPixmap(QPixmap(image)) 
        
        self.quit_button = QPushButton(self) 
        self.quit_button.setGeometry(368, 0, 32, 32) 
        self.quit_button.setFlat(True) 
        self.quit_button.setStyleSheet('QPushButton{background-color: rgba(0, 0, 0, 0.0)}') 
        self.quit_button.setIcon(QIcon('image/quit.png')) 
        self.quit_button.setIconSize(QSize(64, 64)) 
        #self.quit_button.clicked.connect(QCoreApplication.instance().quit) 

        #그룹박스 
        self.gb= QGroupBox(self) 
        self.gb.setGeometry(10, 150, 380, 200) 
        self.gb.setObjectName("gb") 
        self.gb.setFlat(True) 
        self.gb.setAutoFillBackground(True) 

        self.teb_gb_color = QPalette() 
        self.teb_gb_color.setColor(QPalette.Background, QColor(39, 174, 96)) 
        self.gb.setPalette(self.teb_gb_color) 

        # 사진 
        image = 'image/user.png' 
        self.python_image = QLabel(self.gb) 
        self.python_image.setGeometry(10, 10 , 32, 32) 
        self.python_image.setPixmap(QPixmap(image)) 

        # 사진 
        image = 'image/password.png' 
        self.python_image = QLabel(self.gb) 
        self.python_image.setGeometry(10, 54 , 32, 32) 
        self.python_image.setPixmap(QPixmap(image)) 
        
        self.id_Input = QLineEdit(self.gb) 
        self.id_Input.setFrame(False) 
        self.id_Input.setPlaceholderText(' ID') 
        self.id_Input.setGeometry(50, 10, 310, 32) 

        self.pw_Input = QLineEdit(self.gb) 
        self.pw_Input.setFrame(False) 
        self.pw_Input.setPlaceholderText(' PW') 
        self.pw_Input.setGeometry(50, 56, 310, 32)

        self.login_button = QPushButton("", self.gb) 
        self.login_button.setGeometry(50, 120, 100, 100) 
        self.login_button.setFlat(True) 
        self.login_button.setStyleSheet('QPushButton{background-color: rgba(0, 0, 0, 0.0)}') 
        self.login_button.setIcon(QIcon('image/login.png')) 
        self.login_button.setIconSize(QSize(100, 100)) 
        self.login_button.clicked.connect(self.signalAuth)

        self.show() 

    def signalAuth(self):
        self.parent.loadMainAfterAuth()
        #self.emit(SIGNAL("authDone()"))

    def gb_Animation_Start(self): 
        # str -> PySide2 QByteArray
        self.gb_Animation = QPropertyAnimation(self, b"size") 
        self.gb_Animation.setDuration(800) 
        self.gb_Animation.setEasingCurve(QEasingCurve.InOutBack) 
        self.gb_Animation.setEndValue(QSize(self.width(), self.height()-170)) 
        self.gb_Animation.start()

    def resizeEvent(self, evt=None): 
        pass 
            
        
def main(): 
    app = QApplication(sys.argv) 
    win = Main(None) 
    win.show() 
    sys.exit(app.exec_()) 
            
if __name__ == '__main__': 
    main()