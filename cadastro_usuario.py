from tkinter import *
import customtkinter
from PIL import Image, ImageTk

def pg_cadastro():

    cadastro=customtkinter.CTk()
    cadastro.title("Cadastro de usuário") 
    cadastro.geometry("700x400")
    customtkinter.set_appearance_mode("dark")
    customtkinter.set_default_color_theme("dark-blue")
    
    #frame título cadastro
    frame_cadastro_title= customtkinter.CTkFrame(master=cadastro, width=700, height=40)
    frame_cadastro_title.pack(side= TOP)

    label_cadastro_title= customtkinter.CTkLabel(master=frame_cadastro_title, text="Cadastro de usuário", font=("Roboto", 25))
    label_cadastro_title.place(x=250, y=10)

    icon_img_profile_path = "images/profile.png"
    icon_img_profile = Image.open(icon_img_profile_path)
    icon_img_profile = icon_img_profile.resize((30,30))
    icon_img_profile = ImageTk.PhotoImage(icon_img_profile)
    label_img_profile = customtkinter.CTkLabel(master=frame_cadastro_title, image=icon_img_profile, text=None)
    label_img_profile.place(x=480, y=10)

    #widgets e labels cadastro
    frame_cadastro= customtkinter.CTkFrame(master=cadastro, width=700, height=360)
    frame_cadastro.pack(side= BOTTOM)

    user_name_label= customtkinter.CTkLabel(master=frame_cadastro, text="Nome Completo", font=("Roboto", 14)).place(x=220, y=10)
    user_name = customtkinter.CTkEntry(master=frame_cadastro, placeholder_text="Digite seu nome", width=300, height=35, font=("Roboto", 14), corner_radius=15).place(x=220, y=40)

    user_email_label= customtkinter.CTkLabel(master=frame_cadastro, text="E-mail", font=("Roboto", 14)).place(x=220, y=80)
    user_email = customtkinter.CTkEntry(master=frame_cadastro, placeholder_text="Digite seu e-mail", width=300, height=35, font=("Roboto", 14), corner_radius=15).place(x=220, y=110)

    user_password_label= customtkinter.CTkLabel(master=frame_cadastro, text="Senha", font=("Roboto", 14)).place(x=220, y=150)
    user_password = customtkinter.CTkEntry(master=frame_cadastro, placeholder_text="Digite sua senha", width=300, height=35, font=("Roboto", 14), show="*", corner_radius=15).place(x=220, y=180)
    user_confirm_password= customtkinter.CTkEntry(master=frame_cadastro, placeholder_text="Confirme sua senha", width=300, height=35, font=("Roboto", 14), show="*", corner_radius=15).place(x=220, y=220) 

    def click_cadastro():
        label_cadastro_title= customtkinter.CTkLabel(master= frame_cadastro, text="Usuário cadastrado com sucesso!", text_color="Green", font=("Roboto", 14)).place(x=270, y=320)
        

    #botão cadastrar
    cadastro_button= customtkinter.CTkButton(master=frame_cadastro, text="Cadastrar" ,cursor= "hand2",width=300, height=35, font=("Roboto", 14), corner_radius= 20, command= click_cadastro).place(x=220, y=280)

    cadastro.mainloop()