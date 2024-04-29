# PyQt stuff
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

# Ui stuff
from Login import Ui_loginWindow 
from Signup import Ui_signupWindow
from Warning import Ui_warningWindow
from Mainmenu import Ui_MainWindow

# Others
import sys
import backend
import re



class windowManager(QWidget):
    
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.initLogin() # opens login menu
        self.loginWindow.loggedIn.connect(self.initMain) # sucessfully logged in


    def initLogin(self):

        self.loginWindow = login()
        self.loginWindow.show()
    
    
    def initMain(self):

        self.mainmenu = mainmenu()
        self. mainmenu.show()

        self.loginWindow.close()






class mainmenu(QMainWindow, Ui_MainWindow): 

    def __init__(self, *args, **kwargs): 
        super(mainmenu, self).__init__(*args, **kwargs)
        self.setupUi(self) # triggers the set up of the interface



























class login(QMainWindow, Ui_loginWindow): 
    '''
    A class representing the login menu. 

    Attributes(non Qt attributes):
        - closed: custom signal
        - successLogin : checks if login input is correct and logs in user
        - dragPos : handles Qpoint() class for window dragging functionality
        - loggedIn : custom signal

    Methods:
        - loginAccount() : if input is valid then logs user into his/her account
        - signupWindowI(event) : initializez signup window
        - warningMsg(text) : initializes warning window
        - mousePressEvent(event) : controls dragging of window
        - mouseMoveEvent(event) : controls dragging of window
        - mouseReleaseEvent(event) : controls dragging of window
        - exitLogin() : exits application
    '''

    loggedIn = pyqtSignal()

    def __init__(self, *args, **kwargs) -> None: 
        super(login, self).__init__(*args, **kwargs)
        self.setupUi(self) 

        # Setting up the window to be borderless
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.statusBar().setSizeGripEnabled(False)

        
        self.exitButton.clicked.connect(self.close) # exit button 
        self.loginButton.clicked.connect(self.loginAccount) # login button
        self.successLogin = False

        self.dragPos = QPoint() # drag window

        self.signupLabel.mousePressEvent = self.initSignup # signup text click


    def loginAccount(self) -> None:
        '''
        Logs into account
        '''

        userID = self.useridlineEdit.text()
        userPassword = self.passwordlineEdit.text()
        self.successLogin = backend.validate_user_login(userID, userPassword)

        if self.successLogin:
            self.loggedIn.emit()
        else:
            self.warningMsg("User ID or Password is incorrect")
      
         
    def initSignup(self, event) -> None:
        '''
        Initializes signup window
        '''

        self.setupSignupWindow = signup()
        self.setupSignupWindow.show()


    def warningMsg(self, text: str) -> None:
        '''
        Initializes warning window

        Parameters:
            - text : warning message
        '''

        self.setupWarningWindow = warning()
        self.setupWarningWindow.show()
        self.setupWarningWindow.warningText.setText(text)


    def mousePressEvent(self, event) -> None:
        '''
        Controls dragging of window
        
        Parameters:
            - event
        '''

        if event.button() == Qt.LeftButton:
            self.dragPos = event.globalPos()
            event.accept()


    def mouseMoveEvent(self, event) -> None:
        '''
        Controls dragging of window

        Parameters:
            - event
        '''

        if event.buttons() == Qt.LeftButton and self.dragPos:
            self.move(self.pos() + event.globalPos() - self.dragPos)
            self.dragPos = event.globalPos()
            event.accept()


    def mouseReleaseEvent(self, event) -> None:
        '''
        Controls dragging of window
        
        Parameters:
            - event
        '''

        self.dragPos = QPoint()



class signup(QMainWindow, Ui_signupWindow): 
    '''
    A class representing the signup menu. 

    Attributes(non Qt attributes):
        - successSignup : checks for successful signup
        - dragPos : handles Qpoint() class for window dragging functionality

    Methods:
        - signupAccount() : inserts data into database
        - validateInput(userEmail, userPassword, userName, userCity, userTimezone) : validates user input
        - validEmail(userEmail) : validates email address
        - warningMsg(text) : initializes warning window
        - mousePressEvent(event) : controls dragging of window
        - mouseMoveEvent(event) : controls dragging of window
        - mouseReleaseEvent(event) : controls dragging of window
    '''

    def __init__(self, *args, **kwargs): 
        super(signup, self).__init__(*args, **kwargs)
        self.setupUi(self) # triggers the set up of the interface

        # Setting up the window to be borderless
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.CustomizeWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.statusBar().setSizeGripEnabled(False)

        self.returnButton.clicked.connect(self.close) # return button

        self.dragPos = QPoint() # drag window

        self.signupButton.clicked.connect(self.signupAccount) # login button
        self.successSignup = False

    def signupAccount(self):
        '''
        Validates and inserts data into database
        '''

        userEmail = self.lineEdit_1.text()
        userPassword = self.lineEdit_2.text()
        userName = self.lineEdit_3.text()
        userCity = self.lineEdit_4.text()
        userTimezone = self.lineEdit_5.text()

        self.successSignup = self.validateInput( userEmail, userPassword, userName, userCity, userTimezone)

        if self.successSignup:
            self.userID = backend.user_signup(userPassword, userName, userEmail, userCity.capitalize(), float(userTimezone))
            self.close()
            #open main window...

    def validateInput(self, userEmail, userPassword, userName, userCity, userTimezone):
        '''
        Validates input

        Parameters:
            - userEmail : email
            - userPassword : password
            - userName : name
            - userCity : city
            - userTimezone : timexone

        Returns:
            - Bool
        '''

        count = 0
        try:
            text = "Invalid Email"
            if self.validEmail(userEmail): count += 1

            text = "Invalid Password"
            if len(userPassword) > 0: count += 1

            text = "Invalid Username"
            if userName.isalnum(): count += 1

            text = "Invalid City"
            if userCity.isalpha(): count += 1

            text = "Invalid Timezone"
            timezone = float(userTimezone)
            if -12 <= timezone <= 14: count += 1

            return True if count == 5 else False # all correct return True else False
          
        except :
            self.warningMsg(text)
            return False
    
    def validEmail(self, userEmail):
        '''
        Validates email

        Parameters:
            - userEmail : email

        Returns:
            - True
            - exception
        '''

        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if re.match(pattern, userEmail) is not None:
            return True
        else:
            raise 
    
    def warningMsg(self, text):
        '''
        Initizes warning window

        Parameters:
            - text : warning message
        '''

        self.setupWarningWindow = warning()
        self.setupWarningWindow.show()
        self.setupWarningWindow.warningText.setText(text)

    def mousePressEvent(self, event):
        '''
        Controls dragging of window

        Parameters:
            - event
        '''

        if event.button() == Qt.LeftButton:
            self.dragPos = event.globalPos()
            event.accept()

    def mouseMoveEvent(self, event):
        '''
        Controls dragging of window

        Parameters:
            - event
        '''

        if event.buttons() == Qt.LeftButton and self.dragPos:
            self.move(self.pos() + event.globalPos() - self.dragPos)
            self.dragPos = event.globalPos()
            event.accept()

    def mouseReleaseEvent(self, event):
        '''
        Controls dragging of window

        Parameters:
            - event
        '''

        self.dragPos = QPoint()



class warning(QDialog, Ui_warningWindow): 
    '''
    A class representing the warning window. 

    Attributes(non Qt attributes):
        - dragPos : handles Qpoint() class for window dragging functionality

    Methods:
        - mousePressEvent(event) : controls dragging of window
        - mouseMoveEvent(event) : controls dragging of window
        - mouseReleaseEvent(event) : controls dragging of window
    
    '''

    def __init__(self, *args, **kwargs): 
        super(warning, self).__init__(*args, **kwargs)
        self.setupUi(self) # triggers the set up of the interface

        
        # Setting up the window to be borderless
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        self.dragPos = QPoint() # drag window

    def mousePressEvent(self, event):
        '''
        Controls dragging of window

        Parameters:
            - event 
        '''

        if event.button() == Qt.LeftButton:
            self.dragPos = event.globalPos()
            event.accept()

    def mouseMoveEvent(self, event):
        '''
        Controls dragging of window

        Parameters:
            - event 
        '''

        if event.buttons() == Qt.LeftButton and self.dragPos:
            self.move(self.pos() + event.globalPos() - self.dragPos)
            self.dragPos = event.globalPos()
            event.accept()

    def mouseReleaseEvent(self, event):
        '''
        Controls dragging of window

        Parameters:
            - event 
        '''

        self.dragPos = QPoint()
      








def closeApp():
    backend.logout_()
    QApplication.instance().quit()


def main():
    '''
    Main function
    '''

    database = "main/Database.db"
    backend.connect(database)

    app = QApplication(sys.argv)
    app.lastWindowClosed.connect(closeApp)  # Connect to the signal

    Window = windowManager()

    sys.exit(app.exec_())



if __name__ == '__main__':
    main()



