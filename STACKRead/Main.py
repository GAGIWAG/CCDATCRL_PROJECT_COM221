import datetime
import time
import tkinter 
import customtkinter
import math
from CTkMessagebox import CTkMessagebox
from PIL import Image

def side_panel_switch():
    if (math.floor(title_frame.winfo_x()) == -75):
        protract()
        return
    if (math.floor(title_frame.winfo_x()) == 75):   
        retract()
        return
    
def protract():
    title_frame.place(x=title_frame.winfo_x()+15)
    search_advanceSearch_frame.place(x=title_frame.winfo_x()+15)
    search_library_frame_inner.place(x=(title_frame.winfo_x()+615))

    if math.floor(title_frame.winfo_x()) == 60:
        Main_app.after_cancel(protract)
    else:
        Main_app.after(10,protract)
    
def retract():
    title_frame.place(x=title_frame.winfo_x()-15)
    search_advanceSearch_frame.place(x=title_frame.winfo_x()-15)
    search_library_frame_inner.place(x=(title_frame.winfo_x()+585))

    if  math.floor(title_frame.winfo_x()) == -60:
        Main_app.after_cancel(retract)
        
    else:
        Main_app.after(10,retract)


def show_main_frame_content(text):

    if text == "Home":
        library_frame.pack_forget()
        search_frame.pack_forget()
        lithit_frame.pack_forget()
        add_books_frame.pack_forget()
        home_frame.pack(fill='both', expand=1)
        
        button_home.configure(state="disabled")
        button_lithit.configure(state="normal")
        button_library.configure(state="normal")
        button_search.configure(state="normal")
        button_addbooks.configure(state="normal")
        
        if button_home.cget("state")=="disabled":
            button_home_img_clicked = customtkinter.CTkImage((Image.open("icons\homeclicked.png")),size=(50,50))
            button_home.configure(image=button_home_img_clicked)
            button_lithit_img = customtkinter.CTkImage((Image.open("icons\markbookunclicked.png")),size=(50,50))
            button_lithit.configure(image=button_lithit_img)
            button_library_img = customtkinter.CTkImage((Image.open("icons\libraryunclicked.png")),size=(50,50))
            button_library.configure(image=button_library_img)
            button_search_img = customtkinter.CTkImage((Image.open("icons\searchunclicked.png")),size=(50,50))
            button_search.configure(image=button_search_img)
            button_addbooks_img_clicked = customtkinter.CTkImage((Image.open("icons\disclickedaddbooks.png")),size=(50,50))
            button_addbooks.configure(image=button_addbooks_img_clicked)
        else:
            button_home_img = customtkinter.CTkImage((Image.open("icons\homeunclicked.png")),size=(50,50))
            button_home.configure(image=button_home_img)

        
    if text == "lithit":
        library_frame.pack_forget()
        search_frame.pack_forget()
        home_frame.pack_forget()
        add_books_frame.pack_forget()
        lithit_frame.pack(fill='both', expand=1)
        
        button_home.configure(state="normal")
        button_lithit.configure(state="disabled")
        button_library.configure(state="normal")
        button_search.configure(state="normal")
        button_addbooks.configure(state="normal")
        
        if button_lithit.cget("state")=="disabled":
            button_home_img = customtkinter.CTkImage((Image.open("icons\homeunclicked.png")),size=(50,50))
            button_home.configure(image=button_home_img)
            button_lithit_img_clicked = customtkinter.CTkImage((Image.open("icons\markbookclicked.png")),size=(50,50))
            button_lithit.configure(image=button_lithit_img_clicked)
            button_library_img = customtkinter.CTkImage((Image.open("icons\libraryunclicked.png")),size=(50,50))
            button_library.configure(image=button_library_img)
            button_search_img = customtkinter.CTkImage((Image.open("icons\searchunclicked.png")),size=(50,50))
            button_search.configure(image=button_search_img)
            button_addbooks_img_clicked = customtkinter.CTkImage((Image.open("icons\disclickedaddbooks.png")),size=(50,50))
            button_addbooks.configure(image=button_addbooks_img_clicked)
        else:
            button_lithit_img = customtkinter.CTkImage((Image.open("icons\markbookunclicked.png")),size=(50,50))
            button_lithit.configure(image=button_lithit_img)
        
    if text == "Search":
        library_frame.pack_forget()
        lithit_frame.pack_forget()
        home_frame.pack_forget()
        add_books_frame.pack_forget()
        search_frame.pack(fill='both', expand=1)
        
        
        button_home.configure(state="normal")
        button_lithit.configure(state="normal")
        button_search.configure(state="disabled")
        button_library.configure(state="normal")
        button_addbooks.configure(state="normal")
        
        if button_search.cget("state")=="disabled":
            button_home_img = customtkinter.CTkImage((Image.open("icons\homeunclicked.png")),size=(50,50))
            button_home.configure(image=button_home_img)
            button_lithit_img = customtkinter.CTkImage((Image.open("icons\markbookunclicked.png")),size=(50,50))
            button_lithit.configure(image=button_lithit_img)
            button_search_img_clicked = customtkinter.CTkImage((Image.open("icons\searchclicked.png")),size=(50,50))
            button_search.configure(image=button_search_img_clicked)
            button_library_img = customtkinter.CTkImage((Image.open("icons\libraryunclicked.png")),size=(50,50))
            button_library.configure(image=button_library_img)
            button_addbooks_img_clicked = customtkinter.CTkImage((Image.open("icons\disclickedaddbooks.png")),size=(50,50))
            button_addbooks.configure(image=button_addbooks_img_clicked)

        else:
            button_search_img = customtkinter.CTkImage((Image.open("icons\searchunclicked.png")),size=(50,50))
            button_search.configure(image=button_search_img)

    if text == "Library":
        search_frame.pack_forget()
        lithit_frame.pack_forget()
        home_frame.pack_forget()
        add_books_frame.pack_forget()
        library_frame.pack(fill='both', expand=1)

        button_home.configure(state="normal")
        button_lithit.configure(state="normal")
        button_search.configure(state="normal")
        button_library.configure(state="disabled")
        button_addbooks.configure(state="normal")
        
        if button_library.cget("state")=="disabled":
            button_home_img = customtkinter.CTkImage((Image.open("icons\homeunclicked.png")),size=(50,50))
            button_home.configure(image=button_home_img)
            button_lithit_img = customtkinter.CTkImage((Image.open("icons\markbookunclicked.png")),size=(50,50))
            button_lithit.configure(image=button_lithit_img)
            button_search_img_ = customtkinter.CTkImage((Image.open("icons\searchunclicked.png")),size=(50,50))
            button_search.configure(image=button_search_img_)
            button_library_img_clicked = customtkinter.CTkImage((Image.open("icons\libraryclicked.png")),size=(50,50))
            button_library.configure(image=button_library_img_clicked)
            button_addbooks_img_clicked = customtkinter.CTkImage((Image.open("icons\disclickedaddbooks.png")),size=(50,50))
            button_addbooks.configure(image=button_addbooks_img_clicked)

        else:
            button_library_img = customtkinter.CTkImage((Image.open("icons\libraryunclicked.png")),size=(50,50))
            button_library.configure(image=button_library_img)

    if text == "Add":
        search_frame.pack_forget()
        lithit_frame.pack_forget()
        home_frame.pack_forget()
        library_frame.pack_forget()
        add_books_frame.pack(fill='both', expand=1)
        
        button_home.configure(state="normal")
        button_lithit.configure(state="normal")
        button_search.configure(state="normal")
        button_library.configure(state="normal")
        button_addbooks.configure(state="disabled")
        
        if button_addbooks.cget("state")=="disabled":
            button_home_img = customtkinter.CTkImage((Image.open("icons\homeunclicked.png")),size=(50,50))
            button_home.configure(image=button_home_img)
            button_lithit_img = customtkinter.CTkImage((Image.open("icons\markbookunclicked.png")),size=(50,50))
            button_lithit.configure(image=button_lithit_img)
            button_search_img_ = customtkinter.CTkImage((Image.open("icons\searchunclicked.png")),size=(50,50))
            button_search.configure(image=button_search_img_)
            button_library_img = customtkinter.CTkImage((Image.open("icons\libraryunclicked.png")),size=(50,50))
            button_library.configure(image=button_library_img)
            button_addbooks_img_clicked = customtkinter.CTkImage((Image.open("icons\clickedaddbooks.png")),size=(50,50))
            button_addbooks.configure(image=button_addbooks_img_clicked)

        else:
            button_addbooks_img = customtkinter.CTkImage((Image.open("icons\disclickedaddbooks.png")),size=(50,50))
            button_addbooks.configure(image=button_addbooks_img)
    # else:
    #     search_frame.pack_forget()
    #     lithit_frame.pack_forget()
    #     home_frame.pack_forget()
    #     add_books_frame.pack_forget()
    #     library_frame.pack_forget()
    #     log_in_frame.pack(fill='both', expand=1)    

def log_in_clock():
    
    rtc = datetime.datetime.now()
    if (rtc.hour < 12):
        if (rtc.hour == 12):
            hr_min_time = "{:02d}:{:02d} AM".format(rtc.hour+12,rtc.minute)
        else:
            hr_min_time = "{:02d}:{:02d} AM".format(rtc.hour,rtc.minute)
    else:
        hr_min_time = "{:02d}:{:02d} PM".format(rtc.hour-12,rtc.minute)
    login_clock_label.configure(text=hr_min_time)
    Main_app.after(1000,log_in_clock)

def login_checker():
    log_in_frame.pack_forget()

def login():
    sign_in_frame.pack_forget() 
    log_in_frame.pack(fill='both', expand=1)    

def sign_in():
    log_in_frame.pack_forget()
    sign_in_frame.pack(fill='both', expand=1)    

def acc_reg_success():
    msg = CTkMessagebox(title="Account Registered", message="Account Registered!",icon="check", option_1="Clock-In")
    response = msg.get()
    
    if response=="Clock-In":
        login()       

customtkinter.set_appearance_mode("light")
customtkinter.set_default_color_theme("blue")

# Main Window
Main_app  = customtkinter.CTk()
Main_app.title("STACKRead")
# Main_app.iconbitmap(Image.open('icons\stackreadicon.png'))

# Get the screen dimensions
screen_width = 1600
screen_height = 900

# Calculate the desired window size as a fraction of the screen dimensions
window_width = 1360  # Adjust the fraction as needed
window_height = 765  # Adjust the fraction as needed

print(window_width)
print(window_height)

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
lithit_frame = customtkinter.CTkFrame(main_content_frame,width=Main_app.winfo_screenwidth(),height=Main_app.winfo_screenheight(),fg_color="#F2E8BD")
search_frame = customtkinter.CTkFrame(main_content_frame,width=Main_app.winfo_screenwidth(),height=Main_app.winfo_screenheight(),fg_color="#F2E8BD")
library_frame = customtkinter.CTkFrame(main_content_frame,width=Main_app.winfo_screenwidth(),height=Main_app.winfo_screenheight(),fg_color="#F2E8BD")
add_books_frame = customtkinter.CTkFrame(main_content_frame,width=Main_app.winfo_screenwidth(),height=Main_app.winfo_screenheight(),fg_color="#F2E8BD")

# Side bar Frames
title_frame = customtkinter.CTkFrame(Main_app,width=150,height=Main_app.winfo_screenheight(),fg_color="#CCD5AE",corner_radius=0,border_width=1,border_color="#CCD5AE")
title_frame.place(x = -75, y = 0)

icon_frame = customtkinter.CTkFrame(Main_app,width=76,height=Main_app.winfo_screenheight(),fg_color="#CCD5AE",corner_radius=0,border_width=1,border_color="#CCD5AE")
icon_frame.place(x = 0, y = 0)

# Credential Frames
sign_in_frame = customtkinter.CTkFrame(Main_app,width=Main_app.winfo_screenwidth(),height=Main_app.winfo_screenheight(),fg_color="#F2E8BD")

log_in_frame = customtkinter.CTkFrame(Main_app,width=Main_app.winfo_screenwidth(),height=Main_app.winfo_screenheight(),fg_color="#F2E8BD")
log_in_frame.pack(fill='both', expand=1)    

# Sign in frame
sign_in_label_img = customtkinter.CTkImage(Image.open('icons\stackreadicon.png'),size=(75,75))
sign_in_label = customtkinter.CTkLabel(sign_in_frame,text="",image=sign_in_label_img,fg_color="transparent")
sign_in_label.place(x=390,y=100)

sign_in_icon_stack_label_img = customtkinter.CTkImage(Image.open('icons\logo.png'),size=(475,75))
sign_in_icon_stack_label = customtkinter.CTkLabel(sign_in_frame,image=sign_in_icon_stack_label_img,anchor="w",text="",fg_color="transparent",font=("Quando",25))
sign_in_icon_stack_label.place(x=470,y=100)

sign_in_icon_quote_label = customtkinter.CTkLabel(sign_in_frame,anchor="w",text="Your digital book wiki.",fg_color="transparent",font=("Quando",25))
sign_in_icon_quote_label.place(x=640,y=180)

sign_in_credentials_frame = customtkinter.CTkFrame(sign_in_frame,fg_color="#1E1E1E",corner_radius=25,width=725,height=425)
sign_in_credentials_frame.place(x=310,y=220)

sign_in_acc_reg_label = customtkinter.CTkLabel(sign_in_credentials_frame,anchor="center",text_color="white",text="Account Registration",fg_color="transparent",font=("Quando",45))
sign_in_acc_reg_label.place(x=110,y=30)

sign_in_username_entry = customtkinter.CTkEntry(sign_in_credentials_frame,fg_color="white",placeholder_text="Username",font=("Quando",25),corner_radius=25,width=630,height=50)
sign_in_username_entry.place(x=50,y=100)

sign_in_email_entry = customtkinter.CTkEntry(sign_in_credentials_frame,width=630,height=50,fg_color="white",placeholder_text="Email",corner_radius=25,font=("Quando",25))
sign_in_email_entry.place(x=50,y=160)

sign_in_password_entry = customtkinter.CTkEntry(sign_in_credentials_frame,width=630,height=50,fg_color="white",placeholder_text="Password",corner_radius=25,show="*",font=("Quando",25))
sign_in_password_entry.place(x=50,y=220)

sign_in_chkbox = customtkinter.CTkCheckBox(sign_in_credentials_frame,text_color="white",width=170,height=50,text="I have read and understood the terms and conditions",font=("Quando",15))
sign_in_chkbox.place(x=150,y=270)

sign_in_button = customtkinter.CTkButton(sign_in_credentials_frame,command=lambda: acc_reg_success(),text="Register",width=230,height=50,fg_color="#C8DF8C",corner_radius=25,text_color="black",font=("Quando",25))
sign_in_button.place(x=250,y=340)

sign_in_already_have_an_account_label = customtkinter.CTkLabel(sign_in_frame,anchor="w",text_color="black",text="Already have an account?",fg_color="transparent",font=("Quando",20))
sign_in_already_have_an_account_label.place(x=410,y=655)

clock_in_button = customtkinter.CTkButton(sign_in_frame,command=lambda: login(),text="Clock-In",width=150,height=25,fg_color="#606060",corner_radius=25,text_color="white",font=("Quando",20))
clock_in_button.place(x=700,y=655)

# Log in Frame Content
login_icon_label_img = customtkinter.CTkImage(Image.open('icons\stackreadicon.png'),size=(75,75))
login_icon_label = customtkinter.CTkLabel(log_in_frame,text="",image=login_icon_label_img,fg_color="transparent")
login_icon_label.place(x=390,y=100)

login_icon_stack_label_img = customtkinter.CTkImage(Image.open('icons\logo.png'),size=(475,75))
login_icon_stack_label = customtkinter.CTkLabel(log_in_frame,image=login_icon_stack_label_img,anchor="w",text="",fg_color="transparent",font=("Quando",25))
login_icon_stack_label.place(x=470,y=100)

login_icon_quote_label = customtkinter.CTkLabel(log_in_frame,anchor="w",text="Your digital book wiki.",fg_color="transparent",font=("Quando",25))
login_icon_quote_label.place(x=640,y=180)

login_credentials_frame = customtkinter.CTkFrame(log_in_frame,fg_color="#B88B68",corner_radius=25,width=725,height=525)
login_credentials_frame.place(x=310,y=220)

login_username_entry = customtkinter.CTkEntry(login_credentials_frame,fg_color="white",placeholder_text="Username",font=("Quando",25),corner_radius=25,width=630,height=50)
login_username_entry.place(x=50,y=40)

login_password_entry = customtkinter.CTkEntry(login_credentials_frame,width=630,height=50,fg_color="white",placeholder_text="Password",corner_radius=25,show="*",font=("Quando",25))
login_password_entry.place(x=50,y=100)

login_button = customtkinter.CTkButton(login_credentials_frame,command=lambda: login_checker(),text="Clock-in",width=230,height=50,fg_color="#C8DF8C",corner_radius=25,text_color="black",font=("Quando",25))
login_button.place(x=250,y=170)

login_clock_frame = customtkinter.CTkFrame(log_in_frame,width=825,height=325,fg_color="#D9D9D9",corner_radius=25)
login_clock_frame.place(x=260,y=470)

login_clock_label = customtkinter.CTkLabel(login_clock_frame,text="12:00 AM",width=725,height=195,text_color="white",fg_color="#292D32",corner_radius=25,font=("Quando",65))
login_clock_label.place(x=50,y=50)

login_no_account_label = customtkinter.CTkLabel(login_clock_frame,text="Don't have an account?",width=150,height=25,fg_color="transparent",text_color="black",corner_radius=25,font=("Quando",20))
login_no_account_label.place(x=140,y=255)

login_register_button = customtkinter.CTkButton(login_clock_frame,text="Register",command=sign_in,corner_radius=450,width=150,height=25,fg_color="#9A9A9A",text_color="black",font=("Quando",20))
login_register_button.place(x=440,y=255)
log_in_clock()

# Main Content Frames

# Home Content
home_search_entry_frame = customtkinter.CTkFrame(home_frame,width=650,height=50,fg_color="transparent",corner_radius=45)
home_search_entry_frame.place(x = (window_width/2)-325, y = 20)

home_search_entry = customtkinter.CTkEntry(home_search_entry_frame,width=550,height=50,fg_color="white",corner_radius=45,placeholder_text="Search Titles...",font=("Quando",20))
home_search_entry.place(x = 0,y=0)

home_search_entry_button_img = customtkinter.CTkImage((Image.open("icons\searchicon.png")),size=(25,25))
home_search_entry_button = customtkinter.CTkButton(home_search_entry_frame,text="",image=home_search_entry_button_img,width=46,height=46,fg_color="transparent",corner_radius=45,border_color="white",hover_color="#CCD5AE")
home_search_entry_button.place(x=550,y=2)

home_top_shelf_frame_outer = customtkinter.CTkFrame(home_frame,width=750,height=150,fg_color="#B88B68",corner_radius=0)
home_top_shelf_frame_outer.place(x = 270, y = 100)

home_top_shelf_frame_inner = customtkinter.CTkFrame(home_top_shelf_frame_outer,width=730,height=130,fg_color="#614D40",corner_radius=0)
home_top_shelf_frame_inner.place(x = 10, y = 10)

home_top_shelf_image_frame = customtkinter.CTkFrame(home_top_shelf_frame_inner,width=100,height=126,fg_color="#B88B68",corner_radius=0)
home_top_shelf_image_frame.place(x = 121, y = 2)

home_top_shelf_image_label = customtkinter.CTkLabel(home_top_shelf_image_frame,corner_radius=0,text="Image Goes Here")
home_top_shelf_image_label.place(x = 0, y = 50)

home_top_shelf_title_label = customtkinter.CTkLabel(home_top_shelf_frame_inner,anchor=customtkinter.W,font=("Quando",20),text_color="white",width=350,height=35,fg_color="transparent",corner_radius=0,text="Title Goes Here")
home_top_shelf_title_label.place(x = 225, y = 10)

home_top_shelf_author_label = customtkinter.CTkLabel(home_top_shelf_frame_inner,anchor=customtkinter.W,font=("Quando",20),text_color="white",width=350,height=35,fg_color="transparent",corner_radius=0,text="Author Goes Here")
home_top_shelf_author_label.place(x = 225, y = 40)

home_top_shelf_previous_button = customtkinter.CTkButton(home_top_shelf_frame_inner,width=35,height=35,font=("Quando",20),fg_color="transparent",corner_radius=0,text="<",text_color="white")
home_top_shelf_previous_button.place(x = 660, y = 95)

home_top_shelf_next_button = customtkinter.CTkButton(home_top_shelf_frame_inner,width=35,height=35,font=("Quando",20),fg_color="transparent",corner_radius=0,text=">",text_color="white")
home_top_shelf_next_button.place(x = 695, y = 95)

home_top_shelf_text_label_img = customtkinter.CTkImage((Image.open("icons\shelftoptext.png")),size=(50,50))
home_top_shelf_text_label = customtkinter.CTkLabel(home_frame,image=home_top_shelf_text_label_img,width=25,height=25,corner_radius=0,text="")
home_top_shelf_text_label.place(x = 295, y = 75)

home_lithit_frame_outer = customtkinter.CTkFrame(home_frame,width=405,height=510,fg_color="transparent",corner_radius=0)
home_lithit_frame_outer.place(x = (window_width/2)-425, y = 260)

home_lithit_frame_inner = customtkinter.CTkFrame(home_lithit_frame_outer,width=355,height=470,fg_color="#B88B68",corner_radius=0)
home_lithit_frame_inner.place(x = 10, y = 40)

home_lithit_button = customtkinter.CTkButton(home_lithit_frame_outer,width=150,height=30,font=("Quando",20),fg_color="#737373",corner_radius=0,text="Literary Hits")
home_lithit_button.place(x = 10, y = 10)

home_lastread_frame_outer = customtkinter.CTkFrame(home_frame,width=405,height=510,fg_color="transparent",corner_radius=0)
home_lastread_frame_outer.place(x = (window_width/2)-20, y = 260)

home_lastread_frame_inner = customtkinter.CTkFrame(home_lastread_frame_outer,width=355,height=470,fg_color="#B88B68",corner_radius=0)
home_lastread_frame_inner.place(x = 10, y = 40)

home_lastread_button = customtkinter.CTkButton(home_lastread_frame_outer,width=150,height=30,font=("Quando",20),fg_color="#737373",corner_radius=0,text="Last Read")
home_lastread_button.place(x = 10, y = 10)

# lithit Content
label_title_lithit = customtkinter.CTkLabel(lithit_frame, text="Literary Hits",width=lithit_frame.winfo_width(),height=50,font=("Quando",50),fg_color="transparent",text_color="black")
label_title_lithit.place(x=(window_width/2)-125,y=0)

# Search Content
search_advanceSearch_frame = customtkinter.CTkFrame(search_frame,width=600,height=765,fg_color="#433F3D",corner_radius=0)
search_advanceSearch_frame.place(x = 0, y = 0)

search_library_frame_inner = customtkinter.CTkFrame(search_frame,width=785,height=765,fg_color="#B88B68",corner_radius=0)
search_library_frame_inner.place(x = 600, y = 0)
        
search_advanceSearch_label = customtkinter.CTkLabel(search_advanceSearch_frame, anchor=customtkinter.W, font=("Quando", 25), text_color="white", width=450, height=69, fg_color="transparent", corner_radius=0, text="Advanced Search")
search_advanceSearch_label.place(x=230, y=20)

search_genre_label = customtkinter.CTkLabel(search_advanceSearch_frame, anchor=customtkinter.W, font=("Quando", 20), text_color="white", width=70, height=30, fg_color="transparent", corner_radius=0, text="Genre")
search_genre_label.place(x=120, y=100)
        
search_genre_entry = customtkinter.CTkEntry(search_advanceSearch_frame,width=200,height=30,fg_color="white",corner_radius=0,placeholder_text="",font=("Quando",20))
search_genre_entry.place(x = 400,y = 100)

search_author_label = customtkinter.CTkLabel(search_advanceSearch_frame, anchor=customtkinter.W, font=("Quando", 20), text_color="white", width=70, height=30, fg_color="transparent", corner_radius=0, text="Author")
search_author_label.place(x=120, y=150)
        
search_author_entry = customtkinter.CTkEntry(search_advanceSearch_frame,width=200,height=30,fg_color="white",corner_radius=0,placeholder_text="",font=("Quando",20))
search_author_entry.place(x = 400,y = 150)

search_theme_label = customtkinter.CTkLabel(search_advanceSearch_frame, anchor=customtkinter.W, font=("Quando", 20), text_color="white", width=70, height=30, fg_color="transparent", corner_radius=0, text="theme")
search_theme_label.place(x=120, y=200)
        
search_theme_entry = customtkinter.CTkEntry(search_advanceSearch_frame,width=200,height=30,fg_color="white",corner_radius=0,placeholder_text="",font=("Quando",20))
search_theme_entry.place(x = 400,y = 200)

search_rating_label = customtkinter.CTkLabel(search_advanceSearch_frame, anchor=customtkinter.W, font=("Quando",20), text_color="white", width=70, height=30, fg_color="transparent", corner_radius=0, text="Rating")
search_rating_label.place(x=120, y=200)
        
search_rating_entry = customtkinter.CTkEntry(search_advanceSearch_frame,width=200,height=30,fg_color="white",corner_radius=0,placeholder_text="",font=("Quando",20))
search_rating_entry.place(x = 400,y = 200)

search_rating_label = customtkinter.CTkLabel(search_advanceSearch_frame, anchor=customtkinter.W, font=("Quando", 20), text_color="white", width=70, height=30, fg_color="transparent", corner_radius=0, text="Rating")
search_rating_label.place(x=120, y=250)
        
search_rating_entry = customtkinter.CTkEntry(search_advanceSearch_frame,width=200,height=30,fg_color="white",corner_radius=0,placeholder_text="",font=("Quando",20))
search_rating_entry.place(x = 400,y = 250)

search_keyword_label = customtkinter.CTkLabel(search_advanceSearch_frame, anchor=customtkinter.W, font=("Quando", 20), text_color="white", width=70, height=30, fg_color="transparent", corner_radius=0, text="Keywords")
search_keyword_label.place(x=120, y=300)
        
search_keyword_entry = customtkinter.CTkEntry(search_advanceSearch_frame,width=200,height=30,fg_color="white",corner_radius=0,placeholder_text="",font=("Quando",20))
search_keyword_entry.place(x = 400,y = 300)

search_award_label = customtkinter.CTkLabel(search_advanceSearch_frame, anchor=customtkinter.W, font=("Quando", 20), text_color="white", width=70, height=30, fg_color="transparent", corner_radius=0, text="Award")
search_award_label.place(x=120, y=350)
        
search_award_entry = customtkinter.CTkEntry(search_advanceSearch_frame,width=200,height=30,fg_color="white",corner_radius=0,placeholder_text="",font=("Quando",20))
search_award_entry.place(x = 400,y = 350)

search_publishDate_label = customtkinter.CTkLabel(search_advanceSearch_frame, anchor=customtkinter.W, font=("Quando",20), text_color="white", width=70, height=30, fg_color="transparent", corner_radius=0, text="Publish Date")
search_publishDate_label.place(x=120, y=400)
        
search_publishDate_entry = customtkinter.CTkEntry(search_advanceSearch_frame,width=200,height=30,fg_color="white",corner_radius=0,placeholder_text="",font=("Quando",20))
search_publishDate_entry.place(x = 400,y = 400)

search_resetFilter_button = customtkinter.CTkButton(search_advanceSearch_frame,width=150,height=40,font=("Quando",20),fg_color="#737373",corner_radius=60,text="Last Read")
search_resetFilter_button.place(x = 250, y = 450)   

search_search_button = customtkinter.CTkButton(search_advanceSearch_frame,width=150,height=40,font=("Quando",20),fg_color="#737373",corner_radius=60,text="Search")
search_search_button.place(x = 430, y = 450)

# Library Content
label_title_library = customtkinter.CTkLabel(library_frame, text="Library",width=library_frame.winfo_width(),height=50,font=("Quando",50),fg_color="transparent",text_color="black")
label_title_library.place(x=(window_width/2)-125,y=0)

# Addbooks Content
addbooks_upload_cover_frame = customtkinter.CTkFrame(add_books_frame,width=250,height=360,fg_color="#414240",corner_radius=0)
addbooks_upload_cover_frame.place(x=190,y=10)

addbooks_upload_cover_button_img = customtkinter.CTkImage(Image.open('icons\coverbookupload.png'),size=(25,25))
addbooks_upload_cover_button = customtkinter.CTkButton(add_books_frame,image=addbooks_upload_cover_button_img,text_color="black",font=("Quando",15),text="Upload Cover",width=250,height=50,fg_color="#C8C8C8",corner_radius=25)
addbooks_upload_cover_button.place(x=190,y=380)

addbooks_book_detail_input_frame = customtkinter.CTkFrame(add_books_frame,width=750,height=420,fg_color="#808080",corner_radius=0)
addbooks_book_detail_input_frame.place(x=455,y=10)

addbooks_book_detail_input_title_entry = customtkinter.CTkEntry(addbooks_book_detail_input_frame,font=("Quando",25),width=730,height=55,fg_color="#F1F1F1",corner_radius=25,placeholder_text="Input Book Title",placeholder_text_color="gray")
addbooks_book_detail_input_title_entry.place(x=10,y=10)

addbooks_book_detail_input_author_name_entry = customtkinter.CTkEntry(addbooks_book_detail_input_frame,font=("Quando",15),width=520,height=45,fg_color="#F1F1F1",corner_radius=25,placeholder_text="Input Author(s) Name",placeholder_text_color="gray")
addbooks_book_detail_input_author_name_entry.place(x=10,y=75)

addbooks_book_detail_input_publish_date_entry = customtkinter.CTkEntry(addbooks_book_detail_input_frame,font=("Quando",12),width=200,height=45,fg_color="#F1F1F1",corner_radius=25,placeholder_text="Publish Date",placeholder_text_color="gray")
addbooks_book_detail_input_publish_date_entry.place(x=540,y=75)

addbooks_book_detail_input_inner_frame = customtkinter.CTkFrame(addbooks_book_detail_input_frame,width=750,height=290,fg_color="#C8C8C8",corner_radius=0)
addbooks_book_detail_input_inner_frame.place(x=0,y=130)

addbooks_book_detail_input_genre_label = customtkinter.CTkLabel(addbooks_book_detail_input_inner_frame,text="Genre:",font=("Quando",20),width=75,height=55,fg_color="transparent")
addbooks_book_detail_input_genre_label.place(x=10,y=10)

addbooks_book_detail_input_theme_label = customtkinter.CTkLabel(addbooks_book_detail_input_inner_frame,text="Theme:",font=("Quando",20),width=75,height=55,fg_color="transparent")
addbooks_book_detail_input_theme_label.place(x=10,y=65)

addbooks_book_detail_input_keywords_label = customtkinter.CTkLabel(addbooks_book_detail_input_inner_frame,text="Keywords:",font=("Quando",20),width=75,height=55,fg_color="transparent")
addbooks_book_detail_input_keywords_label.place(x=10,y=120)

addbooks_book_detail_input_language_label = customtkinter.CTkLabel(addbooks_book_detail_input_inner_frame,text="Language:",font=("Quando",20),width=75,height=55,fg_color="transparent")
addbooks_book_detail_input_language_label.place(x=10,y=175)

addbooks_book_detail_input_rating_label = customtkinter.CTkLabel(addbooks_book_detail_input_inner_frame,text="Rating:",font=("Quando",20),width=75,height=55,fg_color="transparent")
addbooks_book_detail_input_rating_label.place(x=10,y=235)

addbooks_book_detail_input_genre_entry = customtkinter.CTkEntry(addbooks_book_detail_input_inner_frame,font=("Quando",12),width=600,height=45,fg_color="#F1F1F1",corner_radius=25)
addbooks_book_detail_input_genre_entry.place(x=135,y=10)

addbooks_book_detail_input_theme_entry = customtkinter.CTkEntry(addbooks_book_detail_input_inner_frame,font=("Quando",12),width=600,height=45,fg_color="#F1F1F1",corner_radius=25)
addbooks_book_detail_input_theme_entry.place(x=135,y=65)

addbooks_book_detail_input_keywords_entry = customtkinter.CTkEntry(addbooks_book_detail_input_inner_frame,font=("Quando",12),width=600,height=45,fg_color="#F1F1F1",corner_radius=25)
addbooks_book_detail_input_keywords_entry.place(x=135,y=120)

addbooks_book_detail_input_rating_entry = customtkinter.CTkEntry(addbooks_book_detail_input_inner_frame,font=("Quando",12),width=600,height=45,fg_color="#F1F1F1",corner_radius=25)
addbooks_book_detail_input_rating_entry.place(x=135,y=175)

addbooks_book_detail_rating = customtkinter.StringVar(value="other")

my_rad1 = customtkinter.CTkRadioButton(addbooks_book_detail_input_inner_frame, text="1", value="1", variable=addbooks_book_detail_rating,)
my_rad1.place(x=155,y=245)

my_rad2 = customtkinter.CTkRadioButton(addbooks_book_detail_input_inner_frame, text="2", value="2", variable=addbooks_book_detail_rating,)
my_rad2.place(x=215,y=245)

my_rad3 = customtkinter.CTkRadioButton(addbooks_book_detail_input_inner_frame, text="3", value="3", variable=addbooks_book_detail_rating,)
my_rad3.place(x=265,y=245)

my_rad4 = customtkinter.CTkRadioButton(addbooks_book_detail_input_inner_frame, text="4", value="4", variable=addbooks_book_detail_rating,)
my_rad4.place(x=315,y=245)

my_rad5 = customtkinter.CTkRadioButton(addbooks_book_detail_input_inner_frame, text="5", value="5", variable=addbooks_book_detail_rating,)
my_rad5.place(x=365,y=245)

addbooks_synopsis_frame = customtkinter.CTkFrame(add_books_frame,width=1015,height=450,fg_color="#808080",corner_radius=0)
addbooks_synopsis_frame.place(x=190,y=445)

addbooks_synopsis_frame_label = customtkinter.CTkLabel(addbooks_synopsis_frame,anchor="w",text="Synopsis",width=1015,height=75,fg_color="transparent",corner_radius=0,text_color="white",font=("Quando",35))
addbooks_synopsis_frame_label.place(x=20,y=0)

addbooks_synopsis_textbox = customtkinter.CTkTextbox(addbooks_synopsis_frame,width=1015,height=235,fg_color="#D9D9D9",corner_radius=0,font=("Quando",25))
addbooks_synopsis_textbox.place(x=0,y=85)

# Title and Icon Frame Content
button_stackread_img = customtkinter.CTkImage((Image.open("icons\stackreadicon.png")),size=(50,50))
button_stackread = customtkinter.CTkButton(icon_frame,image=button_stackread_img,text="",width=75,height=75,command=side_panel_switch,corner_radius=0,fg_color="#CCD5AE",hover_color="#737373")
button_stackread.place(x = 0, y = 0)

label_title_img = customtkinter.CTkImage(Image.open('icons\logo.png'),size=(145,20))
label_title = customtkinter.CTkLabel(title_frame,image=label_title_img,anchor=customtkinter.W, text="",width=150,height=75,font=("Quando",20),fg_color="transparent",text_color="black")
label_title.place(x = 0, y = 0)

# Buttons for sidebar
button_home_img = customtkinter.CTkImage((Image.open("icons\homeunclicked.png")),size=(50,50))
button_home = customtkinter.CTkButton(icon_frame, image=button_home_img,text="", command=lambda: show_main_frame_content("Home"),width=75,height=75,corner_radius=0,fg_color="#CCD5AE",hover=False)
button_home.place(x = 0 , y = 100)

button_lithit_img = customtkinter.CTkImage((Image.open("icons\markbookunclicked.png")),size=(50,50))
button_lithit = customtkinter.CTkButton(icon_frame,image=button_lithit_img, text="", command=lambda: show_main_frame_content("lithit"),width=75,height=75,corner_radius=0,font=("Quando",16),fg_color="#CCD5AE",hover=False)
button_lithit.place(x = 0 , y = 200)

button_search_img = customtkinter.CTkImage((Image.open("icons\searchunclicked.png")),size=(50,50))
button_search = customtkinter.CTkButton(icon_frame,image=button_search_img, text="", command=lambda: show_main_frame_content("Search"),width=75,height=75,corner_radius=0,font=("Quando",16),fg_color="#CCD5AE",hover=False)
button_search.place(x = 0 , y = 300)

button_library_img = customtkinter.CTkImage((Image.open("icons\libraryunclicked.png")),size=(50,50))
button_library = customtkinter.CTkButton(icon_frame,image=button_library_img, text="", command=lambda: show_main_frame_content("Library"),width=75,height=75,corner_radius=0,font=("Quando",16),fg_color="#CCD5AE",hover=False)
button_library.place(x = 0 , y = 400)

button_addbooks_img= customtkinter.CTkImage((Image.open("icons\disclickedaddbooks.png")),size=(50,50))
button_addbooks = customtkinter.CTkButton(icon_frame,image=button_addbooks_img,text="",command=lambda: show_main_frame_content("Add"),width=75,height=75,corner_radius=0,font=("Quando",16),fg_color="#CCD5AE",hover=False)
button_addbooks.place(x = 0, y = 570)

# button_log_out_img= customtkinter.CTkImage((Image.open("icons\disclickedaddbooks.png")),size=(50,50))
button_log_out = customtkinter.CTkButton(icon_frame,text="<-",command=lambda: login(),width=75,height=75,corner_radius=0,font=("Quando",16),fg_color="#CCD5AE",hover=False,text_color="black")
button_log_out.place(x = 0, y = 650)

# Button Labels for Sidebar
button_label_home = customtkinter.CTkButton(title_frame,anchor="w", text="Home",width=150,height=75,corner_radius=0,fg_color="transparent",font=("Quando",20),text_color="black",hover=False)
button_label_home.place(x = 0 , y = 100)

button_label_lithit = customtkinter.CTkButton(title_frame,anchor="w", text="Literary Hits",width=150,height=75,corner_radius=0,fg_color="transparent",font=("Quando",20),text_color="black",hover=False)
button_label_lithit.place(x = 0 , y = 200)

button_label_search = customtkinter.CTkButton(title_frame,anchor="w", text="Advanced"+"\n"+"Search",width=150,height=75,corner_radius=0,fg_color="transparent",font=("Quando",20),text_color="black",hover=False)
button_label_search.place(x = 0 , y = 300)

button_label_library = customtkinter.CTkButton(title_frame,anchor="w", text="Library",width=150,height=75,corner_radius=0,fg_color="transparent",font=("Quando",20),text_color="black",hover=False)
button_label_library.place(x = 0 , y = 400)

button_label_addbooks = customtkinter.CTkButton(title_frame,anchor="w", text="Add Books",width=150,height=75,corner_radius=0,fg_color="transparent",font=("Quando",20),text_color="black",hover=False)
button_label_addbooks.place(x = 0, y = 570)

# button_label_log_out_img= customtkinter.CTkImage((Image.open("icons\disclickedaddbooks.png")),size=(50,50))
button_label_log_out = customtkinter.CTkButton(title_frame,anchor="w", text="Log Out",width=150,height=75,corner_radius=0,fg_color="transparent",font=("Quando",20),text_color="black",hover=False)
button_label_log_out.place(x = 0, y = 650)

# Main Loop
Main_app.mainloop()