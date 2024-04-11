import functions as func
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
import os
import sys

class OverlayDialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setStyleSheet("background-color: rgba(100, 100, 100, 150)")
        
        self.label = QtWidgets.QLabel("Transfer in progress - do not close the application", self)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setStyleSheet("color: white; font-size: 20px;")
        
        self.label.setGeometry(0, 0, self.width(), self.height())

class InfoWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Info")
        self.setGeometry(100, 100, 325, 100)
        self.setFixedSize(300,100)

        self.layout = QtWidgets.QVBoxLayout()
        self.setLayout(self.layout)

        self.link1 = QtWidgets.QLabel("This program was created by: <a href='https://nikosav.com/'>nikosav.com</a>" , alignment=QtCore.Qt.AlignCenter)
        self.link1.setOpenExternalLinks(True)
        self.layout.addWidget(self.link1)

        self.link2 = QtWidgets.QLabel("\n<a href='https://creativecommons.org/licenses/by-nc/4.0/'>License</a>", alignment=QtCore.Qt.AlignCenter)
        self.link2.setOpenExternalLinks(True)
        self.layout.addWidget(self.link2)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(685, 229)
        MainWindow.setFixedSize(685, 229)
        icon = QtGui.QIcon("icon.png")
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.filter_standard_button = QtWidgets.QPushButton(self.centralwidget)
        self.filter_standard_button.setGeometry(QtCore.QRect(30, 50, 201, 41))
        font = QtGui.QFont()
        font.setFamily("Levenim MT")
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.filter_standard_button.setFont(font)
        self.filter_standard_button.setDefault(False)
        self.filter_standard_button.setFlat(False)
        self.filter_standard_button.setObjectName("filter_standard_button")
        self.filter_vintage_button = QtWidgets.QPushButton(self.centralwidget)
        self.filter_vintage_button.setGeometry(QtCore.QRect(450, 50, 201, 41))
        font = QtGui.QFont()
        font.setFamily("Levenim MT")
        font.setPointSize(13)
        self.filter_vintage_button.setFont(font)
        self.filter_vintage_button.setObjectName("filter_vintage_button")
        self.filter_blackwhite_button = QtWidgets.QPushButton(self.centralwidget)
        self.filter_blackwhite_button.setGeometry(QtCore.QRect(240, 50, 201, 41))
        font = QtGui.QFont()
        font.setFamily("Levenim MT")
        font.setPointSize(13)
        self.filter_blackwhite_button.setFont(font)
        self.filter_blackwhite_button.setObjectName("filter_blackwhite_button")

        font = QtGui.QFont()
        font.setPointSize(10)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 685, 21))
        self.menubar.setObjectName("menubar")
        self.menuMenu = QtWidgets.QMenu(self.menubar)
        self.menuMenu.setToolTipsVisible(True)
        self.menuMenu.setObjectName("menuMenu")
        self.info_action = QtWidgets.QAction(MainWindow)
        self.info_action.setObjectName("info_action")
        self.actionManual = QtWidgets.QAction(MainWindow)
        self.actionManual.setStatusTip("")
        self.actionManual.setWhatsThis("")
        self.actionManual.setIconVisibleInMenu(False)
        self.actionManual.setObjectName("actionManual")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.menuMenu.addAction(self.info_action)
        self.menuMenu.addAction(self.actionManual)
        self.menuMenu.addAction(self.actionExit)
        self.menubar.addAction(self.menuMenu.menuAction())

        self.title_textbox = QtWidgets.QLabel(self.centralwidget)
        self.title_textbox.setGeometry(QtCore.QRect(10, 20, 661, 20))
        self.title_textbox.setText("Choose a filter to install")
        self.title_textbox.setAlignment(Qt.AlignCenter)
        self.title_textbox.setStyleSheet("font-size: 12px;")

        self.status_textbox = QtWidgets.QLabel(self.centralwidget)
        self.status_textbox.setGeometry(QtCore.QRect(10, 120, 661, 20))
        self.status_textbox.setText("Status:")
        self.status_textbox.setAlignment(Qt.AlignCenter)

        self.disclaimer_label = QtWidgets.QLabel(self.centralwidget)
        self.disclaimer_label.setGeometry(QtCore.QRect(0, 160, 685, 20))  # Adjust the y-coordinate as needed
        self.disclaimer_label.setAlignment(QtCore.Qt.AlignCenter)
        self.disclaimer_label.setStyleSheet("color: red;")
        self.disclaimer_label.setText("Disclaimer: while this program is completely safe, note that any damage caused by incorrect file transfer is the user's liability.")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)



    def show_overlay(self):
        self.overlay_dialog = OverlayDialog(MainWindow)
        self.overlay_dialog.setFixedSize(MainWindow.size())
        self.overlay_dialog.show()

    def hide_overlay(self):
        if hasattr(self, 'overlay_dialog'):
            self.overlay_dialog.close()

    def show_info_window(self):
        self.info_window = InfoWindow()
        main_window_rect = MainWindow.frameGeometry()
        info_window_rect = self.info_window.frameGeometry()
        info_window_rect.moveCenter(main_window_rect.center())
        self.info_window.move(info_window_rect.topLeft())
        self.info_window.show()
        
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Campsnap Filter Installer"))
        self.filter_standard_button.setText(_translate("MainWindow", "Standard Filter"))
        self.filter_vintage_button.setText(_translate("MainWindow", "Vintage Filter"))
        self.filter_blackwhite_button.setText(_translate("MainWindow", "Black and White Filter"))
        self.menuMenu.setTitle(_translate("MainWindow", "Menu"))
        self.actionManual.setText(_translate("MainWindow", "Manual"))
        self.actionManual.setToolTip(_translate("MainWindow", "Open the user manual for the campsnap camera"))
        self.info_action.setText(_translate("MainWindow", "Info"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))



# Initialize the triggers for UI items
def initialize_triggers():
    print("Triggers initialized!")
    ui.actionExit.triggered.connect(MainWindow.close)
    ui.actionManual.triggered.connect(open_manual)
    ui.info_action.triggered.connect(ui.show_info_window)
    # Connect buttons to new_filter function with corresponding filter names
    ui.filter_standard_button.clicked.connect(lambda: process_filter(ui, "standard-filter"))
    ui.filter_vintage_button.clicked.connect(lambda: process_filter(ui, "vintage-filter"))
    ui.filter_blackwhite_button.clicked.connect(lambda: process_filter(ui, "black-and-white-filter"))

def process_filter(ui, filter_name):
    ui.show_overlay()  # Show overlay before starting file transfer
    result = func.new_filter(filter_name)
    ui.hide_overlay()  # Hide overlay after file transfer
    if result == False:
        ui.status_textbox.setText("Status: Files already exist on the camera. Please restart the camera.")
    elif result == None:
        ui.status_textbox.setText("Status: Camera not found.")
    else:
        ui.status_textbox.setText("Status: Files Transferred successfully, please restart the camera twice.")
        return
        
# Only works on Windows
def open_manual():
    manual_path = 'CS15Instructions.pdf'
    if os.path.exists(manual_path):
        os.startfile(manual_path) 
        
    else:
        ui.status_textbox.setText("Status: Manual does not exist in folder, check website.")
        print("Could not find manual")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    initialize_triggers()
    sys.exit(app.exec_())
