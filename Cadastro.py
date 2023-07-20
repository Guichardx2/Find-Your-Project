from tkinter import *
import customtkinter

def pg_cadastro():
    cadastrar=customtkinter.CTk()
    cadastrar.title("Cadastro de Processo") 
    cadastrar.geometry("800x600")
    customtkinter.set_appearance_mode("dark")
    customtkinter.set_default_color_theme("dark-blue")
    txt= Label(cadastrar, text="Vamos começar o cadastro!").grid(column=0, row=0)

    cadastrar.mainloop()
    