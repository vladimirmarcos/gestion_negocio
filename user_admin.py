import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import messagebox

class UserMenu:
    def __init__(self, root, login_screen):
        self.root = root
        self.login_screen = login_screen
        self.root.title("User Menu")
        
        # Crear barra de menú
        self.menu_bar = ttk.Menu(self.root)
        
        # Crear menú Archivo
        self.file_menu = ttk.Menu(self.menu_bar, tearoff=0)
        self.file_menu.add_command(label="Option 1", command=self.option1)
        self.file_menu.add_command(label="Option 2", command=self.option2)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Cerrar Sesión", command=self.logout)
        self.menu_bar.add_cascade(label="Archivo", menu=self.file_menu)
        
        # Crear menú Ayuda
        self.help_menu = ttk.Menu(self.menu_bar, tearoff=0)
        self.help_menu.add_command(label="About", command=self.show_about)
        self.menu_bar.add_cascade(label="Ayuda", menu=self.help_menu)
        
        # Configurar la barra de menú
        self.root.config(menu=self.menu_bar)

        # Frame principal
        self.frame = ttk.Frame(self.root, padding=20)
        self.frame.pack(pady=100)

        self.label = ttk.Label(self.frame, text="User Menu", font=("Helvetica", 24))
        self.label.pack(pady=20)

        self.button1 = ttk.Button(self.frame, text="Option 1", command=self.option1)
        self.button1.pack(pady=10)

        self.button2 = ttk.Button(self.frame, text="Option 2", command=self.option2)
        self.button2.pack(pady=10)

    def clear_frame(self):
        for widget in self.frame.winfo_children():
            widget.destroy()

    def option1(self):
        self.clear_frame()
        self.label = ttk.Label(self.frame, text="Option 1 Selected", font=("Helvetica", 24))
        self.label.pack(pady=20)
        print("User Option 1 selected")

    def option2(self):
        self.clear_frame()
        self.label = ttk.Label(self.frame, text="Option 2 Selected", font=("Helvetica", 24))
        self.label.pack(pady=20)
        print("User Option 2 selected")

    def show_about(self):
        messagebox.showinfo("About", "User Menu\nVersion 1.0")

    def logout(self):
        self.frame.destroy()
        self.login_screen.show_login_screen()
