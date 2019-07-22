from PyQt4.QtGui import *
from PyQt4.QtCore import *
import sys


class MyDialog(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.WINDOW_HEIGHT = 500
        self.WINDOW_WIDTH = 1000 

        self.setWindowTitle('Secret Master') 
        self.setGeometry(600,400,self.WINDOW_WIDTH, self.WINDOW_HEIGHT) #위치, 크기
        self.setWindowIcon(QIcon('images/Lock.png'))
        self.statusBar().showMessage('준비')
        self.setMinimumSize(1000, 500)
        self.setMaximumSize(1000, 500)


#-----------------------------------------------------------------------------------------------------------------------------        
        

        font = QFont('', 13) 
        self.subClass = None
        MyDialog.KeyArrayList = [{'a':'b','b':'c','c':'d','d':'e','e':'f','f':'g','g':'h','h':'i','i':'j','j':'k','k':'l','l':'m','m':'n','n':'o','o':'p','p':'q','q':'r','r':'s','s':'t','t':'u','u':'v','v':'w','w':'x','x':'y','y':'z','z':'a'}]
        MyDialog.SolveKeyArrayList = [{'b':'a','c':'b','d':'c','e':'d','f':'e','g':'f','h':'g','i':'h','j':'i','k':'j','l':'k','m':'l','n':'m','o':'n','p':'o','q':'p','r':'q','s':'r','t':'s','u':'t','v':'u','w':'v','x':'w','y':'x','z':'y','a':'z'}]
        self.addKeyVal = ''
        self.KeyItem = None
        self.inputWord = None
        self.SolveKeyItem = None
        MyDialog.MainWindowState = 'FirstMain'

        self.BackGround = QLabel(self)
        self.BackGround.setPixmap(QPixmap('images/BackGround.jpg'))
        self.BackGround.resize(1000,500)
        self.BackGround.move(0, 0)

        self.MainSecretBtn = QPushButton('암호문 복호화', self) #버튼 객체 생성
        self.MainSecretBtn.setToolTip('<b>암호문 복호화</b>') #커서를 가져다 대면 메시지 출력
        self.MainSecretBtn.resize(300,70) #사이즈 변경
        self.MainSecretBtn.move(100, 300) #좌표로 이동
        self.MainSecretBtn.setFont(font)
        self.MainSecretBtn.clicked.connect(self.btnClicked) #눌려졌을 때 이벤트 처리

        self.MainSolveBtn = QPushButton('평문 암호화', self)
        self.MainSolveBtn.setToolTip('<b>평문 암호화</b>')
        self.MainSolveBtn.resize(300,70)
        self.MainSolveBtn.move(600, 300)
        self.MainSolveBtn.setFont(font)
        self.MainSolveBtn.clicked.connect(self.btnClicked2)

        self.MainImage = QLabel(self)
        pixmap = QPixmap('images/MainLock.png')
        self.MainImage.resize(200, 200)
        self.MainImage.move(400, 50)
        self.MainImage.setPixmap(pixmap)

        self.SecretLabel = QLabel('복  호  화',self)
        self.SecretLabel.setFont(QFont('', 45))
        self.SecretLabel.resize(400, 60)
        self.SecretLabel.move(350, 30)
        self.SecretLabel.hide()

        self.getSecret = QTextEdit(self)
        self.getSecret.resize(700,40)
        self.getSecret.move(150, 110)
        self.getSecret.hide()

        self.SecretHelp = QLabel('↑여기에 입력해 주세요',self)
        self.SecretHelp.move(150,155)
        self.SecretHelp.resize(170, 30)
        self.SecretHelp.setFont(QFont('', 10))
        self.SecretHelp.hide()
        
        self.SecretKeyBtn = QPushButton('Modify key list', self)
        self.SecretKeyBtn.move(0, 200)
        self.SecretKeyBtn.resize(150, 50)
        self.SecretKeyBtn.setFont(QFont('', 15))
        self.SecretKeyBtn.clicked.connect(self.ModifyClicked)
        self.SecretKeyBtn.hide()

        self.SecretStart = QPushButton('Start', self)
        self.SecretStart.move(0, 250)
        self.SecretStart.resize(150, 50)
        self.SecretStart.setFont(QFont('', 15))
        self.SecretStart.clicked.connect(self.startBuild)
        self.SecretStart.hide()

        self.SecretShowLabel = QListWidget(self)
        self.SecretShowLabel.resize(700, 300)
        self.SecretShowLabel.move(150, 200)
        self.SecretShowLabel.setFont(QFont('',15))
        self.SecretShowLabel.addItem('123')
        self.SecretShowLabel.hide()

        self.KeyLabel = QLabel('Keys', self)
        self.KeyLabel.move(450, 25)
        self.KeyLabel.resize(150, 60)
        self.KeyLabel.setFont(QFont('', 40))
        self.KeyLabel.hide()

        MyDialog.KeyList = QListWidget(self)
        MyDialog.KeyList.resize(700, 350)
        MyDialog.KeyList.move(150, 150)
        MyDialog.KeyList.setFont(QFont('',15))
        MyDialog.KeyList.addItem('a:b,b:c,c:d,d:e,e:f,f:g,g:h,h:i,i:j,j:k,k:l,l:m,m:n,n:o,o:p,p:q,q:r,r:s,s:t,t:u,u:v,v:w,w:x,x:y,y:z,z:a')
        MyDialog.KeyList.itemClicked.connect(self.listClicked)
        MyDialog.KeyList.hide()

        self.addKey = QPushButton('add Key', self)
        self.addKey.resize(150, 50)    
        self.addKey.move(0,150)
        self.addKey.setFont(QFont('', 15))
        self.addKey.clicked.connect(self.addKeyClicked)
        self.addKey.hide()

        self.deleteKey = QPushButton('delete Key', self)
        self.deleteKey.resize(150, 50)
        self.deleteKey.move(0, 200)
        self.deleteKey.setFont(QFont('', 15))
        self.deleteKey.clicked.connect(self.DeleteKey)
        self.deleteKey.hide()

        self.deleteAll = QPushButton('delete All', self)
        self.deleteAll.resize(150, 50)
        self.deleteAll.move(0, 250)
        self.deleteAll.setFont(QFont('', 15))
        self.deleteAll.clicked.connect(self.deleteAllClicked)
        self.deleteAll.hide()

        self.SolveLabel = QLabel('암 호 화', self)
        self.SolveLabel.setFont(QFont('', 45))
        self.SolveLabel.move(350, 30)
        self.SolveLabel.resize(400, 60)
        self.SolveLabel.hide()

        self.getSolve = QTextEdit(self)
        self.getSolve.resize(700, 40)
        self.getSolve.move(150, 110)
        self.getSolve.hide()

        self.SolveHelp = QLabel('↑여기에 입력해 주세요', self)
        self.SolveHelp.setFont(QFont('', 10))
        self.SolveHelp.resize(170, 50)
        self.SolveHelp.move(150, 155)
        self.SolveHelp.hide()

        self.SolveKeyBtn = QPushButton('Modify key list', self)
        self.SolveKeyBtn.resize(150, 50)
        self.SolveKeyBtn.move(0, 200)
        self.SolveKeyBtn.setFont(QFont('', 15))
        self.SolveKeyBtn.clicked.connect(self.SolveModifyClicked)
        self.SolveKeyBtn.hide()

        self.SolveStart = QPushButton('Start', self)
        self.SolveStart.resize(150, 50)
        self.SolveStart.move(0, 250)
        self.SolveStart.setFont(QFont('', 15))
        self.SolveStart.clicked.connect(self.SolveStartClicked)
        self.SolveStart.hide()

        self.ShowSolveLabel = QListWidget(self)
        self.ShowSolveLabel.resize(700, 300)
        self.ShowSolveLabel.move(150, 200)
        self.ShowSolveLabel.setFont(QFont('', 15))
        self.ShowSolveLabel.hide()

        self.SolveKeyLabel = QLabel('Keys', self)
        self.SolveKeyLabel.move(400, 25)
        self.SolveKeyLabel.resize(150, 60)
        self.SolveKeyLabel.setFont(QFont('', 40))
        self.SolveKeyLabel.hide()

        MyDialog.SolveKeyList = QListWidget(self)
        MyDialog.SolveKeyList.move(150, 150)
        MyDialog.SolveKeyList.resize(700, 350)
        MyDialog.SolveKeyList.setFont(QFont('', 15))
        MyDialog.SolveKeyList.addItem('b:a,c:b,d:c,e:d,f:e,g:f,h:g,i:h,j:i,k:j,l:k,m:l,n:m,o:n,p:o,q:p,r:q,s:r,t:s,u:t,v:u,w:v,x:w,y:x,z:y,a:z')
        MyDialog.SolveKeyList.itemClicked.connect(self.SolveItemClicked)
        MyDialog.SolveKeyList.hide()

        self.SolveAddKey = QPushButton('addKey', self)
        self.SolveAddKey.move(0, 150)
        self.SolveAddKey.resize(150, 50)
        self.SolveAddKey.setFont(QFont('', 15))
        self.SolveAddKey.clicked.connect(self.SolveAddKeyClicked)
        self.SolveAddKey.hide()

        self.SolveDeleteKey = QPushButton('delete key', self)
        self.SolveDeleteKey.move(0, 200)
        self.SolveDeleteKey.resize(150, 50)
        self.SolveDeleteKey.setFont(QFont('', 15))
        self.SolveDeleteKey.clicked.connect(self.SolveDeleteKeyClicked)
        self.SolveDeleteKey.hide()

        self.SolveDeleteAll = QPushButton('delete All', self)
        self.SolveDeleteAll.move(0, 250)
        self.SolveDeleteAll.resize(150,50)
        self.SolveDeleteAll.setFont(QFont('', 15))
        self.SolveDeleteAll.clicked.connect(self.SolveDeleteAllClicked)
        self.SolveDeleteAll.hide()

        self.BackButton = QPushButton(self)
        self.BackButton.move(0, 0)
        self.BackButton.resize(50, 50)
        self.BackButton.setIcon(QIcon(QPixmap('images/back.png')))
        self.BackButton.setIconSize(QSize(50, 50))
        self.BackButton.setStyleSheet("background-color: white")
        # self.BackButton.setStyleSheet("border-image: url(images/back.png); background-color:white;") #background image 설정
        self.BackButton.clicked.connect(self.MainBackClicked)
        self.BackButton.hide()

        self.connect(self, SIGNAL("quit()"), self.closeEvent)

        self.show() 

#-----------------------------------------------------------------------------------------------------------------------------------------------------
   

    def listClicked(self, item):
        self.KeyItem = item

    def btnClicked(self):
        self.MainSecretBtn.hide()
        self.MainSolveBtn.hide()
        self.MainImage.hide()       
        self.BackGround.hide()
        
        self.SecretLabel.show()
        self.getSecret.show()
        self.SecretHelp.show()
        self.SecretShowLabel.show()
        self.SecretKeyBtn.show()
        self.SecretStart.show()
        self.BackButton.show()
        MyDialog.MainWindowState = 'Lock'


    def btnClicked2(self):
        self.MainSecretBtn.hide()
        self.MainSolveBtn.hide()
        self.MainImage.hide()
        self.BackGround.hide()

        self.SolveLabel.show()
        self.getSolve.show()
        self.SolveHelp.show()
        self.SolveKeyBtn.show()
        self.SolveStart.show()
        self.ShowSolveLabel.show()
        self.BackButton.show()
        MyDialog.MainWindowState = 'Solve'

    def ModifyClicked(self):
        self.SecretLabel.hide()
        self.getSecret.hide()
        self.SecretHelp.hide()
        self.SecretShowLabel.hide()
        self.SecretKeyBtn.hide()
        self.SecretStart.hide()

        self.KeyLabel.show()
        MyDialog.KeyList.show()
        self.addKey.show()
        self.deleteKey.show()
        self.deleteAll.show()
        MyDialog.MainWindowState = 'LockKey'

    def startBuild(self):
        self.SecretShowLabel.clear()
        for a in range(len(MyDialog.KeyArrayList)):
            self.inputWord = list(self.getSecret.toPlainText()) #텍스트 에디트에서 값을 받아욤
            self.RealWord = ''    
            for wod in range(len(self.inputWord)):        
                for b in MyDialog.KeyArrayList[a]:
                    if self.inputWord[wod] == b:
                        self.inputWord[wod] = MyDialog.KeyArrayList[a][b]
                        break
            for i in self.inputWord:
               self.RealWord += i
            self.SecretShowLabel.addItem(self.RealWord)

    def addKeyClicked(self):
        self.subClass = subKey() 
        self.subClass.show()
            
    def DeleteKey(self):
        if MyDialog.KeyList.isItemSelected(self.KeyItem):
            del(MyDialog.KeyArrayList[MyDialog.KeyList.selectedIndexes()[0].row()])
            MyDialog.KeyList.takeItem(MyDialog.KeyList.selectedIndexes()[0].row())

    def deleteAllClicked(self):
        MyDialog.KeyArrayList = []
        MyDialog.KeyList.clear()

    def closeEvent(self, event):
        if self.subClass != None:
            self.subClass.close()

    def SolveModifyClicked(self):
        self.SolveLabel.hide()
        self.SolveKeyBtn.hide()
        self.SolveHelp.hide()
        self.SolveStart.hide()
        self.getSolve.hide()
        self.ShowSolveLabel.hide()

        self.KeyLabel.show()
        MyDialog.SolveKeyList.show()
        self.SolveAddKey.show()
        self.SolveDeleteKey.show()
        self.SolveDeleteAll.show()
        MyDialog.MainWindowState = 'SolveKey'

    def SolveStartClicked(self):
        self.ShowSolveLabel.clear()
        for a in range(len(MyDialog.SolveKeyArrayList)):
            self.SolveinputWord = list(self.getSolve.toPlainText()) #텍스트 에디트에서 값을 받아욤
            self.SolveRealWord = ''    
            for wod in range(len(self.SolveinputWord)):        
                for b in MyDialog.SolveKeyArrayList[a]:
                    if self.SolveinputWord[wod] == b:
                        self.SolveinputWord[wod] = MyDialog.SolveKeyArrayList[a][b]
                        break
            for i in self.SolveinputWord:
               self.SolveRealWord += i
            self.ShowSolveLabel.addItem(self.SolveRealWord)

    def SolveItemClicked(self, item):
        self.SolveKeyItem = item

    def SolveAddKeyClicked(self):
        self.subClass = subKey()
        self.subClass.show()

    def SolveDeleteKeyClicked(self):
        if MyDialog.SolveKeyList.isItemSelected(self.SolveKeyItem):
            del(MyDialog.SolveKeyArrayList[MyDialog.SolveKeyList.selectedIndexes()[0].row()])
            MyDialog.SolveKeyList.takeItem(MyDialog.SolveKeyList.selectedIndexes()[0].row())


    def SolveDeleteAllClicked(self):
        MyDialog.SolveKeyList.clear()
        MyDialog.SolveKeyArrayList = []


    def MainBackClicked(self):
        if MyDialog.MainWindowState == 'Lock':
            MyDialog.MainWindowState = 'FirstMain'
            self.BackGround.show()
            self.MainSecretBtn.show()
            self.MainSolveBtn.show()
            self.MainImage.show()

            self.SecretLabel.hide()
            self.getSecret.hide()
            self.SecretShowLabel.hide()
            self.SecretKeyBtn.hide()
            self.SecretStart.hide()
            self.SecretHelp.hide()
            self.BackButton.hide()

        elif MyDialog.MainWindowState == 'LockKey':
            MyDialog.MainWindowState = 'Lock'
            self.KeyLabel.hide()
            MyDialog.KeyList.hide()
            self.addKey.hide()
            self.deleteKey.hide()
            self.deleteAll.hide()

            self.SecretLabel.show()
            self.getSecret.show()
            self.SecretShowLabel.show()
            self.SecretKeyBtn.show()
            self.SecretStart.show()
            self.SecretHelp.show()  

        elif MyDialog.MainWindowState == 'Solve':
            MyDialog.MainWindowState = 'FirstMain'
            self.SolveLabel.hide()
            self.SolveHelp.hide()
            self.SolveKeyBtn.hide()
            self.getSolve.hide()
            self.ShowSolveLabel.hide()
            self.SolveStart.hide()
            self.BackButton.hide()

            self.BackGround.show()
            self.MainSecretBtn.show()
            self.MainSolveBtn.show()
            self.MainImage.show()

        elif MyDialog.MainWindowState == 'SolveKey':
            MyDialog.MainWindowState = 'Solve'
            self.SolveLabel.show()
            self.SolveKeyBtn.show()
            self.SolveHelp.show()
            self.SolveStart.show()
            self.getSolve.show()
            self.ShowSolveLabel.show()

            self.KeyLabel.hide()
            MyDialog.SolveKeyList.hide()
            self.SolveAddKey.hide()
            self.SolveDeleteKey.hide()
            self.SolveDeleteAll.hide()




#--------------------------------------------------------------------------------
class subKey(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.setWindowTitle("add Key")
        self.setWindowIcon(QIcon('images/Key.png'))
        self.resize(500, 200)
        self.statusBar().showMessage('Key')
        self.setMaximumSize(500,200)
        self.setMinimumSize(500, 200)

        self.KeyInput = QLineEdit(self)
        self.KeyInput.resize(450, 30)
        self.KeyInput.setFont(QFont('', 10))
        self.KeyInput.move(25, 30)

        self.ShowLabel = QLabel('↑여기에 원래 문자:바꿀 키, 키:바꿀 값 이런식으로 작성해주세요\n예: a:b,c:h,j:q 키:a,c,j 값:b,h,q\n∴만약 키 혹은 값 안에 문자열이 들어가면 에러가 일어납니다', self)
        self.ShowLabel.resize(450, 45)
        self.ShowLabel.move(25, 65)
        self.ShowLabel.setFont(QFont('', 10))

        self.finishButton = QPushButton('O K', self)
        self.finishButton.resize(100, 35)
        self.finishButton.move(340,120)
        self.finishButton.setFont(QFont('', 13))
        self.finishButton.clicked.connect(self.finished)

        self.show()

    def finished(self):
        word = self.KeyInput.text()
        state = 'key'
        thisKey = None
        thisValues = None
        wordFinish = 'no'
        outLoop = 'no'
        isError = 'no'
        if MyDialog.MainWindowState == 'LockKey':
            MyDialog.KeyArrayList.append({})
        elif MyDialog.MainWindowState == 'SolveKey':
            MyDialog.SolveKeyArrayList.append({})
        for a in word:
            if a != ':' and state == 'None':
                QMessageBox.information(self, 'error', '형식에 맞게 쓰지 않았습니다')
                if MyDialog.MainWindowState == 'LockKey':
                    del(MyDialog.KeyArrayList[len(MyDialog.KeyArrayList) - 1])
                elif MyDialog.MainWindowState == 'SolveKey':
                    del(MyDialog.SolveKeyArrayList[len(MyDialog.SolveKeyArrayList) - 1])
                outLoop = 'yes'

            if outLoop == 'yes':
                isError = 'yes'
                break

            if wordFinish == 'yes':
                wordFinish = 'no'
                if MyDialog.MainWindowState == 'LockKey':
                    MyDialog.KeyArrayList[len(MyDialog.KeyArrayList) - 1][thisKey] = thisValue
                elif MyDialog.MainWindowState == 'SolveKey':
                    MyDialog.SolveKeyArrayList[len(MyDialog.SolveKeyArrayList) - 1][thisKey] = thisValue
                thiskey = None
                thisvalues = None

            if state == 'key':
                state = 'None'
                thisKey = a
                continue

            if state == 'value':
                thisValue = a
                state = 'sleep'
                wordFinish = 'yes'
                continue

            if state == 'None':
                state = 'value'
                continue

            if state == 'sleep':
                state = 'key'
                continue
        if isError != 'yes':
            if MyDialog.MainWindowState == 'LockKey':
                MyDialog.KeyArrayList[len(MyDialog.KeyArrayList) - 1][thisKey] = thisValue
            elif MyDialog.MainWindowState == 'SolveKey':
                MyDialog.SolveKeyArrayList[len(MyDialog.SolveKeyArrayList) - 1][thisKey] = thisValue  
        
        if isError == 'yes':
            pass
        elif MyDialog.MainWindowState == 'LockKey':
            MyDialog.KeyList.addItem(word)
        elif MyDialog.MainWindowState== 'SolveKey':
            MyDialog.SolveKeyList.addItem(word)
        
        self.close()

#----------------------------------------------------------------

def main():
    app = QApplication(sys.argv)
    ex = MyDialog()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
