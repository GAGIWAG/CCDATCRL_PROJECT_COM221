import datetime
import time
import tkinter 
import customtkinter
import math
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

    if text == "Home":
        library_frame.pack_forget()
        search_frame.pack_forget()
        bookmark_frame.pack_forget()
        add_books_frame.pack_forget()
        home_frame.pack(fill='both', expand=1)
        
        button_home.configure(state="disabled")
        button_bookmark.configure(state="normal")
        button_library.configure(state="normal")
        button_search.configure(state="normal")
        button_addbooks.configure(state="normal")
        
        if button_home.cget("state")=="disabled":
            button_home_img_clicked = customtkinter.CTkImage((Image.open("icons\homeclicked.png")),size=(50,50))
            button_home.configure(image=button_home_img_clicked)
            button_bookmark_img = customtkinter.CTkImage((Image.open("icons\markbookunclicked.png")),size=(50,50))
            button_bookmark.configure(image=button_bookmark_img)
            button_library_img = customtkinter.CTkImage((Image.open("icons\libraryunclicked.png")),size=(50,50))
            button_library.configure(image=button_library_img)
            button_search_img = customtkinter.CTkImage((Image.open("icons\searchunclicked.png")),size=(50,50))
            button_search.configure(image=button_search_img)
            button_addbooks_img_clicked = customtkinter.CTkImage((Image.open("icons\disclickedaddbooks.png")),size=(50,50))
            button_addbooks.configure(image=button_addbooks_img_clicked)
        else:
            button_home_img = customtkinter.CTkImage((Image.open("icons\homeunclicked.png")),size=(50,50))
            button_home.configure(image=button_home_img)

        
    if text == "Bookmark":
        library_frame.pack_forget()
        search_frame.pack_forget()
        home_frame.pack_forget()
        add_books_frame.pack_forget()
        bookmark_frame.pack(fill='both', expand=1)
        
        button_home.configure(state="normal")
        button_bookmark.configure(state="disabled")
        button_library.configure(state="normal")
        button_search.configure(state="normal")
        button_addbooks.configure(state="normal")
        
        if button_bookmark.cget("state")=="disabled":
            button_home_img = customtkinter.CTkImage((Image.open("icons\homeunclicked.png")),size=(50,50))
            button_home.configure(image=button_home_img)
            button_bookmark_img_clicked = customtkinter.CTkImage((Image.open("icons\markbookclicked.png")),size=(50,50))
            button_bookmark.configure(image=button_bookmark_img_clicked)
            button_library_img = customtkinter.CTkImage((Image.open("icons\libraryunclicked.png")),size=(50,50))
            button_library.configure(image=button_library_img)
            button_search_img = customtkinter.CTkImage((Image.open("icons\searchunclicked.png")),size=(50,50))
            button_search.configure(image=button_search_img)
            button_addbooks_img_clicked = customtkinter.CTkImage((Image.open("icons\disclickedaddbooks.png")),size=(50,50))
            button_addbooks.configure(image=button_addbooks_img_clicked)
        else:
            button_bookmark_img = customtkinter.CTkImage((Image.open("icons\markbookunclicked.png")),size=(50,50))
            button_bookmark.configure(image=button_bookmark_img)
        
    if text == "Search":
        library_frame.pack_forget()
        bookmark_frame.pack_forget()
        home_frame.pack_forget()
        add_books_frame.pack_forget()
        search_frame.pack(fill='both', expand=1)
        
        
        button_home.configure(state="normal")
        button_bookmark.configure(state="normal")
        button_search.configure(state="disabled")
        button_library.configure(state="normal")
        button_addbooks.configure(state="normal")
        
        if button_search.cget("state")=="disabled":
            button_home_img = customtkinter.CTkImage((Image.open("icons\homeunclicked.png")),size=(50,50))
            button_home.configure(image=button_home_img)
            button_bookmark_img = customtkinter.CTkImage((Image.open("icons\markbookunclicked.png")),size=(50,50))
            button_bookmark.configure(image=button_bookmark_img)
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
        bookmark_frame.pack_forget()
        home_frame.pack_forget()
        add_books_frame.pack_forget()
        library_frame.pack(fill='both', expand=1)

        button_home.configure(state="normal")
        button_bookmark.configure(state="normal")
        button_search.configure(state="normal")
        button_library.configure(state="disabled")
        button_addbooks.configure(state="normal")
        
        if button_library.cget("state")=="disabled":
            button_home_img = customtkinter.CTkImage((Image.open("icons\homeunclicked.png")),size=(50,50))
            button_home.configure(image=button_home_img)
            button_bookmark_img = customtkinter.CTkImage((Image.open("icons\markbookunclicked.png")),size=(50,50))
            button_bookmark.configure(image=button_bookmark_img)
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
        bookmark_frame.pack_forget()
        home_frame.pack_forget()
        library_frame.pack_forget()
        add_books_frame.pack(fill='both', expand=1)
        
        button_home.configure(state="normal")
        button_bookmark.configure(state="normal")
        button_search.configure(state="normal")
        button_library.configure(state="normal")
        button_addbooks.configure(state="disabled")
        
        if button_addbooks.cget("state")=="disabled":
            button_home_img = customtkinter.CTkImage((Image.open("icons\homeunclicked.png")),size=(50,50))
            button_home.configure(image=button_home_img)
            button_bookmark_img = customtkinter.CTkImage((Image.open("icons\markbookunclicked.png")),size=(50,50))
            button_bookmark.configure(image=button_bookmark_img)
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
    #     bookmark_frame.pack_forget()
    #     home_frame.pack_forget()
    #     add_books_frame.pack_forget()
    #     library_frame.pack_forget()
    #     log_in_frame.pack(fill='both', expand=1)    

def log_in_clock():
    
    rtc = datetime.datetime.now()
    if (rtc.hour < 12):
        hr_min_time = "{:02d}:{:02d} AM".format(rtc.hour,rtc.minute)
    else:
        hr_min_time = "{:02d}:{:02d} PM".format(rtc.hour,rtc.minute)
    login_clock_label.configure(text=hr_min_time)
    Main_app.after(1000,log_in_clock)

def login_checker():
    log_in_frame.pack_forget()

customtkinter.set_appearance_mode("light")
customtkinter.set_default_color_theme("blue")

# Main Window
Main_app  = customtkinter.CTk()
Main_app.title("STACKRead")
# Main_app.iconbitmap(Image.open('icons\stackreadicon.png'))

# Get the screen dimensions
screen_width = Main_app.winfo_screenwidth()
screen_height = Main_app.winfo_screenheight()

# Calculate the desired window size as a fraction of the screen dimensions
window_width = int(screen_width * .85)  # Adjust the fraction as needed
window_height = int(screen_height * 0.85)  # Adjust the fraction as needed

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
bookmark_frame = customtkinter.CTkFrame(main_content_frame,width=Main_app.winfo_screenwidth(),height=Main_app.winfo_screenheight(),fg_color="#F2E8BD")
search_frame = customtkinter.CTkFrame(main_content_frame,width=Main_app.winfo_screenwidth(),height=Main_app.winfo_screenheight(),fg_color="#F2E8BD")
library_frame = customtkinter.CTkFrame(main_content_frame,width=Main_app.winfo_screenwidth(),height=Main_app.winfo_screenheight(),fg_color="#F2E8BD")
add_books_frame = customtkinter.CTkFrame(main_content_frame,width=Main_app.winfo_screenwidth(),height=Main_app.winfo_screenheight(),fg_color="#F2E8BD")

# Side bar Frames
title_frame = customtkinter.CTkFrame(Main_app,width=150,height=Main_app.winfo_screenheight(),fg_color="#CCD5AE",corner_radius=0)
title_frame.place(x = -75, y = 0)

icon_frame = customtkinter.CTkFrame(Main_app,width=75,height=Main_app.winfo_screenheight(),fg_color="#CCD5AE",corner_radius=0,border_width=0)
icon_frame.place(x = 0, y = 0)

log_in_frame = customtkinter.CTkFrame(Main_app,width=Main_app.winfo_screenwidth(),height=Main_app.winfo_screenheight(),fg_color="#F2E8BD")
log_in_frame.pack(fill='both', expand=1)    

# Log in Frame Content
login_icon_label_img = customtkinter.CTkImage(Image.open('icons\stackreadicon.png'),size=(75,75))
login_icon_label = customtkinter.CTkLabel(log_in_frame,text="",image=login_icon_label_img,fg_color="transparent")
login_icon_label.place(x=380,y=100)

login_icon_stack_label_img = customtkinter.CTkImage(Image.open('icons\logo.png'),size=(475,75))
login_icon_stack_label = customtkinter.CTkLabel(log_in_frame,image=login_icon_stack_label_img,anchor="w",text="",fg_color="transparent",font=("Quando",25))
login_icon_stack_label.place(x=460,y=100)

login_icon_quote_label = customtkinter.CTkLabel(log_in_frame,anchor="w",text="Your digital book wiki.",fg_color="transparent",font=("Quando",25))
login_icon_quote_label.place(x=630,y=180)

login_credentials_frame = customtkinter.CTkFrame(log_in_frame,fg_color="#B88B68",corner_radius=25,width=725,height=525)
login_credentials_frame.place(x=300,y=220)

login_username_entry = customtkinter.CTkEntry(login_credentials_frame,fg_color="white",placeholder_text="Username",font=("Quando",25),corner_radius=25,width=630,height=50)
login_username_entry.place(x=50,y=40)

login_password_entry = customtkinter.CTkEntry(login_credentials_frame,width=630,height=50,fg_color="white",placeholder_text="Password",corner_radius=25,show="*",font=("Quando",25))
login_password_entry.place(x=50,y=100)

login_button = customtkinter.CTkButton(login_credentials_frame,command=lambda: login_checker(),text="Clock-in",width=230,height=50,fg_color="#C8DF8C",corner_radius=25,text_color="black",font=("Quando",25))
login_button.place(x=250,y=170)

login_clock_frame = customtkinter.CTkFrame(log_in_frame,width=825,height=325,fg_color="#D9D9D9",corner_radius=25)
login_clock_frame.place(x=250,y=470)

login_clock_label = customtkinter.CTkLabel(login_clock_frame,text="12:00 AM",width=725,height=195,text_color="white",fg_color="#292D32",corner_radius=25,font=("Quando",65))
login_clock_label.place(x=50,y=50)

login_no_account_label = customtkinter.CTkLabel(login_clock_frame,text="Don't have an account?",width=150,height=25,fg_color="transparent",text_color="black",corner_radius=25,font=("Quando",20))
login_no_account_label.place(x=140,y=255)

login_register_button = customtkinter.CTkButton(login_clock_frame,text="Register",corner_radius=450,width=150,height=25,fg_color="#9A9A9A",text_color="black",font=("Quando",20))
login_register_button.place(x=440,y=255)
log_in_clock()

# Main Content Frames

# Home Content
home_search_entry_frame = customtkinter.CTkFrame(home_frame,width=650,height=50,fg_color="transparent",corner_radius=45)
home_search_entry_frame.place(x = (window_width/2)-325, y = 20)

home_search_entry = customtkinter.CTkEntry(home_search_entry_frame,width=550,height=50,fg_color="white",corner_radius=45,placeholder_text="Search Titles...",font=("Quando",.00002*(window_width*window_height)))
home_search_entry.place(x = 0,y=0)

home_search_entry_button_img = customtkinter.CTkImage((Image.open("icons\searchicon.png")),size=(25,25))
home_search_entry_button = customtkinter.CTkButton(home_search_entry_frame,text="",image=home_search_entry_button_img,width=46,height=46,fg_color="transparent",corner_radius=45,border_color="white",hover_color="#CCD5AE")
home_search_entry_button.place(x=550,y=2)

home_top_shelf_frame_outer = customtkinter.CTkFrame(home_frame,width=750,height=150,fg_color="#B88B68",corner_radius=0)
home_top_shelf_frame_outer.place(x = (window_width/2)-400, y = 100)

home_top_shelf_frame_inner = customtkinter.CTkFrame(home_top_shelf_frame_outer,width=730,height=130,fg_color="#614D40",corner_radius=0)
home_top_shelf_frame_inner.place(x = 10, y = 10)

home_top_shelf_image_frame = customtkinter.CTkFrame(home_top_shelf_frame_inner,width=100,height=126,fg_color="#B88B68",corner_radius=0)
home_top_shelf_image_frame.place(x = 121, y = 2)

home_top_shelf_image_label = customtkinter.CTkLabel(home_top_shelf_image_frame,corner_radius=0,text="Image Goes Here")
home_top_shelf_image_label.place(x = 0, y = 50)

home_top_shelf_title_label = customtkinter.CTkLabel(home_top_shelf_frame_inner,anchor=customtkinter.W,font=("Quando",.00002*(window_width*window_height)),text_color="white",width=350,height=35,fg_color="transparent",corner_radius=0,text="Title Goes Here")
home_top_shelf_title_label.place(x = 225, y = 10)

home_top_shelf_author_label = customtkinter.CTkLabel(home_top_shelf_frame_inner,anchor=customtkinter.W,font=("Quando",.00002*(window_width*window_height)),text_color="white",width=350,height=35,fg_color="transparent",corner_radius=0,text="Author Goes Here")
home_top_shelf_author_label.place(x = 225, y = 40)

home_top_shelf_text_label_img = customtkinter.CTkImage((Image.open("icons\shelftoptext.png")),size=(50,50))
home_top_shelf_text_label = customtkinter.CTkLabel(home_frame,image=home_top_shelf_text_label_img,width=25,height=25,fg_color="white",corner_radius=0,text="")
home_top_shelf_text_label.place(x = 295, y = 75)

home_top_shelf_previous_button = customtkinter.CTkButton(home_top_shelf_frame_inner,width=35,height=35,font=("Quando",.00002*(window_width*window_height)),fg_color="transparent",corner_radius=0,text="<",text_color="white")
home_top_shelf_previous_button.place(x = 660, y = 95)

home_top_shelf_next_button = customtkinter.CTkButton(home_top_shelf_frame_inner,width=35,height=35,font=("Quando",.00002*(window_width*window_height)),fg_color="transparent",corner_radius=0,text=">",text_color="white")
home_top_shelf_next_button.place(x = 695, y = 95)

home_bookmark_frame_outer = customtkinter.CTkFrame(home_frame,width=405,height=510,fg_color="transparent",corner_radius=0)
home_bookmark_frame_outer.place(x = (window_width/2)-425, y = 260)

home_bookmark_frame_inner = customtkinter.CTkFrame(home_bookmark_frame_outer,width=355,height=470,fg_color="#B88B68",corner_radius=0)
home_bookmark_frame_inner.place(x = 10, y = 40)

home_bookmark_button = customtkinter.CTkButton(home_bookmark_frame_outer,width=150,height=30,font=("Quando",.00002*(window_width*window_height)),fg_color="#737373",corner_radius=0,text="Bookmarks")
home_bookmark_button.place(x = 10, y = 10)

home_lastread_frame_outer = customtkinter.CTkFrame(home_frame,width=405,height=510,fg_color="transparent",corner_radius=0)
home_lastread_frame_outer.place(x = (window_width/2)-20, y = 260)

home_lastread_frame_inner = customtkinter.CTkFrame(home_lastread_frame_outer,width=355,height=470,fg_color="#B88B68",corner_radius=0)
home_lastread_frame_inner.place(x = 10, y = 40)

home_lastread_button = customtkinter.CTkButton(home_lastread_frame_outer,width=150,height=30,font=("Quando",.00002*(window_width*window_height)),fg_color="#737373",corner_radius=0,text="Last Read")
home_lastread_button.place(x = 10, y = 10)

home_bookmark_frame_inner = customtkinter.CTkFrame(home_frame,width=750,height=150,fg_color="#B88B68",corner_radius=0)
home_bookmark_frame_inner.place(x = (window_width/2)-400, y = 100)

# Bookmark Content
label_title_bookmark = customtkinter.CTkLabel(bookmark_frame, text="Bookmark",width=bookmark_frame.winfo_width(),height=50,font=("Quando",50),fg_color="transparent",text_color="black")
label_title_bookmark.place(x=(window_width/2)-125,y=0)

# Search Content
search_advanceSearch_frame = customtkinter.CTkFrame(search_frame,width=700,height=1080,fg_color="#433F3D",corner_radius=0)
search_advanceSearch_frame.place(x = (window_width/2)-710, y = 0)

search_library_frame_inner = customtkinter.CTkFrame(search_frame,width=1509,height=1122,fg_color="#B88B68",corner_radius=0)
search_library_frame_inner.place(x = 600, y = 0)
        
search_advanceSearch_label = customtkinter.CTkLabel(search_advanceSearch_frame, anchor=customtkinter.W, font=("Quando", 20), text_color="white", width=450, height=69, fg_color="transparent", corner_radius=0, text="Advance Search")
search_advanceSearch_label.place(x=230, y=20)

search_genre_label = customtkinter.CTkLabel(search_advanceSearch_frame, anchor=customtkinter.W, font=("Quando", 20), text_color="white", width=70, height=30, fg_color="transparent", corner_radius=0, text="Genre")
search_genre_label.place(x=320, y=100)
        
search_genre_entry = customtkinter.CTkEntry(search_advanceSearch_frame,width=200,height=30,fg_color="white",corner_radius=0,placeholder_text="",font=("Quando",20))
search_genre_entry.place(x = 400,y = 100)

search_author_label = customtkinter.CTkLabel(search_advanceSearch_frame, anchor=customtkinter.W, font=("Quando", 20), text_color="white", width=70, height=30, fg_color="transparent", corner_radius=0, text="Author")
search_author_label.place(x=320, y=150)
        
search_author_entry = customtkinter.CTkEntry(search_advanceSearch_frame,width=200,height=30,fg_color="white",corner_radius=0,placeholder_text="",font=("Quando",20))
search_author_entry.place(x = 400,y = 150)

search_theme_label = customtkinter.CTkLabel(search_advanceSearch_frame, anchor=customtkinter.W, font=("Quando", .00002 * (window_width * window_height)), text_color="white", width=70, height=30, fg_color="transparent", corner_radius=0, text="theme")
search_theme_label.place(x=320, y=200)
        
search_theme_entry = customtkinter.CTkEntry(search_advanceSearch_frame,width=200,height=30,fg_color="white",corner_radius=0,placeholder_text="",font=("Quando",20))
search_theme_entry.place(x = 400,y = 200)

search_rating_label = customtkinter.CTkLabel(search_advanceSearch_frame, anchor=customtkinter.W, font=("Quando",20), text_color="white", width=70, height=30, fg_color="transparent", corner_radius=0, text="Rating")
search_rating_label.place(x=320, y=200)
        
search_rating_entry = customtkinter.CTkEntry(search_advanceSearch_frame,width=200,height=30,fg_color="white",corner_radius=0,placeholder_text="",font=("Quando",20))
search_rating_entry.place(x = 400,y = 200)

search_rating_label = customtkinter.CTkLabel(search_advanceSearch_frame, anchor=customtkinter.W, font=("Quando", 20), text_color="white", width=70, height=30, fg_color="transparent", corner_radius=0, text="Rating")
search_rating_label.place(x=320, y=250)
        
search_rating_entry = customtkinter.CTkEntry(search_advanceSearch_frame,width=200,height=30,fg_color="white",corner_radius=0,placeholder_text="",font=("Quando",20))
search_rating_entry.place(x = 400,y = 250)

search_keyword_label = customtkinter.CTkLabel(search_advanceSearch_frame, anchor=customtkinter.W, font=("Quando", 20), text_color="white", width=70, height=30, fg_color="transparent", corner_radius=0, text="Keywords")
search_keyword_label.place(x=300, y=300)
        
search_keyword_entry = customtkinter.CTkEntry(search_advanceSearch_frame,width=200,height=30,fg_color="white",corner_radius=0,placeholder_text="",font=("Quando",20))
search_keyword_entry.place(x = 400,y = 300)

search_award_label = customtkinter.CTkLabel(search_advanceSearch_frame, anchor=customtkinter.W, font=("Quando", 20), text_color="white", width=70, height=30, fg_color="transparent", corner_radius=0, text="Award")
search_award_label.place(x=320, y=350)
        
search_award_entry = customtkinter.CTkEntry(search_advanceSearch_frame,width=200,height=30,fg_color="white",corner_radius=0,placeholder_text="",font=("Quando",20))
search_award_entry.place(x = 400,y = 350)

search_publishDate_label = customtkinter.CTkLabel(search_advanceSearch_frame, anchor=customtkinter.W, font=("Quando",20), text_color="white", width=70, height=30, fg_color="transparent", corner_radius=0, text="Publish Date")
search_publishDate_label.place(x=260, y=400)
        
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
label_title_addbooks = customtkinter.CTkLabel(add_books_frame, text="Add Books",width=library_frame.winfo_width(),height=50,font=("Quando",50),fg_color="transparent",text_color="black")
label_title_addbooks.place(x=(window_width/2)-125,y=0)



# Title and Icon Frame Content
button_stackread_img = customtkinter.CTkImage((Image.open("icons\stackreadicon.png")),size=(50,50))
button_stackread = customtkinter.CTkButton(icon_frame,image=button_stackread_img,text="",width=75,height=75,command=side_panel_switch,corner_radius=0,fg_color="#CCD5AE",hover_color="#fefae0")
button_stackread.place(x = 0, y = 0)

label_title = customtkinter.CTkLabel(title_frame,anchor=customtkinter.W, text="STACKRead",width=150,height=75,font=("Quando",20),fg_color="transparent",text_color="black")
label_title.place(x = 0, y = 0)

# Buttons for sidebar
button_home_img = customtkinter.CTkImage((Image.open("icons\homeunclicked.png")),size=(50,50))
button_home = customtkinter.CTkButton(icon_frame, image=button_home_img,text="", command=lambda: show_main_frame_content("Home"),width=75,height=75,corner_radius=0,fg_color="#CCD5AE",hover=False)
button_home.place(x = 0 , y = 100)

button_bookmark_img = customtkinter.CTkImage((Image.open("icons\markbookunclicked.png")),size=(50,50))
button_bookmark = customtkinter.CTkButton(icon_frame,image=button_bookmark_img, text="", command=lambda: show_main_frame_content("Bookmark"),width=75,height=75,corner_radius=0,font=("Quando",16),fg_color="#CCD5AE",hover=False)
button_bookmark.place(x = 0 , y = 200)

button_search_img = customtkinter.CTkImage((Image.open("icons\searchunclicked.png")),size=(50,50))
button_search = customtkinter.CTkButton(icon_frame,image=button_search_img, text="", command=lambda: show_main_frame_content("Search"),width=75,height=75,corner_radius=0,font=("Quando",16),fg_color="#CCD5AE",hover=False)
button_search.place(x = 0 , y = 300)

button_library_img = customtkinter.CTkImage((Image.open("icons\libraryunclicked.png")),size=(50,50))
button_library = customtkinter.CTkButton(icon_frame,image=button_library_img, text="", command=lambda: show_main_frame_content("Library"),width=75,height=75,corner_radius=0,font=("Quando",16),fg_color="#CCD5AE",hover=False)
button_library.place(x = 0 , y = 400)

button_addbooks_img= customtkinter.CTkImage((Image.open("icons\disclickedaddbooks.png")),size=(50,50))
button_addbooks = customtkinter.CTkButton(icon_frame,image=button_addbooks_img,text="",command=lambda: show_main_frame_content("Add"),width=75,height=75,corner_radius=0,font=("Quando",16),fg_color="#CCD5AE",hover=False)
button_addbooks.place(x = 0, y = 630)


# Button Labels for Sidebar
button_label_home = customtkinter.CTkButton(title_frame,anchor="w", text="Home",width=150,height=75,corner_radius=0,fg_color="transparent",font=("Quando",20),text_color="black",hover=False)
button_label_home.place(x = 0 , y = 100)

button_label_bookmark = customtkinter.CTkButton(title_frame,anchor="w", text="BookMark",width=150,height=75,corner_radius=0,fg_color="transparent",font=("Quando",20),text_color="black",hover=False)
button_label_bookmark.place(x = 0 , y = 200)

button_label_search = customtkinter.CTkButton(title_frame,anchor="w", text="Advanced\nSearch",width=150,height=75,corner_radius=0,fg_color="transparent",font=("Quando",20),text_color="black",hover=False)
button_label_search.place(x = 0 , y = 300)

button_label_library = customtkinter.CTkButton(title_frame,anchor="w", text="Library",width=150,height=75,corner_radius=0,fg_color="transparent",font=("Quando",20),text_color="black",hover=False)
button_label_library.place(x = 0 , y = 400)

button_label_addbooks = customtkinter.CTkButton(title_frame,anchor="w", text="Add Books",width=150,height=75,corner_radius=0,fg_color="transparent",font=("Quando",20),text_color="black",hover=False)
button_label_addbooks.place(x = 0, y = 630)

# Main Loop
Main_app.mainloop()