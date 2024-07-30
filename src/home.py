import customtkinter as ctk
from tkinter import *
from PIL import Image, ImageTk
from cadastro_processo import AppProcess


class ApplicationHome():

    def __init__(self):
        self.home = ctk.CTk()
        self.tema_home()
        self.home_screen()

    def tema_home(self):
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")

    def home_screen(self):    
        self.home.title("Home") 
        screen_width = self.home.winfo_screenwidth()
        screen_height = self.home.winfo_screenheight()
        # home.attributes("-fullscreen", True)
        self.home.geometry(f"{screen_width}x{screen_height}")

        #frame título home
        frame_home_title= ctk.CTkFrame(master=self.home,width=screen_width, height=70).pack(side= TOP)
        label_home_title= ctk.CTkLabel(master=frame_home_title, text="Home", font=("Roboto", 25))
        label_home_title.place(x=30, y=15)

        #label imagem
        img_homeprofile_path= "images/profile.png"
        img_homeprofile= Image.open(img_homeprofile_path)
        img_homeprofile= img_homeprofile.resize((40,40))
        img_homeprofile= ImageTk.PhotoImage(img_homeprofile)

        label_homeprofile= ctk.CTkLabel(master=frame_home_title, image=img_homeprofile, text="Usuário", font=("Roboto", 14) , compound=RIGHT, padx=10)
        label_homeprofile.place(x=(screen_width - 140), y=15)


        #label principal
        search_bar_entry= ctk.CTkEntry(master=self.home, placeholder_text="Faça sua pesquisa...", width=800, height=35, font=("Roboto", 14), corner_radius=15)
        search_bar_entry.place(x=(screen_width/2) - 400, y=90)
        search_button= ctk.CTkButton(master=self.home, text="Pesquisar", cursor= "hand2",width=100, height=35, font=("Roboto", 14), corner_radius= 20)
        search_button.place(x=(screen_width - 270), y=90)

        filter_combo= ctk.CTkComboBox(master=self.home, width=120, height=35, values=["Filtro", "option 2"], corner_radius=20, hover= True , dropdown_hover_color="green", button_hover_color="green")
        filter_combo.place(x=(screen_width - 160), y=90)

    #adicionar processo button
        def click_add_process():
            app_process= AppProcess()
            app_process.mainloop()
                
        add_process_button= ctk.CTkButton(master=self.home, text="Adicionar processo", cursor= "hand2", width=200, height=35, font=("Roboto", 14), corner_radius= 20, command= click_add_process).place(x= 30 , y=90)
            
        #frame de conteúdo
        scrollable_frame = ctk.CTkScrollableFrame(master=self.home, width=screen_width, height=(screen_height-230), scrollbar_fg_color="#46295A", fg_color="#1a1b1b", orientation="vertical")
        scrollable_frame.pack(side=BOTTOM)

        #conteúdo
        for i in range(10):
            frame_content = ctk.CTkFrame(master=scrollable_frame, width=(screen_width - 40), height=100, fg_color="#46295A")
            frame_content.pack(side=TOP, pady=10)

            #button visualizar
            # def click_view():
            #     pass
            button_cover= ctk.CTkButton(master=frame_content, text="Visualizar", cursor= "hand2", width=(screen_width - 40), height=100, font=("Roboto", 14), fg_color="#46295A")
            button_cover.pack(side= BOTTOM)
            label_content = ctk.CTkLabel(master=button_cover, text=f"Processo {i+2}", font=("Roboto", 14))
            label_content.place(x=10, y=10)

if __name__ == "__main__":
    app_home = ApplicationHome()
    app_home.home.mainloop()