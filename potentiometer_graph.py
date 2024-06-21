import serial
import time
import matplotlib.pyplot as plt # type: ignore
import matplotlib.animation as animation # type: ignore

def animate(i, dataList, ser):
    arduinoData_string = ser.readline().decode('ascii')# Decode receive Arduino data as a formatted string
    #print(i)                                           # 'i' is a incrementing variable based upon frames = x argument
    try:
        arduinoData_float = float(arduinoData_string)   # Convert to float
        dataList.append(arduinoData_float)              # Add to the list holding the fixed number of points to animate
    except:                                             # Pass if data point is bad                               
        pass
    
    dataList = dataList[-50:]                          # Fix the list size so that the animation plot 'window' is x number of points

    ax.clear()
    ax.plot(dataList)                                   # Plot new data frame
    
    ax.set_ylim([0, 1200])                              # Set Y axis limit of plot
    #ax.set_xlim([1,50])
    ax.set_title("Arduino Data")                        # Set title of figure
    ax.set_ylabel("Voltage (V)")                              # Set title of y axis 
    ax.set_xlabel("Time (s)")

dataList = []                                           # Create empty list variable for later use
                                                        
fig = plt.figure()                                      # Create Matplotlib plots fig is the 'higher level' plot window
ax = fig.add_subplot(111)                               # Add subplot to main fig window

ser = serial.Serial("COM8", 9600)                       # Establish Serial object with COM port and BAUD rate to match Arduino Port/rate
time.sleep(0.0002)                                          # Time delay for Arduino Serial initialization 

                                                        # Matplotlib Animation Fuction that takes takes care of real time plot.
                                                        # Note that 'fargs' parameter is where we pass in our dataList and Serial object. 
ani = animation.FuncAnimation(fig, animate, frames=100, fargs=(dataList, ser), interval=0.000001) 

plt.show()                                              # Keep Matplotlib plot persistent on screen until it is closed
ser.close()
