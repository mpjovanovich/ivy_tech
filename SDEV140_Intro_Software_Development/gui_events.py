
import PySimpleGUI as sg

def main():
    # Define the layout of the GUI
    layout = [
        [sg.Text("Button Click Event:")],
        [sg.Button("Click Me", key="btnClickMe", enable_events=True)],
        [sg.Text("Key Press Event:")],
        [sg.Input(key="inpKeyPress", enable_events=True)],
        [sg.Text("Item Select Event:")],
        [sg.Combo(["Option 1", "Option 2", "Option 3"], key="cboSelectEvent", enable_events=True)],
        [sg.Button("Exit", key="btnExit")]
    ]

    # Create the window
    window = sg.Window("Event Demo", layout)

    # Event loop
    while True:
        event, values = window.read()

        # Handle button click event
        if event == "btnClickMe":
            sg.popup("Button clicked!")

        # Handle key press event
        elif event == "inpKeyPress":
            sg.popup(f"Key pressed: {values['inpKeyPress']}")

        # Handle item select event
        elif event == "cboSelectEvent":
            sg.popup(f"Item selected: {values['cboSelectEvent']}")

        # Handle window close event
        elif event == sg.WINDOW_CLOSED or event == "btnExit":
            break

    # Close the window
    window.close()

if __name__ == "__main__":
    main()
