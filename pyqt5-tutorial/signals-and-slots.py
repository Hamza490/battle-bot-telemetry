import sys 
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton

class MainWindow(QMainWindow):
  def __init__(self):
    super().__init__()
    
    #Initialize Variables + App Name
    self.setWindowTitle('My App')
    self.button_is_clicked = True
    button = QPushButton('Press Me!')

    button.setCheckable(True) #Also provides checked variable
    #button.clicked.connect(self.the_button_was_clicked)
    button.clicked.connect(self.the_button_was_toggled)
    button.setChecked(self.button_is_clicked)#Stores value into var passed

    self.setCentralWidget(button)

  def the_button_was_clicked(self):
    print("Clicked")

  def the_button_was_toggled(self, checked):
    self.button_is_clicked = checked
    print("checked?", checked)

#Main Executable
app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
