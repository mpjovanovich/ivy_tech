import tkinter as tk

## This function converts from meters to feet.
## It's called by the "convert" button.
def convert():
    try:
        value = float( txt_feet.get() )
        meters = int(0.3048 * value * 10000.0 + 0.5) / 10000.0
        txt_meters.delete( 0, tk.END )
        txt_meters.insert( 0, str(meters) )
    except ValueError:
        pass

## Create the window.
window = tk.Tk()
window.title( "Feet to Meters" )
window.geometry( '350x200' )

## Add a label and text entry control for feet.
lbl_feet = tk.Label( window, text="Feet:" )
lbl_feet.grid( column=0, row=0 )

txt_feet = tk.Entry( window, width=10, state='normal' )
txt_feet.grid( row=0, column=1 )

## Add a label and text entry control for meters.
lbl_meters = tk.Label( window, text="Meters:" )
lbl_meters.grid( row=1, column=0 )

txt_meters = tk.Entry( window, width=10, state='normal' )
txt_meters.grid( row=1, column=1 )

## Add the "convert" button.
btn_convert = tk.Button( window, text="Convert", command=convert )
btn_convert.grid( row=3, column=0 )

## Put in some padding around all of the controls so they're not touching 
## each other.
for child in window.winfo_children(): 
    child.grid_configure(padx=5, pady=5)

## Set the focus on the feet text entry so it's ready to accept input
## when the program starts.
txt_feet.focus()

## "Run" the window.
window.mainloop()

