import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import messagebox
from forgot_password import ForgotPasswordScreen
from connect.account import verify_user
from admin_menu import AdminMenu
from user_menu import UserMenu

class LoginScreen:
    def __init__(self, root):
        self.root = root
        self.root.title("Ingreso")
        self.frame = None
        self.show_login_screen()

    def show_login_screen(self):
        if self.frame:
            self.frame.destroy()
             
            self.emptyMenu = ttk.Menu(self.root)
            self.root.config(menu=self.emptyMenu)
            
        
        self.frame = ttk.Frame(self.root, padding=20)
        self.frame.pack()

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
        self.button_forgot_password.grid(row=3, columnspan=2, pady=10)

    def login(self, event=None):
        username = self.entry_username.get()
        password = self.entry_password.get()

        user = verify_user(username, password)
        if user:
            role = user[0]
            if role == 'admin':
                self.frame.destroy()
                AdminMenu(self.root, self)
            else:
                self.frame.destroy()
                UserMenu(self.root, self)
        else:
            messagebox.showerror("Error", "Usuario o contraseña incorrectos.")

    def show_forgot_password(self):
        self.frame.destroy()
        ForgotPasswordScreen(self.root, self)

    def logout(self):
        self.show_login_screen()
