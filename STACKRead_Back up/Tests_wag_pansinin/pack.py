import tkinter as tk
import customtkinter
from PIL import Image,ImageTk
import os

def button_click(button_text):
    print(f"Button clicked: {button_text}")

# Create the main window
root = tk.Tk()
root.title("Button Click Example")

file_path = os.path.dirname(os.path.realpath(__file__))
# Create three buttons with different text
butt1_img = customtkinter.CTkImage(Image.open("icons\homeunclicked.png"))
button1 = customtkinter.CTkButton(master=root, image=butt1_img,text="")
button2 = tk.Button(root, text="Button 2", command=lambda: button_click("Button 2"))
button3 = tk.Button(root, text="Button 3", command=lambda: button_click("Button 3"))

# Pack the buttons into the window
button1.pack()
button2.pack()
button3.pack()

# Start the Tkinter main loop
root.mainloop()
