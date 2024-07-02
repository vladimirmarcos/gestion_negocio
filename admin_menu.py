import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from basic.basic import BasicMethods
from new_supplier import AddNewSupplier

class AdminMenu(BasicMethods):
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

        self.user_menu = ttk.Menu(self.menu_bar, tearoff=0)
        self.user_menu.add_command(label="Crear Usuario", command=self.show_create_user_form)
        self.user_menu.add_command(label="Modificar/Eliminar Usuario", command=self.show_modify_user_form)
        self.menu_bar.add_cascade(label="Usuarios", menu=self.user_menu)

        self.stock_menu = ttk.Menu(self.menu_bar, tearoff=0)
        self.stock_menu.add_command(label="Agregar Stock", command=self.show_add_stock_form)
        self.stock_menu.add_command(label="Ver Stock", command=self.show_view_stock_form)
        self.menu_bar.add_cascade(label="Stock", menu=self.stock_menu)

        self.client_supplier_stock = ttk.Menu(self.menu_bar, tearoff=0)
        self.client_supplier_stock.add_command(label="Crear Nuevo Proveedor", command=self.show_create_new_supplier)
        self.client_supplier_stock.add_command(label="Ver Stock", command=self.show_view_stock_form)
        self.menu_bar.add_cascade(label="Cliente/Provedores", menu=self.client_supplier_stock)

        self.root.config(menu=self.menu_bar)

        

    
        

    def logout(self):
        self.delete_frame(self.frame)
        self.menu_bar.destroy()
        self.login_screen.show_login_screen()

    def show_create_user_form(self):
        self.delete_frame(self.frame)
        from create_user_form import CreateUserForm
        CreateUserForm(self.frame)

    def show_modify_user_form(self):
        self.delete_frame(self.frame)
        from modify_user_form import ModifyUserForm
        ModifyUserForm(self.frame)

    def show_add_stock_form(self):
        self.delete_frame(self.frame)
        from add_stock_form import AddStockForm
        AddStockForm(self.frame)

    def show_view_stock_form(self):
        self.delete_frame(self.frame)
        from view_stock_form import ViewStockForm
        ViewStockForm(self.frame)

    def show_create_new_supplier(self):
        self.delete_frame(self.frame)
        AddNewSupplier(self.frame)