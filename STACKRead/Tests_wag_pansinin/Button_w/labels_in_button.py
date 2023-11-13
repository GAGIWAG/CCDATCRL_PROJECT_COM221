import tkinter as tk

root = tk.Tk()

# Create a new button widget.
button = tk.Button(root, text="Click Me!")

# Create a new label widget and set its parent to the button widget.
label = tk.Label(button, text="This is a label inside a button!")

# Place the label widget inside the button widget using the pack() method.
label.pack()

# Pack the button widget into the main window.
button.pack()

root.mainloop()
