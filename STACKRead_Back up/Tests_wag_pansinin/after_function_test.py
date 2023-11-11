import math
import tkinter as tk
import customtkinter
from time import time

def side_panel_switch():
    if (math.floor(title_frame.winfo_x()) == -100):
        protract()
        button_collapse.configure(text="<")
        return
    if (math.floor(title_frame.winfo_x()) == 0):   
        retract()
        button_collapse.configure(text=">")
        return
    
def protract():
    title_frame.place(x=title_frame.winfo_x()+10)
    
    if math.floor(title_frame.winfo_x()) == -10:
        print(title_frame.winfo_x())
        Main_app.after_cancel(protract)
    else:
        print("Increasing",title_frame.winfo_x())
        Main_app.after(10,protract)
    
def retract():
    title_frame.place(x=title_frame.winfo_x()-10)
    
    if  math.floor(title_frame.winfo_x()) == -90:
        print(title_frame.winfo_x())
        Main_app.after_cancel(retract)
        
    else:
        print("Decreasing",title_frame.winfo_x())
        Main_app.after(10,retract)


customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

# Main Window
Main_app  = customtkinter.CTk()
Main_app.geometry("700x480")
Main_app.title("App")
Main_app.resizable(0,0)

button_collapse = customtkinter.CTkButton(Main_app, text=">",width=100,height=50, command=side_panel_switch)
button_collapse.place(x = 0, y = 0)

title_frame = customtkinter.CTkFrame(Main_app,width=100,height=480)
title_frame.place(x=-100,y=50)

# Loop
Main_app.mainloop()