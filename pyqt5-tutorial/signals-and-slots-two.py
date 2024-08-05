import sys 
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton

class MainWindow(QMainWindow):
  def __init__(self):
    super().__init__()
    self.button_is_checked = True
    self.setWindowTitle('My App')
    
    self.button = QPushButton('Press Me!')
    self.button.clicked.connect(self.the_button_was_clicked)

    self.setCentralWidget(self.button)

  def the_button_was_clicked(self):
    self.button.setText("You already clicked me.")
    self.button.setEnabled(False)
    self.setWindowTitle('My Oneshot App')


#Main Executable
app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
