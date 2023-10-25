import tkinter
import customtkinter  # <- import the CustomTkinter module
from PIL import Image

def click(text):
    if text == "But1":
        print("But 1 Pressed")
        button_home.configure(state="disabled")
        button2.configure(state="normal")
        if button_home.cget("state") == "disabled":
            disabled_butt1_icon = customtkinter.CTkImage((Image.open("icons\homeclicked.png")),size=(50,50))
            button_home.configure(image=disabled_butt1_icon)
            butt2_icon = customtkinter.CTkImage((Image.open("icons\libraryunclicked.png")),size=(50,50))
            button2.configure(image=butt2_icon)
        else:
            butt1_icon = customtkinter.CTkImage((Image.open("icons\homeunclicked.png")),size=(50,50))
            button_home.configure(image=butt1_icon)
     
    if text == "But2":    
        print("But 2 Pressed")
        button_home.configure(state="normal")
        button2.configure(state="disabled")
        if button2.cget("state") == "disabled":
            disabled_butt2_icon = customtkinter.CTkImage((Image.open("icons\libraryclicked.png")),size=(50,50))
            button2.configure(image=disabled_butt2_icon)
            butt1_icon = customtkinter.CTkImage((Image.open("icons\homeunclicked.png")),size=(50,50))
            button_home.configure(image=butt1_icon)
        else:
            butt2_icon = customtkinter.CTkImage((Image.open("icons\libraryunclicked.png")),size=(50,50))
            button2.configure(image=butt2_icon)

root_tk = tkinter.Tk()  # create the Tk window like you normally do
root_tk.geometry("400x240")
root_tk.title("CustomTkinter Test")

button_home = customtkinter.CTkImage((Image.open("icons\homeunclicked.png")),size=(50,50))
button_home = customtkinter.CTkButton(master=root_tk,text="",image=button_home, corner_radius=10, command=lambda: click("But1"), state="normal",width=25,height=25)
button_home.place(x=50,y=0)

butt2_icon = customtkinter.CTkImage((Image.open("icons\libraryunclicked.png")),size=(50,50))
button2 = customtkinter.CTkButton(master=root_tk,text="",image=butt2_icon, corner_radius=10, command=lambda: click("But2"), state="normal",width=25,height=25)
button2.place(x=50,y=70)

root_tk.mainloop()