import customtkinter
from tkinter import *
from tkinter import messagebox
# from cadastro_usuario import *
from PIL import Image, ImageTk
from home import *

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

login_pg= customtkinter.CTk()
login_pg.title('Login')
login_pg.resizable(False, False)
login_pg.geometry("700x400")
    
#img da tela
img_path= "images/pasta.png"
img= Image.open(img_path)
img= img.resize((400,400))
img= ImageTk.PhotoImage(img)

#frame imagem
frame_img= customtkinter.CTkFrame(master=login_pg, width=330, height=400)
frame_img.pack(side=LEFT)

#label imagem
label_img= customtkinter.CTkLabel(master=frame_img, image=img, bg_color="gray", text=None)
label_img.place(x=-30,y=5)

#frame
frame_login= customtkinter.CTkFrame(master=login_pg, width=370, height=400)
frame_login.pack(side=RIGHT)

#frame de login
label_login= customtkinter.CTkLabel(master=frame_login, text="Bem-vindo ao sistema!", font=("Roboto", 25))
label_login.place(x=50, y=10)

#widgtes
user_name_label= customtkinter.CTkLabel(master=frame_login, text="Usuário", font=("Roboto", 14)).place(x=30, y=60)
user_name = customtkinter.CTkEntry(master=frame_login, placeholder_text="Digite seu usuário", width=300, height=35, font=("Roboto", 14), corner_radius=15).place(x=30, y=90)
user_name_warning= customtkinter.CTkLabel(master=frame_login, text="*Este campo é obrigatório*", text_color="green", font=("Roboto", 12), fg_color="transparent").place(x=30, y=130)

password_label= customtkinter.CTkLabel(master=frame_login, text="Senha", font=("Roboto", 14)).place(x=30, y=160)
password = customtkinter.CTkEntry(master=frame_login, placeholder_text="Digite sua senha", width=300, height=35, font=("Roboto", 14), show="*", corner_radius=15).place(x=30, y=190)
password_warning= customtkinter.CTkLabel(master=frame_login, text="*Este campo é obrigatório*", text_color="green", font=("Roboto", 12), fg_color="transparent").place(x=30, y=230)

checkbox= customtkinter.CTkCheckBox(master=frame_login, text="Lembrar de mim", font=("Roboto", 12)).place(x=30, y=270)

def click_login():
    login_pg.destroy()
    pg_home()

#botão
login_button= customtkinter.CTkButton(master=frame_login, text="Entrar", cursor= "hand2",width=300, height=35, font=("Roboto", 14), corner_radius= 20, command=click_login).place(x=30, y=315)

#Tela de cadastro
def pg_cadastro():
    #excluir frame de login
    frame_login.pack_forget()
    
    #criar frame de cadastro
    frame_cadastro= customtkinter.CTkFrame(master=login_pg, width=370, height=400)
    frame_cadastro.pack(side=RIGHT)

    label_cadastro_title= customtkinter.CTkLabel(master=frame_cadastro, text="Cadastro de usuário", font=("Roboto", 25))
    label_cadastro_title.place(x=50, y=10)

    #user icon img
    icon_img_profile_path = "images/profile.png"
    icon_img_profile = Image.open(icon_img_profile_path)
    icon_img_profile = icon_img_profile.resize((30,30))
    icon_img_profile = ImageTk.PhotoImage(icon_img_profile)
    label_img_profile = customtkinter.CTkLabel(master=frame_cadastro, image=icon_img_profile, text=None)
    label_img_profile.place(x=280, y=10)

    label1= customtkinter.CTkLabel(master=frame_cadastro, text="Preencha todos os dados com cuidado!", text_color="yellow",font=("Roboto", 14)).place(x=50, y=50)

    #widgets e labels cadastro
    user_name_label= customtkinter.CTkLabel(master=frame_cadastro, text="Nome Completo", font=("Roboto", 14)).place(x=30, y=80)
    user_name = customtkinter.CTkEntry(master=frame_cadastro, placeholder_text="Digite seu nome", width=300, height=35, font=("Roboto", 14), corner_radius=15).place(x=30, y=110)

    user_email_label= customtkinter.CTkLabel(master=frame_cadastro, text="E-mail", font=("Roboto", 14)).place(x=30, y=150)
    user_email = customtkinter.CTkEntry(master=frame_cadastro, placeholder_text="Digite seu e-mail", width=300, height=35, font=("Roboto", 14), corner_radius=15).place(x=30, y=180)

    user_password_label= customtkinter.CTkLabel(master=frame_cadastro, text="Defina sua senha", font=("Roboto", 14)).place(x=30, y=220)
    user_password = customtkinter.CTkEntry(master=frame_cadastro, placeholder_text="Digite sua senha", width=300, height=35, font=("Roboto", 14), show="*", corner_radius=15).place(x=30, y=250)
    user_confirm_password= customtkinter.CTkEntry(master=frame_cadastro, placeholder_text="Confirme sua senha", width=300, height=35, font=("Roboto", 14), show="*", corner_radius=15).place(x=30, y=290) 

    def click_cadastro():
        msg = messagebox.showinfo(title="Mensagem de cadastro", message="Cadastrado com sucesso!")

    def click_voltar():
        frame_cadastro.pack_forget()
        frame_login.pack(side=RIGHT)

    #botão cadastrar
    cadastro_button= customtkinter.CTkButton(master=frame_cadastro, text="Cadastrar", fg_color="green", hover_color="#014b05",cursor= "hand2",width=130, height=30, font=("Roboto", 14), corner_radius= 20, command= click_cadastro).place(x=200, y=338)
    button_voltar= customtkinter.CTkButton(master=frame_cadastro, text="Voltar",fg_color="#151515", hover_color="#262626", cursor= "hand2",width=130, height=30, font=("Roboto", 14), corner_radius= 20, command= click_voltar).place(x=30, y=338)


cadastro_label= customtkinter.CTkLabel(master=frame_login, text="Ainda não tem uma conta?", font=("Roboto", 14)).place(x=30, y=363)
cadastro_button= customtkinter.CTkButton(master=frame_login, text="Cadastre-se", fg_color="green", hover_color="#014B05" ,cursor= "hand2", width=130, height=25, font=("Roboto", 12), command=pg_cadastro ).place(x=200, y=363)


login_pg.mainloop()    