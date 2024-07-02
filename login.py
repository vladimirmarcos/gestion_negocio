import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import messagebox
from forgot_password import ForgotPasswordScreen
from db import verify_user,user_exists
from admin_menu import AdminMenu
from basic.basic import BasicMethods
from user_menu import UserMenu
class LoginScreen(BasicMethods):
    def __init__(self, root):
        self.root = root
        self.root.title("Ingreso")
        self.frame = None
        self.show_login_screen()

    def show_login_screen(self):
        """_summary_
        """        
        self.delete_frame(self.frame)
        
        self.frame = ttk.Frame(self.root)
        self.frame.pack(pady=100)

        self.label_username = ttk.Label(self.frame, text="Usuario:")
        self.label_username.grid(row=0, column=0, pady=10)

        self.entry_username = ttk.Entry(self.frame)
        self.entry_username.grid(row=0, column=1, pady=10)
        self.entry_username.bind("<Return>", self.login)

        self.label_password = ttk.Label(self.frame, text="Password:")
        self.label_password.grid(row=1, column=0, pady=10)

        self.entry_password = ttk.Entry(self.frame, show="*")
        self.entry_password.grid(row=1, column=1, pady=10)
        self.entry_password.bind("<Return>", self.login)

        self.button_forgot_password = ttk.Button(self.frame, text="Recuperar Contraseña", command=self.show_forgot_password)
        self.button_forgot_password.grid(row=3, column=1)

    def login(self,event):
        """_summary_

        Args:
            event (_type_): _description_
        """        
        user = user_exists(self.entry_username.get())
        if user:
            user_login=verify_user(self.entry_username.get(),self.entry_password.get())
            if user_login:
                if user_login[0]== 'admin':
                    self.frame.destroy()
                    AdminMenu(self.root, self)
                else:
                 self.frame.destroy()
                 UserMenu(self.root, self)
            else:
                messagebox.showerror("Error", "Usuario o contraseña incorrectos.")
                self.clear_entry(self.frame)

        else:
            messagebox.showerror("Error", f"Usuario {self.entry_username.get()} no existe")
            self.clear_entry(self.frame)

    def show_forgot_password(self):
        """_summary_
        """        
        self.frame.destroy()
        ForgotPasswordScreen(self.root, self)
