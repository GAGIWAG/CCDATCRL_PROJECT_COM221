import tkinter as tk

def on_button_click():
    label_text = button_label.cget("text")
    print(label_text)

# Create the main window
root = tk.Tk()
root.title("Button with Label")
root.geometry("450x450")

# Create a Button widget with the label inside
button = tk.Button(root, command=on_button_click, width=50,height=25)
button.place(x=0,y=0)

button_frame = tk.Frame(button,width=25,height=10)
button_frame.place(x=0,y=0)

# Create a Label widget
button_label = tk.Label(button_frame, text="Label has been Clicked",width=25,height=10,justify="center",anchor="center")
button_label.place(x=0,y=0)

# Start the Tkinter event loop
root.mainloop()
