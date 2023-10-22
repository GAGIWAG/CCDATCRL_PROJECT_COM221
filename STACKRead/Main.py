import tkinter as tk
import customtkinter
import math
import os
from PIL import ImageTk,Image
from time import time

def side_panel_switch():
    if (math.floor(title_frame.winfo_x()) == -75):
        protract()
        return
    if (math.floor(title_frame.winfo_x()) == 75):   
        retract()
        return
    
 
def protract():
    title_frame.place(x=title_frame.winfo_x()+15)
    
    if math.floor(title_frame.winfo_x()) == 60:
        Main_app.after_cancel(protract)
    else:
        Main_app.after(10,protract)
    
def retract():
    title_frame.place(x=title_frame.winfo_x()-15)
    
    if  math.floor(title_frame.winfo_x()) == -60:
        Main_app.after_cancel(retract)
        
    else:
        Main_app.after(10,retract)

def show_main_frame_content(text):
    print(text)
    if text == "Home":
        library_frame.pack_forget()
        search_frame.pack_forget()
        bookmark_frame.pack_forget()
        home_frame.pack(fill='both', expand=1)
    if text == "Bookmark":
        library_frame.pack_forget()
        search_frame.pack_forget()
        home_frame.pack_forget()
        bookmark_frame.pack(fill='both', expand=1)
    if text == "Search":
        library_frame.pack_forget()
        bookmark_frame.pack_forget()
        home_frame.pack_forget()
        search_frame.pack(fill='both', expand=1)
    if text == "Library":
        search_frame.pack_forget()
        bookmark_frame.pack_forget()
        home_frame.pack_forget()
        library_frame.pack(fill='both', expand=1)

        
customtkinter.set_appearance_mode("light")
customtkinter.set_default_color_theme("blue")

# Main Window
Main_app  = customtkinter.CTk()
Main_app.title("STACKRead")

# Get the screen dimensions
screen_width = Main_app.winfo_screenwidth()
screen_height = Main_app.winfo_screenheight()

# Calculate the desired window size as a fraction of the screen dimensions
window_width = int(screen_width * .9)  # Adjust the fraction as needed
window_height = int(screen_height * 0.85)  # Adjust the fraction as needed

# Set the window size and position it in the center of the screen
x_position = (screen_width - window_width) // 2
y_position = (screen_height - window_height) // 4.5

# Set the window's geometry
Main_app.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")
Main_app.resizable(0,0)

# Main Content Frames
main_content_frame = customtkinter.CTkFrame(Main_app,width=Main_app.winfo_screenwidth(),height=Main_app.winfo_screenheight(),fg_color="#F2E8BD")
main_content_frame.place(x = 50, y = 0)

home_frame = customtkinter.CTkFrame(main_content_frame,width=Main_app.winfo_screenwidth(),height=Main_app.winfo_screenheight(),fg_color="#F2E8BD")
bookmark_frame = customtkinter.CTkFrame(main_content_frame,width=Main_app.winfo_screenwidth(),height=Main_app.winfo_screenheight(),fg_color="#F2E8BD")
search_frame = customtkinter.CTkFrame(main_content_frame,width=Main_app.winfo_screenwidth(),height=Main_app.winfo_screenheight(),fg_color="#F2E8BD")
library_frame = customtkinter.CTkFrame(main_content_frame,width=Main_app.winfo_screenwidth(),height=Main_app.winfo_screenheight(),fg_color="#F2E8BD")

# Side bar Frames
title_frame = customtkinter.CTkFrame(Main_app,width=150,height=Main_app.winfo_screenheight(),fg_color="#CCD5AE",corner_radius=0)
title_frame.place(x = -75, y = 0)

icon_frame = customtkinter.CTkFrame(Main_app,width=76,height=Main_app.winfo_screenheight(),fg_color="#CCD5AE",corner_radius=0)
icon_frame.place(x = 0, y = 0)


# Main Content Frames

# Home Content
label_title_home = customtkinter.CTkLabel(home_frame, text="Home",width=home_frame.winfo_width(),height=50,font=("Quando",50),fg_color="transparent",text_color="black")
label_title_home.place(x=(window_width/2)-125,y=0)

label_title_bookmark = customtkinter.CTkLabel(bookmark_frame, text="Bookmark",width=bookmark_frame.winfo_width(),height=50,font=("Quando",50),fg_color="transparent",text_color="black")
label_title_bookmark.place(x=(window_width/2)-125,y=0)

label_title_search = customtkinter.CTkLabel(search_frame, text="Search",width=search_frame.winfo_width(),height=50,font=("Quando",50),fg_color="transparent",text_color="black")
label_title_search.place(x=(window_width/2)-125,y=0)

label_title_library = customtkinter.CTkLabel(library_frame, text="Library",width=library_frame.winfo_width(),height=50,font=("Quando",50),fg_color="transparent",text_color="black")
label_title_library.place(x=(window_width/2)-125,y=0)


# Title and Icon Frame Content
button_stackread_img = customtkinter.CTkImage((Image.open("icons\stackreadicon.png")),size=(50,50))
button_stackread = customtkinter.CTkButton(icon_frame,image=button_stackread_img,text="",width=75,height=75,command=side_panel_switch,corner_radius=0,fg_color="#CCD5AE")
button_stackread.place(x = 0, y = 0)

label_title = customtkinter.CTkLabel(title_frame, text="STACKRead",width=150,height=75,font=("Quando",.00002*(window_width*window_height)),fg_color="transparent",text_color="black")
label_title.place(x = 0, y = 0)


# Buttons for sidebard
button_home_img = customtkinter.CTkImage((Image.open("icons\homeunclicked.png")),size=(50,50))
button_home = customtkinter.CTkButton(icon_frame, image=button_home_img,text="", command=lambda: show_main_frame_content("Home"),width=75,height=75,corner_radius=0,fg_color="#CCD5AE",hover_color="#fefae0")
button_home.place(x = 0 , y = 75)

button_bookmark_img = customtkinter.CTkImage((Image.open("icons\markbookunclicked.png")),size=(50,50))
button_bookmark = customtkinter.CTkButton(icon_frame,image=button_bookmark_img, text="", command=lambda: show_main_frame_content("Bookmark"),width=75,height=75,corner_radius=0,font=("Quando",16),fg_color="#CCD5AE",hover_color="#fefae0")
button_bookmark.place(x = 0 , y = 150)

button_search_img = customtkinter.CTkImage((Image.open("icons\searchunclicked.png")),size=(50,50))
button_search = customtkinter.CTkButton(icon_frame,image=button_search_img, text="", command=lambda: show_main_frame_content("Search"),width=75,height=75,corner_radius=0,font=("Quando",16),fg_color="#CCD5AE",hover_color="#fefae0")
button_search.place(x = 0 , y = 225)

button_library_img = customtkinter.CTkImage((Image.open("icons\libraryunclicked.png")),size=(50,50))
button_library = customtkinter.CTkButton(icon_frame,image=button_library_img, text="", command=lambda: show_main_frame_content("Library"),width=75,height=75,corner_radius=0,font=("Quando",16),fg_color="#CCD5AE",hover_color="#fefae0")
button_library.place(x = 0 , y = 300)

# button_settings = customtkinter.CTkButton(icon_frame, text="⚙️",width=50,height=50,corner_radius=0,font=("Quando",16),fg_color="#CCD5AE")
# button_settings.place(x = 0, y = 375)


# Button Labels for Sidebar
button_label_home = customtkinter.CTkButton(title_frame, text="Home",command=lambda: show_main_frame_content("Home"),width=150,height=75,corner_radius=0,fg_color="transparent",font=("Quando",.00002*(window_width*window_height)),text_color="black",hover_color="#fefae0")
button_label_home.place(x = 0 , y = 75)

button_label_bookmark = customtkinter.CTkButton(title_frame, text="BookMark", command=lambda: show_main_frame_content("Bookmark"),width=150,height=75,corner_radius=0,fg_color="transparent",font=("Quando",.00002*(window_width*window_height)),text_color="black",hover_color="#fefae0")
button_label_bookmark.place(x = 0 , y = 150)

button_label_search = customtkinter.CTkButton(title_frame, text="Search", command=lambda: show_main_frame_content("Search"),width=150,height=75,corner_radius=0,fg_color="transparent",font=("Quando",.00002*(window_width*window_height)),text_color="black",hover_color="#fefae0")
button_label_search.place(x = 0 , y = 225)


button_label_library = customtkinter.CTkButton(title_frame, text="Library", command=lambda: show_main_frame_content("Library"),width=150,height=75,corner_radius=0,fg_color="transparent",font=("Quando",.00002*(window_width*window_height)),text_color="black",hover_color="#fefae0")
button_label_library.place(x = 0 , y = 300)

# button_label_settings = customtkinter.CTkButton(title_frame, text="Settings",width=100,height=50,corner_radius=0,fg_color="transparent",font=("Quando",16),text_color="black")
# button_label_settings.place(x = 0, y = 430)

# Loop
Main_app.mainloop()