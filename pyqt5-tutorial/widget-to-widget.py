from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QVBoxLayout, QWidget
import sys

class MainWindow(QMainWindow):
  def __init__(self):
    super().__init__()
    
    self.setWindowTitle("Widget to Widget Connection")

    self.label = QLabel()
    self.input = QLineEdit()
    self.input.textChanged.connect(self.label.setText)

    layout = QVBoxLayout()
    layout.addWidget(self.label)
    layout.addWidget(self.input)

    container = QWidget()
    container.setLayout(layout)

    self.setCentralWidget(container)

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()