
# Import the PySimpleGUI library so that we can use it with the alias 'sg'
import PySimpleGUI as sg

# Define the layout of the GUI
layout = [[sg.Button('Click Me')]]

# Create the window
window = sg.Window('My GUI', layout)

# Event loop to process events and get user input
while True:
    event, values = window.read()
    
    # If the user closes the window, exit the program
    if event == sg.WINDOW_CLOSED:
        break
    
    # If the button is clicked, display a message
    if event == 'Click Me':
        sg.popup('Button clicked!')

# Close the window
window.close()
