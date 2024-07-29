import customtkinter as ctk
from tkinter import filedialog

ctk.set_appearance_mode("dark")  
ctk.set_default_color_theme("blue")

class AppProcess(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.geometry("800x600")
        self.title("Cadastro de Processos")
        self.resizable(False, False)

        # Frame para o título
        self.title_frame = ctk.CTkFrame(self)
        self.title_frame.pack(side= "top" ,pady=10, padx=10, fill="x")

        self.title_label = ctk.CTkLabel(self.title_frame, text="Cadastro de processo", font=("Roboto", 20))
        self.title_label.pack(side="top")

        # Frame para os arquivos
        self.files_frame = ctk.CTkFrame(self, width= 800, height= 600)
        self.files_frame.pack(side="bottom", pady=10, padx=10)

        # Frame para títulos
        self.fields_frame = ctk.CTkFrame(self.files_frame, width= 250, height= 600)
        self.fields_frame.pack(side="left", pady=10, padx=10 ,fill="y")

        self.title_sig_company_label= ctk.CTkLabel(self.fields_frame, text="Sigla da empresa", font=("Roboto", 14)).place(x= 10, y= 15)
        self.title_entry = ctk.CTkEntry(self.fields_frame, placeholder_text="Ex: P.G.P.S...", width= 230, height= 30).place(x= 10, y= 40)

        self.title_process_label= ctk.CTkLabel(self.fields_frame, text="Título do processo", font=("Roboto", 14)).place(x= 10, y= 80)
        self.title_entry = ctk.CTkEntry(self.fields_frame, placeholder_text="Ex: Nome ou local de trabalho...", width= 230, height= 30).place(x= 10, y= 105)

        self.title_placa_label= ctk.CTkLabel(self.fields_frame, text="Placa do veículo", font=("Roboto", 14)).place(x= 10, y= 145)
        self.title_entry = ctk.CTkEntry(self.fields_frame, placeholder_text="Ex: ABC-1234...", width= 230, height= 30).place(x= 10, y= 170)

        # Files Button
        self.add_file_button = ctk.CTkButton(self.fields_frame, text="Adicionar arquivos", width= 200, height= 30, corner_radius= 20, command=self.add_file).place(x= 10, y= 290)

        # Lista de arquivos
        self.files_list = ctk.CTkTextbox(self.files_frame, width=500, height=500)
        self.files_list.pack(side="right", pady=10, padx=10, fill="both", expand=True)

        # Botões de ação
        self.save_button = ctk.CTkButton(self.fields_frame, text="Salvar", width=200, height=30, corner_radius=20, command=self.save_process)
        self.save_button.place(x=10, y=400)
        self.cancel_button = ctk.CTkButton(self.fields_frame, text="Cancelar", width=200, height=30, corner_radius=20, command=self.cancel)
        self.cancel_button.place(x=10, y=450)
        

    def add_file(self):
        filetypes = (
            ('Arquivos do Word', '*.docx'),
            ('Arquivos do Excel', '*.xlsx'),
            ('Imagens', '*.jpg;*.jpeg;*.png'),
        )
        filenames = filedialog.askopenfilenames(
            title='Open files',
            initialdir='/',
            filetypes=filetypes)
        for filename in filenames:
            self.files_list.insert("end", filename)

    def save_process(self):
        # Aqui você implementaria a lógica para salvar os dados do processo, incluindo o título e os arquivos
        print("Salvando processo...")
        print("Título:", self.title_entry.get())
        print("Arquivos:", self.file_list.get(0, "end"))

    def cancel(self):
        self.destroy()
    
if __name__ == "__main__":
    app_process = AppProcess()
    app_process.mainloop()