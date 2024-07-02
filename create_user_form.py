import ttkbootstrap as ttk
from ttkbootstrap.constants import *

class CreateUserForm:
    def __init__(self, parent):
        self.parent = parent
        self.create_form()

    def create_form(self):
        self.label_create = ttk.Label(self.parent, text="Crear Usuario", font=("Helvetica", 18))
        self.label_create.grid(row=0, column=0, columnspan=2, pady=10)

        self.label_username_create = ttk.Label(self.parent, text="Username:")
        self.label_username_create.grid(row=1, column=0, pady=5)
        self.entry_username_create = ttk.Entry(self.parent)
        self.entry_username_create.grid(row=1, column=1, pady=5)

        self.label_password_create = ttk.Label(self.parent, text="Password:")
        self.label_password_create.grid(row=2, column=0, pady=5)
        self.entry_password_create = ttk.Entry(self.parent, show="*")
        self.entry_password_create.grid(row=2, column=1, pady=5)

        self.label_role_create = ttk.Label(self.parent, text="Role:")
        self.label_role_create.grid(row=3, column=0, pady=5)
        self.role_var_create = ttk.StringVar()
        self.role_var_create.set("user")
        self.option_role_create = ttk.OptionMenu(self.parent, self.role_var_create, "user", "user", "admin")
        self.option_role_create.grid(row=3, column=1, pady=5)

        self.button_create_user = ttk.Button(self.parent, text="Crear Usuario", command=self.create_user)
        self.button_create_user.grid(row=4, column=0, columnspan=2, pady=10)

    def create_user(self):
        # Lógica para crear usuario
        pass
