import time
import serial
from collections import deque
import pyqtgraph as pg
from pyqtgraph.Qt import QtWidgets, QtCore

# Initialize serial connection
ser = serial.Serial('COM8', baudrate=115200, timeout=0.1)
time.sleep(2)  # Allow time for the serial connection to initialize

# Initialize data deque
data_deque = deque([0] * 50, maxlen=50)

# Initialize the Qt Application and the window
app = QtWidgets.QApplication([])
win = pg.GraphicsLayoutWidget(show=True, title="Real-Time Plotting with PyQtGraph")
win.resize(800, 600)
win.setWindowTitle('Arduino Data')

# Create a plot and add it to the window
plot = win.addPlot(title="Real-Time Data from Arduino")
curve = plot.plot(pen='y')

# Set plot parameters
plot.setYRange(0, 5)
plot.setXRange(0, 50)

# Define a function to update the plot
def update():
    try:
        # Read a line of data from the serial port
        arduinoData_string = ser.readline().decode('ascii').strip()
        # Convert the data to a float
        arduinoData_float = float(arduinoData_string)
        # Append new data to deque
        data_deque.append(arduinoData_float)
        print(arduinoData_float)  # Print the data for debugging

    except ValueError:
        print(f"Invalid data: {arduinoData_string}")  # Print invalid data for debugging

    # Update the plot
    curve.setData(data_deque)

# Use a QTimer to call the update function at regular intervals
timer = QtCore.QTimer()
timer.timeout.connect(update)
timer.start(1)  # Update every 10 milliseconds

# Start the Qt event loop
if __name__ == '__main__':
    QtWidgets.QApplication.instance().exec_()

# Close the serial connection when done
ser.close()