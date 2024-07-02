import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

class UserMenu:
    def __init__(self, root, login_screen):
        self.root = root
        self.login_screen = login_screen
        self.frame = None
        self.create_widgets()

    def create_widgets(self):
        self.menu_bar = ttk.Menu(self.root)

        self.file_menu = ttk.Menu(self.menu_bar, tearoff=0)
        self.file_menu.add_command(label="Cerrar Sesión", command=self.logout)
        self.menu_bar.add_cascade(label="Archivo", menu=self.file_menu)

        self.stock_menu = ttk.Menu(self.menu_bar, tearoff=0)
        self.stock_menu.add_command(label="Agregar Stock", command=self.show_add_stock_form)
        self.stock_menu.add_command(label="Ver Stock", command=self.show_view_stock_form)
        self.menu_bar.add_cascade(label="Stock", menu=self.stock_menu)

        self.root.config(menu=self.menu_bar)

        self.frame = ttk.Frame(self.root)
        self.frame.pack()

        self.label = ttk.Label(self.frame, text="User Menu", font=("Helvetica", 24))
        self.label.pack(pady=20)

        self.button1 = ttk.Button(self.frame, text="Option 1", command=self.option1)
        self.button1.pack(pady=10)

        self.button2 = ttk.Button(self.frame, text="Option 2", command=self.option2)
        self.button2.pack(pady=10)

    def clear_frame(self):
        if self.frame:
            self.frame.destroy()
        self.frame = ttk.Frame(self.root)
        self.frame.pack()

    def logout(self):
        self.clear_frame()
        self.menu_bar.destroy()
        self.login_screen.show_login_screen()

    def option1(self):
        self.clear_frame()
        self.label = ttk.Label(self.frame, text="Option 1 Selected", font=("Helvetica", 24))
        self.label.pack(pady=20)

    def option2(self):
        self.clear_frame()
        self.label = ttk.Label(self.frame, text="Option 2 Selected", font=("Helvetica", 24))
        self.label.pack(pady=20)

    def show_add_stock_form(self):
        self.clear_frame()
        from add_stock_form import AddStockForm
        AddStockForm(self.frame)

    def show_view_stock_form(self):
        self.clear_frame()
        from view_stock_form import ViewStockForm
        ViewStockForm(self.frame)
