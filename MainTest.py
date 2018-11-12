# -*- coding: utf-8 -*-

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2 import QtCore, QtGui, QtWidgets

import sys
import time
import UiTest
import socketClient as socketClient
import socketServer as socketServer


#적립완료 됐을 시 팝업
class accCompPopup(QWidget):
    def __init__(self):
        #QWidget.__init__(self)
        super().__init__()
        self.setupUi(self)

    # def paintEvent(self, e):
    #     dc = QPainter(self)
    #     dc.drawLine(0, 0, 100, 100)
    #     dc.drawLine(100, 0, 0, 100)
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 139)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(110, 30, 181, 16))
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(50, 80, 75, 23))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        # self.threadTest = ThreadTest()
        # self.threadTest_thread = QThread()
        # self.threadTest.moveToThread(self.threadTest_thread)
        # self.threadTest_thread.start()


        # self.threadTest.sig_numbers.connect(self.updateStatus)
        # self.threadTest.startWork()

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtWidgets.QApplication.translate("Form", "Form", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("Form", "XXX P적립이 완료 되었습니다.", None, -1))
        self.pushButton.setText(QtWidgets.QApplication.translate("Form", "확인", None, -1))
       

#적립 버튼 눌렀을 시 팝업
class accSendWaitPopup(QWidget):
    def __init__(self, parent):
        self.parentUi = parent
        super().__init__()
        self.setupUi(self)

    # def paintEvent(self, e):
    #     dc = QPainter(self)
    #     dc.drawLine(0, 0, 100, 100)
    #     dc.drawLine(100, 0, 0, 100)
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 139)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(110, 30, 181, 16))
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(50, 80, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(230, 80, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        #직접입력 버튼
        self.connect(self.pushButton_2, SIGNAL("clicked()"), self.directInput)
        #취소버튼
        self.connect(self.pushButton, SIGNAL("clicked()"), self.cancelButton)


    def retranslateUi(self, Form):
        Form.setWindowTitle(QtWidgets.QApplication.translate("Form", "Form", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("Form", "고객 정보 입력 대기 중", None, -1))
        self.pushButton.setText(QtWidgets.QApplication.translate("Form", "취소", None, -1))
        self.pushButton_2.setText(QtWidgets.QApplication.translate("Form", "직접입력", None, -1))

    def directInput(self):
        self.instance = socketClient.socketCreate()
        #코드 값에 따라 다르게 소켓통신 분리
        self.instance.code = '2000'
        self.returnMsg = self.instance.clientSocket()

    def cancelButton(self):
        print('취소버튼 클릭')
        self.close()
        self.parentUi.show()
        self.instance = socketClient.socketCreate()
        #코드 값에 따라 다르게 소켓통신 분리
        self.instance.code = '3000'
        self.returnMsg = self.instance.clientSocket()

class accRecvWaitPopup(QWidget):
    def __init__(self):
        QWidget.__init__(self)

    def paintEvent(self, e):
        dc = QPainter(self)
        dc.drawLine(100, 100, 200, 200)
        dc.drawLine(200, 100, 100, 200)

# class Main(Qwidget):
#     def __init__(self):
#         UiTest()

class Main(QWidget, UiTest.Ui_Form):
    def __init__(self, parent): 
        self.signalVal = None
        self.sndWait = None
        self.sendThread = None
        # 부모 클래스 생성자 호출 
        super(Main, self).__init__() 

        # 부모 메소드 호출
        self.setupUi(self)

        self.pressed = None

        self.initUi() 

        self.parent = parent
    
    # 마우스 Press 이벤트
    def mousePressEvent(self, event):
        if event.button() == Qt.RightButton:
            self.pressed = True
            self.offset = event.pos()
    
    #마우스 Move 이벤트
    def mouseMoveEvent(self, event):
        if self.pressed is True:
            x = event.globalX()
            y = event.globalY()
            x_w = self.offset.x()
            y_w = self.offset.y()
            self.move(x-x_w, y-y_w)

    #마우스 Release 이벤트
    def mouseReleaseEvent(self, event):
        self.pressed = False
        
    def initUi(self):
        self.setWindowFlags(Qt.FramelessWindowHint)

        #적립버튼 누를시 이벤트 (sendDeady에서 새로운 위젯 팝업 세팅 및 쓰레드 스타트)
        self.connect(self.accumulatebtn, SIGNAL("clicked()"), self.sendReady)

        # threadDone() Signal 연결
        self.sendThread = WorkerSendThread()
        self.connect(self.sendThread, SIGNAL("threadDone()"), self.sendThreadDone)

        self.recvThread = WorkerReceivThread()
        self.connect(self.recvThread, SIGNAL("threadDone()"), self.receivThreadDone)
            
    
    def sendReady(self):
        #QMessageBox.information(self, "Info", "적립하기 클릭")
        #새로운 위젯 생성       
        
        #self   .sndWait = accSendWaitPopup(self)
        self.sndWait = accSendWaitPopup(self)
        self.sndWait.setGeometry(QRect(100, 100, 400, 200))
        self.sndWait.show()
        
        #메인창 닫기
        self.close()
        self.sendThread.start()
    
    def gb_Animation_Start(self): 
        # str -> PySide2 QByteArray
        self.gb_Animation = QPropertyAnimation(self, b"size") 
        self.gb_Animation.setDuration(800) 
        self.gb_Animation.setEasingCurve(QEasingCurve.InOutBack) 
        self.gb_Animation.setEndValue(QSize(self.width(), self.height()-170)) 
        self.gb_Animation.start()

    def resizeEvent(self, evt=None): 
        pass 

    #보내는 쓰레드 종료
    def sendThreadDone(self):

        print('쓰레드 종료')
        # self.sndWait.close()
        # self.recvWait = accRecvWaitPopup()
        # self.recvWait.setGeometry(QRect(100, 100, 400, 200))
        # self.recvWait.show()

        print('bbbb',self.sendThread.returnMsg)
        
        if self.sendThread.returnMsg != "b'OK'": #서버 통신 비정상
            QMessageBox.information(self, "Info", "서버와의 통신이 원활하지 않습니다.")
            self.sndWait.close()
        elif self.sendThread.returnMsg == "b'OK'" : #서버 통신 정상 (다시 리시브 소켓 생성)
            print('서버통신 정상')
            self.recvThread.start()
            #self.close()  
            #self.sndWait.close()
        
        print("sendThreadDone")
        #QMessageBox.warning(self, "Warning", "Send Thread done.")

    #받는 쓰레드 종료
    def receivThreadDone(self):

        print('받는 쓰레드 종료')

        self.sndWait = accCompPopup()
        self.sndWait.setGeometry(QRect(100, 100, 400, 200))
        self.sndWait.show()


#보내는 쓰레드 (POST에서 직접입력: tablet 입력 중지)
class WorkerSendThread2(QThread):
    def __init__(self, parent=None):
        self.returnMsg = None
        super(WorkerSendThread, self).__init__(parent)

    def run(self):
        print("쓰레드 실행")
        self.instance = socketClient.socketCreate()
        #코드 값에 따라 다르게 소켓통신 분리
        self.instance.code = '1000'
        self.returnMsg = self.instance.clientSocket()
        #self.returnMsg = socketClient.socketCreate(self)
        print('리턴값:', self.returnMsg)
        # 커스텀 시그널 발행
        #self.emit(SIGNAL("threadDone()"))
        self.emit(SIGNAL("threadDone()"))


#보내는 쓰레드 (포인트 적립)
class WorkerSendThread(QThread):
    def __init__(self, parent=None):
        self.returnMsg = None
        super(WorkerSendThread, self).__init__(parent)

    def run(self):
        print("쓰레드 실행")
        self.code = '1000'
        self.instance = socketClient.socketCreate()
        #코드 값에 따라 다르게 소켓통신 분리
        self.instance.code = '1000'
        self.returnMsg = self.instance.clientSocket()
        #self.returnMsg = socketClient.socketCreate(self)
        print('리턴값:', self.returnMsg)
        # 커스텀 시그널 발행
        #self.emit(SIGNAL("threadDone()"))
        self.emit(SIGNAL("threadDone()"))

#받는 쓰레드
class WorkerReceivThread(QThread):
    def __init__(self, parent=None):
        self.returnMsg = None
        self.resultCd = None
        super(WorkerReceivThread, self).__init__(parent)

    def run(self):
        print("쓰레드 실행")
        self.returnMsg = socketServer.socketCreate()
        self.resultCd = self.returnMsg['resultCd']
        print('리턴값:', self.returnMsg)
        # 커스텀 시그널 발행
        #self.emit(SIGNAL("threadDone()"))
        self.emit(SIGNAL("threadDone()"))

def main(): 
    app = QApplication(sys.argv) 
    win = Main(None) 
    win.show() 
    sys.exit(app.exec_()) 
            
if __name__ == '__main__': 
    main()