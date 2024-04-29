'''
from PyQt5 import QtWidgets

class MyWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.centralWidget = QtWidgets.QWidget(self)
        self.setCentralWidget(self.centralWidget)
        layout = QtWidgets.QVBoxLayout(self.centralWidget)

        # Create buttons
        self.button1 = QtWidgets.QPushButton("Action 1", self)
        self.button2 = QtWidgets.QPushButton("Action 2", self)

        # Add buttons to layout
        layout.addWidget(self.button1)
        layout.addWidget(self.button2)

        # Connect buttons to a method with different messages
        self.button1.clicked.connect(lambda: self.showWarningDialog("Warning: Action 1 might cause issues."))
        self.button2.clicked.connect(lambda: self.showWarningDialog("Warning: Action 2 is not recommended."))

    def showWarningDialog(self, message):
        dialog = QtWidgets.QMessageBox()
        dialog.setWindowTitle("Warning")
        dialog.setIcon(QtWidgets.QMessageBox.Warning)
        dialog.setText(message)
        dialog.exec_()



if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MyWindow()
    window.show()
    app.exec_()
'''





'''
from warning import Ui_warningWindow
from PyQt5.QtWidgets import QDialog, QDialogButtonBox, QVBoxLayout, QApplication


class WarningDialog(QDialog, Ui_warningWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        # You can add more initialization code here if needed


app = QApplication([])
dialog = WarningDialog()
dialog.warningText.setText("This is a warning message")  # Set your warning message here
result = dialog.exec_()

if result == QDialog.Accepted:
    print("The dialog was accepted")
else:
    print("The dialog was rejected")
'''


'''
from PyQt5.QtWidgets import QDialog, QDialogButtonBox, QVBoxLayout, QApplication

class WarningDialog(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Warning")

        self.buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        layout = QVBoxLayout()
        layout.addWidget(self.buttonBox)
        self.setLayout(layout)

# Usage
app = QApplication([])
dialog = WarningDialog()
result = dialog.exec_()
if result:
    print("Ok clicked")
else:
    print("Cancel clicked")
'''

'''
from PyQt5 import QtWidgets, QtCore

class BorderlessWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)  # Make the window borderless
        self._dragPos = QtCore.QPoint()

    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self._dragPos = event.globalPos()
            event.accept()

    def mouseMoveEvent(self, event):
        if event.buttons() == QtCore.Qt.LeftButton and self._dragPos:
            self.move(self.pos() + event.globalPos() - self._dragPos)
            self._dragPos = event.globalPos()
            event.accept()

    def mouseReleaseEvent(self, event):
        self._dragPos = QtCore.QPoint()

# Example Usage
if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = BorderlessWindow()
    window.show()
    app.exec_()
'''
'''
from PyQt5 import QtWidgets, uic

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main_window.ui', self)  # Load the UI file

        # Assuming you have buttons to switch screens
        self.buttonScreen1.clicked.connect(self.display_screen1)
        self.buttonScreen2.clicked.connect(self.display_screen2)

        # Assuming 'stackedWidget' is the objectName of your QStackedWidget in Qt Designer
        self.stackedWidget = self.findChild(QtWidgets.QStackedWidget, 'stackedWidget')

    def display_screen1(self):
        self.stackedWidget.setCurrentIndex(0)  # Switch to the first screen

    def display_screen2(self):
        self.stackedWidget.setCurrentIndex(1)  # Switch to the second screen

# Run the application
app = QtWidgets.QApplication([])
window = MainWindow()
window.show()
app.exec_()
'''


'''
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class App(QApplication):
    def __init__(self, sys_argv):
        super(App, self).__init__(sys_argv)
        self.main_window = MainWindow()

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setGeometry(100, 100, 400, 300)
        self.button_app_modal = QPushButton('Application Modal', self)
        self.button_app_modal.clicked.connect(self.show_application_modal_dialog)
        self.button_app_modal.move(50, 50)

        self.button_window_modal = QPushButton('Window Modal', self)
        self.button_window_modal.clicked.connect(self.show_window_modal_dialog)
        self.button_window_modal.move(50, 100)

        self.show()

    def show_application_modal_dialog(self):
        dialog = QDialog(self)
        dialog.setWindowTitle('Application Modal Dialog')
        dialog.setWindowModality(Qt.ApplicationModal)  # Application modal
        dialog.exec_()

    def show_window_modal_dialog(self):
        dialog = QDialog(self)
        dialog.setWindowTitle('Window Modal Dialog')
        dialog.setWindowModality(Qt.WindowModal)  # Window modal
        dialog.exec_()

if __name__ == '__main__':
    app = App(sys.argv)
    sys.exit(app.exec_())

'''
'''
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys # Only needed for access to command line arguments

class LoginWindow(QMainWindow):
    closed = pyqtSignal()  # Signal to be emitted when the window is closed

    def closeEvent(self, event):
        self.closed.emit()  # Emit the closed signal
        super().closeEvent(event)



app = QApplication(sys.argv)

window = LoginWindow()
window.show()



# Start the event loop.
app.exec_()
'''

'''
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtCore import pyqtSignal, QObject

class MyWidget(QWidget):
    my_signal = pyqtSignal()

    def __init__(self):
        super().__init__()

        self.button = QPushButton("Click me", self)
        self.button.clicked.connect(self.emit_signal)
        self.my_signal.connect(self.my_slot)

    def emit_signal(self):
        self.my_signal.emit()

    def my_slot(self):
        print("Signal was caught!")

if __name__ == "__main__":
    app = QApplication([])
    widget = MyWidget()
    widget.show()
    app.exec_()
'''

'''
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys # Only needed for access to command line arguments

class MyEmitter(QObject):
    my_signal = pyqtSignal(int, str)

    def do_something(self):
        self.my_signal.emit(42, "Hello")

class MyReceiver(QWidget):
    def __init__(self):
        super().__init__()
        self.emitter = MyEmitter()
        self.emitter.my_signal.connect(self.handle_signal)
        self.button = QPushButton("Emit Signal", self)
        self.button.clicked.connect(self.emitter.do_something)

    def handle_signal(self, number, text):
        print(f"Received number: {number}, text: '{text}'")

app = QApplication(sys.argv)
receiver = MyReceiver()
receiver.show()
sys.exit(app.exec_())
'''


from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys # Only needed for access to command line arguments

class LoginScreen(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout(self)
        self.login_button = QPushButton("Login", self)
        self.login_button.clicked.connect(self.login)
        self.layout.addWidget(self.login_button)

    def login(self):
        # Logic for login
        # On successful login, emit a signal or directly call a method to switch screens
        pass

class HomeScreen(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout(self)
        self.label = QLabel("Welcome to the Home Screen", self)
        self.layout.addWidget(self.label)

class MainApp(QWidget):
    def __init__(self):
        super().__init__()
        self.stacked_widget = QStackedWidget(self)
        self.login_screen = LoginScreen()
        self.home_screen = HomeScreen()

        self.stacked_widget.addWidget(self.login_screen)
        self.stacked_widget.addWidget(self.home_screen)

        self.layout = QVBoxLayout(self)
        self.layout.addWidget(self.stacked_widget)

        self.login_screen.login_button.clicked.connect(self.switch_to_home)

    def switch_to_home(self):
        self.stacked_widget.setCurrentWidget(self.home_screen)

app = QApplication(sys.argv)
main_app = MainApp()
main_app.show()
sys.exit(app.exec_())

