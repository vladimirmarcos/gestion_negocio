import ttkbootstrap as ttk
from ttkbootstrap.constants import *
#from login import LoginScreen
from add_drugs_form import AdddrugsForm
from view_drugs_form import ViewdrugsForm
from add_provider_form import AddProviderForm

class UserMenu:
    def __init__(self, root, login_screen):
        self.root = root
        self.login_screen = login_screen
        self.frame = None
        self.create_menu()
        self.show_main_menu()

    def create_menu(self):
        self.menu_bar = ttk.Menu(self.root)
        self.root.config(menu=self.menu_bar)

        self.stock_menu = ttk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Stock", menu=self.stock_menu)
        self.stock_menu.add_command(label="Agregar Stock", command=self.show_add_stock_form)
        self.stock_menu.add_command(label="Ver Stock", command=self.show_view_stock_form)

        self.provider_menu = ttk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Proveedor", menu=self.provider_menu)
        self.provider_menu.add_command(label="Agregar Proveedor", command=self.show_add_provider_form)

        self.user_menu = ttk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Usuario", menu=self.user_menu)
        self.user_menu.add_command(label="Cerrar Sesión", command=self.logout)

    def show_main_menu(self):
        self.clear_frame()
        self.frame = ttk.Frame(self.root, padding=20)
        self.frame.pack(pady=100)

        self.label = ttk.Label(self.frame, text="User Menu", font=("Helvetica", 24))
        self.label.pack(pady=20)

    def clear_frame(self):
        if self.frame:
            self.frame.destroy()
        self.frame = ttk.Frame(self.root)
        self.frame.pack()

    def show_add_stock_form(self):
        self.clear_frame()
        AdddrugsForm(self.frame)

    def show_view_stock_form(self):
        self.clear_frame()
        ViewdrugsForm(self.frame)

    def show_add_provider_form(self):
        self.clear_frame()
        AddProviderForm(self.frame)

    def logout(self):
        self.clear_frame()
        self.login_screen.show_login_screen()
