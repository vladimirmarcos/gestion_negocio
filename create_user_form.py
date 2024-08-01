import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import messagebox
from connect.account import create_user

class CreateUserForm:
    def __init__(self, parent_frame):
        self.parent_frame = parent_frame
        self.create_widgets()

    def create_widgets(self):
        self.label_create = ttk.Label(self.parent_frame, text="Crear Usuario", font=("Helvetica", 18))
        self.label_create.grid(row=0, column=0, columnspan=2, pady=10)

        self.label_username_create = ttk.Label(self.parent_frame, text="Usuario:")
        self.label_username_create.grid(row=1, column=0, pady=5)
        self.entry_username_create = ttk.Entry(self.parent_frame)
        self.entry_username_create.grid(row=1, column=1, pady=5)

        self.label_password_create = ttk.Label(self.parent_frame, text="Contraseña:")
        self.label_password_create.grid(row=2, column=0, pady=5)
        self.entry_password_create = ttk.Entry(self.parent_frame, show="*")
        self.entry_password_create.grid(row=2, column=1, pady=5)

        self.label_role_create = ttk.Label(self.parent_frame, text="Rol:")
        self.label_role_create.grid(row=3, column=0, pady=5)
        self.social_condition = ttk.Combobox(
        self.parent_frame,
        state="readonly",
        values=["admin","user"],width=20
         )
        self.social_condition.set("user")
        self.social_condition.grid(row=3, column=1, pady=5,sticky="w")

        self.button_create_user = ttk.Button(self.parent_frame, text="Crear Usuario", command=self.create_user,width=19)
        self.button_create_user.grid(row=4, column=0, columnspan=2, pady=10)

    def create_user(self):
        username = self.entry_username_create.get()
        password = self.entry_password_create.get()
        role = self.role_var_create.get()

        if username and password:
            if create_user(username, password, role):
                messagebox.showinfo("Éxito", "Usuario creado exitosamente.")
            else:
                messagebox.showerror("Error", "El usuario ya existe.")
        else:
            messagebox.showerror("Error", "Por favor complete todos los campos.")
