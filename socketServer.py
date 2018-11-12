import socket
import json

def decoding(recvMsg):
    Msg = recvMsg
    decodeMsg = Msg.decode()
    return decodeMsg

def socketCreate():
    try:
        s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        print("소켓 생성완료")
    except socket.error as err :
        print("에러 발생 원인 :  %s"%(err))
    
    temp="서버에서 클라이언트로 보내는 메세지입니다"
    msg=bytearray(temp,'utf-8')
    HOST='localhost'
    port=1234
    s.bind((HOST,port))
    s.listen(5)
    print("%d 포트로 연결을 기다리는중"%(port))
    #while True:
    print('aaaa')
    c, addr = s.accept()
    print(addr,"사용자가 접속함")
    c.send(msg)
    a = decoding(c.recv(1024))
    dict = json.loads(a)
    name = dict['name']
    print("name", dict['name'])
    print("phone", dict['phone'])
    print("성별", dict['성별'])
    print("resultCd", dict['resultCd'])
   
    return dict
    c.close()
    #return None

