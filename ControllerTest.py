from PySide2.QtWidgets import *
from PySide2.QtCore import *
import sys

import MainTest
import UiEx
import PospotMainDialog

class ControllerTest():
    def __init__(self): 
        super(ControllerTest, self).__init__() 
        #self.ui() 
        #self.show() 
        self.selectedMain = None
        self.autoLogin = False
        self.auth = False

        # Auth Check
        if self.autoLogin is False and self.auth is False:
            self.selectedMain = UiEx.Main(self)
            #self.connect(self.selectedMain, SIGNAL("authDone()"), self.loadMainAfterAuth)
            print("auth plz~")
        else:
            self.selectedMain = MainTest.Main(self)
            print("auth ok~")

    def loadMain(self):
        if self.selectedMain is not None:
            return self.selectedMain
        else:
            print("pass")
            pass  # 예외처리 필요?

    def authorized(self):
        self.auth = True
        #del self.selectedMain
        self.selectedMain = MainTest.Main(self)

    def autoLogined(self):
        self.autoLogin = True
    
    #@Slot()
    def loadMainAfterAuth(self):
        self.authorized()
        self.loadMain().show()
        print("loadMainAfterAuth")

def main(): 
    app = QApplication(sys.argv) 
    #? ControllerTest().loadMain().show()
    
    con = ControllerTest()
    con.loadMain().show()
    
    sys.exit(app.exec_()) 
            
if __name__ == '__main__': 
    main()