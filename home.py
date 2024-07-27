import customtkinter
from tkinter import *
from PIL import Image, ImageTk
from cadastro_processo import *

def pg_home():

    home=customtkinter.CTk()
    home.title("Home") 
    screen_width = home.winfo_screenwidth()
    screen_height = home.winfo_screenheight()
    home.geometry(f"{screen_width}x{screen_height}")
    customtkinter.set_appearance_mode("dark")
    customtkinter.set_default_color_theme("dark-blue")
    #frame título home
    frame_home_title= customtkinter.CTkFrame(master=home,width=screen_width, height=60).pack(side= TOP)
    label_home_title= customtkinter.CTkLabel(master=frame_home_title, text="Home", font=("Roboto", 25))
    label_home_title.place(x=30, y=10)

    #user name label
    # user_name_label= customtkinter.CTkLabel(master=home, text="Usuário", font=("Roboto", 14)).place(x=(screen_width - 120), y=15)

    #label imagem
    img_homeprofile_path= "images/profile.png"
    img_homeprofile= Image.open(img_homeprofile_path)
    img_homeprofile= img_homeprofile.resize((40,40))
    img_homeprofile= ImageTk.PhotoImage(img_homeprofile)

    label_homeprofile= customtkinter.CTkLabel(master=frame_home_title, image=img_homeprofile, text="Usuário", font=("Roboto", 14) , compound=RIGHT)
    label_homeprofile.place(x=(screen_width - 110), y=10)


    #label principal
    search_bar_entry= customtkinter.CTkEntry(master=home, placeholder_text="Faça sua pesquisa...", width=800, height=35, font=("Roboto", 14), corner_radius=15)
    search_bar_entry.place(x=(screen_width/2) - 400, y=80)
    search_button= customtkinter.CTkButton(master=home, text="Pesquisar", cursor= "hand2",width=100, height=35, font=("Roboto", 14), corner_radius= 20).place(x=(screen_width - 270), y=80)

    filter_combo= customtkinter.CTkComboBox(master=home, width=120, height=35, values=["option 1", "option 2"], corner_radius=20, hover= True , dropdown_hover_color="green", button_hover_color="green").place(x=(screen_width - 160), y=80)

    #adicionar processo button

    def click_add_process():
        pg_cadastro_processo()
        
    add_process_button= customtkinter.CTkButton(master=home, text="Adicionar processo", cursor= "hand2", width=200, height=35, font=("Roboto", 14), corner_radius= 20, command= pg_cadastro_processo).place(x= 30 , y=80)
    
    #frame de conteúdo

    home.mainloop()