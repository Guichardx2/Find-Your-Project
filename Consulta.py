from tkinter import * 
import customtkinter

def pg_consulta ():
    consulta= customtkinter.CTk()
    customtkinter.set_appearance_mode("dark")
    customtkinter.set_default_color_theme("dark-blue")
    consulta.title('Consulta de Processo')
    consulta.geometry("800x600")
    
    consulta.mainloop()