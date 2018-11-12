from socket import *
from select import *
import sys
from time import ctime
import socket
class socketCreate():
    def __init__(self):
        self.code = None
        self.ipAdress = socket.gethostbyname(socket.getfqdn())
        #self.HOST = 'localhost' #localhost
        self.HOST = socket.gethostbyname(socket.getfqdn())
        self.PORT = 9876

    def clientSocket(self):
        print('####@@@@@@@code3:', self.code)
        print("@@@@@@@@@@@IPADRESS:", self.HOST)
        #1000은 point값 보내 키패드 activity 요청
        try:
            if self.code == '1000':
                print('테블릿에서 적립 진행합니다.')
                s=socket.socket(socket.AF_INET, socket.SOCK_STREAM) #소켓생성
                s.connect((self.HOST,self.PORT))
                tmp = '100point 적립창 띄우세요'
                msg = bytearray(tmp, 'utf-8')
                s.send(msg) #문자를 보냄
                data=s.recv(1024) #서버로 부터 정보를 받음
                s.close()
                print('Received',repr(data))
                return repr(data)
            elif self.code == '2000' :

                print('POS에서 적립 진행합니다. 입력창 중지하세요')
                s=socket.socket(socket.AF_INET, socket.SOCK_STREAM) #소켓생성
                s.connect((self.HOST,self.PORT))
                tmp = 'POS에서 적립 진행합니다. 입력창 중지하세요'
                msg = bytearray(tmp, 'utf-8')
                s.send(msg) #문자를 보냄
                data=s.recv(1024) #서버로 부터 정보를 받음
                s.close()
                print('Received',repr(data))
                return repr(data)
            elif self.code == '3000' :

                print('적립 취소입니다.')
                s=socket.socket(socket.AF_INET, socket.SOCK_STREAM) #소켓생성
                s.connect((self.HOST,self.PORT))
                tmp = 'POS에서 적립 취소합니다.'
                msg = bytearray(tmp, 'utf-8')
                s.send(msg) #문자를 보냄
                data=s.recv(1024) #서버로 부터 정보를 받음
                s.close()
                print('Received',repr(data))
                return repr(data)
        except Exception as e:
            print('EXCEPTION!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
            print(e)


