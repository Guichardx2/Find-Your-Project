from tkinter import *
from Cadastro import * 
import customtkinter

class Home(Tk):
    customtkinter.set_appearance_mode("dark")
    customtkinter.set_default_color_theme("dark-blue")
    inicio= customtkinter.CTk()
    inicio.title('Find Your Process')
    inicio.geometry("700x400")
    
    img= PhotoImage(file= "bemvindo-transformed.png")
    label_img= customtkinter.CTkLabel(master= inicio, image= img)
    label_img.place(x=5, y=65)

    welcome= Label(inicio, text= "Bem-vindo a um pequeno programa de ajuda na organização!").grid(column=0, row= 0, padx=10, pady=10 )
    txt= Label(inicio, text= "Escolha uma das opções abaixo, o que deseja fazer? Vai no teu tempo!").grid(column=0, row=1, pady=10)
    btn_Cadastro= Button(inicio, text= "Cadastrar processo", command= pg_cadastro).grid(column=0, row=2, pady=5)
    btn_Consulta= Button(inicio, text= "Consultar um processo", command= inicio.destroy).grid(column=0, row=3)
    
    inicio.mainloop()    
    
