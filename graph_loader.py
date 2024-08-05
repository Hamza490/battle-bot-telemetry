import serial
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout
from PyQt5.uic import loadUi
from PyQt5.QtCore import QTimer
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi('graph.ui', self) # Load your Qt Designer .ui file
        self.serial = serial.Serial('COM3', 9600) # Adjust COM port as needed

        # Set up the matplotlib Figure and FigureCanvas
        self.figure, self.ax = plt.subplots()
        self.canvas = FigureCanvas(self.figure)
        layout = QVBoxLayout()
        layout.addWidget(self.canvas)
        self.plotWidget.setLayout(layout)

        self.xdata = []
        self.ydata = []

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_graph)
        self.timer.start(100) # Update the graph every 100 ms

    def update_graph(self):
        if self.serial.in_waiting > 0:
            line = self.serial.readline().decode('utf-8').strip()
            try:
                value = int(line)
                self.xdata.append(len(self.xdata))
                self.ydata.append(value)
                if len(self.xdata) > 100:
                    self.xdata.pop(0)
                    self.ydata.pop(0)
                self.ax.clear()
                self.ax.plot(self.xdata, self.ydata)
                self.canvas.draw()
            except ValueError:
                pass

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())