from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow
from PyQt5.QtCore import QSize, Qt
import sys
'''
This code was made to practice creating individual window:
window=QWidget()
window2=QPushButton("Push my buttons :p")
window3=QMainWindow()

#window.show()
#window2.show()
window3.show()
'''

class MainWindow(QMainWindow):
  def __init__(self):
    super().__init__()

    self.setWindowTitle("Battle-Bot Telemetry")
    button = QPushButton("Port")

    self.setCentralWidget(button)

    self.setFixedSize(QSize(1000,800))
app = QApplication(sys.argv)

window = MainWindow()
window.show()
app.exec()