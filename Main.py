from tkinter import *
from cadastro import * 
import customtkinter
from PIL import Image, ImageTk

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

home= customtkinter.CTk()
home.title('Login')
home.resizable(False, False)
home.geometry("700x400")
    
#img da tela
img_path= "images/pasta.png"
img= Image.open(img_path)
img= img.resize((400,400))
img= ImageTk.PhotoImage(img)

#frame imagem
frame_img= customtkinter.CTkFrame(master=home, width=350, height=400)
frame_img.pack(side=LEFT)

#label imagem
label_img= customtkinter.CTkLabel(master=frame_img, image=img, bg_color="lightblue", text=None)
label_img.place(x=-10,y=5)

#frame
frame_login= customtkinter.CTkFrame(master=home, width=350, height=400)
frame_login.pack(side=RIGHT)

#frame de login
label_login= customtkinter.CTkLabel(master=frame_login, text="Bem-vindo ao sistema!", font=("Roboto", 25))
label_login.place(x=50, y=10)

#widgtes
user_name_label= customtkinter.CTkLabel(master=frame_login, text="Usuário", font=("Roboto", 14)).place(x=30, y=70)
user_name = customtkinter.CTkEntry(master=frame_login, placeholder_text="Digite seu usuário", width=300, height=35, font=("Roboto", 14), corner_radius=15).place(x=30, y=100)
user_name_warning= customtkinter.CTkLabel(master=frame_login, text="*Este campo é obrigatório*", text_color="green", font=("Roboto", 12), fg_color="transparent").place(x=30, y=140)

password_label= customtkinter.CTkLabel(master=frame_login, text="Senha", font=("Roboto", 14)).place(x=30, y=180)
password = customtkinter.CTkEntry(master=frame_login, placeholder_text="Digite sua seha", width=300, height=35, font=("Roboto", 14), show="*", corner_radius=15).place(x=30, y=210)
password_warning= customtkinter.CTkLabel(master=frame_login, text="*Este campo é obrigatório*", text_color="green", font=("Roboto", 12), fg_color="transparent").place(x=30, y=250)

#botão
login_button= customtkinter.CTkButton(master=frame_login, text="Entrar", width=300, height=35, font=("Roboto", 14), corner_radius= 20).place(x=30, y=300)

cadastro_label= customtkinter.CTkLabel(master=frame_login, text="Ainda não tem uma conta?", font=("Roboto", 12)).place(x=30, y=370)
cadastro_button= customtkinter.CTkButton(master=frame_login, text="Cadastre-se", width=100, height=25, font=("Roboto", 12)).place(x=180, y=370)
home.mainloop()    