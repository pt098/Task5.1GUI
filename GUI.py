import gpiod
import tkinter as tk

# Set up GPIO lines using chip and request as output
chip = gpiod.Chip('gpiochip4')  # Access the GPIO chip 4 for raspberry Pi 5
red_line = chip.get_line(17)    # Red LED for GPIO 17
green_line = chip.get_line(27)  # Blue LED for GPIO 27
blue_line = chip.get_line(22)   # Green LED for GPIO 22

# Configuring the lines to be output
red_line.request(consumer="led_control", type=gpiod.LINE_REQ_DIR_OUT)
green_line.request(consumer="led_control", type=gpiod.LINE_REQ_DIR_OUT)
blue_line.request(consumer="led_control", type=gpiod.LINE_REQ_DIR_OUT)

# Function to turn off all LEDs
def all_off():
    red_line.set_value(0)
    green_line.set_value(0)
    blue_line.set_value(0)

# Function to control LEDs based on the selected button
def led_control():
    all_off()
    if var.get() == 1:
        red_line.set_value(1)
    elif var.get() == 2:
        green_line.set_value(1)
    elif var.get() == 3:
        blue_line.set_value(1)

# Function to turn off all LEDs and then exit
def exit_program():
    all_off()  # turn off all LEDs before exiting
    root.quit()  # exit the GUI

# Create the GUI window
root = tk.Tk()
root.title("LED Control System")

# Set the window size for GUI (width x height)
root.geometry("300x200")  
# Radio button variable
var = tk.IntVar()

# Create radio buttons
red_radio = tk.Radiobutton(root, text="Red LED", variable=var, value=1, command=led_control)
green_radio = tk.Radiobutton(root, text="Blue LED", variable=var, value=2, command=led_control)
blue_radio = tk.Radiobutton(root, text="Green LED", variable=var, value=3, command=led_control)

# exit button 
exit_button = tk.Button(root, text="Exit", command=exit_program)

# place options in the window
red_radio.pack()
green_radio.pack()
blue_radio.pack()
exit_button.pack()

# Start the Tkinter event loop
root.mainloop()

# Release GPIO lines when the program exits
red_line.release()
green_line.release()
blue_line.release()
