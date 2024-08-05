import sys
import serial
from PyQt5 import QtWidgets, QtCore
from ui_mainwindow import Ui_MainWindow

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
  def __init__(self, *args, **kwargs):
    super(MainWindow, self).__init__(*args, **kwargs)
    self.setupUi(self)

    # Initialize PySerial
    self.serial_port = serial.Serial('COM8', baudrate=9600, timeout=1)
    self.timer = QtCore.QTimer(self)
    self.timer.timeout.connect(self.update_plot_data)
    self.timer.start(100)  # Update every 100 ms

  def update_plot_data(self):
    if self.serial_port.in_waiting > 0:
      line = self.serial_port.readline().decode('utf-8').strip()
      data = float(line)  # Assume incoming data is a float
      self.graphWidget.plot([data], clear=True)

if __name__ == "__main__":
  app = QtWidgets.QApplication(sys.argv)
  window = MainWindow()
  window.show()
  sys.exit(app.exec_())