import ttkbootstrap as ttk
from ttkbootstrap.constants import *

class ModifyUserForm:
    def __init__(self, parent):
        self.parent = parent
        self.create_form()

    def create_form(self):
        self.label_modify = ttk.Label(self.parent, text="Modificar/Eliminar Usuario", font=("Helvetica", 18))
        self.label_modify.grid(row=0, column=0, columnspan=2, pady=10)

        self.label_username_modify = ttk.Label(self.parent, text="Username:")
        self.label_username_modify.grid(row=1, column=0, pady=5)
        self.entry_username_modify = ttk.Entry(self.parent)
        self.entry_username_modify.grid(row=1, column=1, pady=5)

        self.label_role_modify = ttk.Label(self.parent, text="Nuevo Role:")
        self.label_role_modify.grid(row=2, column=0, pady=5)
        self.role_var_modify = ttk.StringVar()
        self.role_var_modify.set("user")
        self.option_role_modify = ttk.OptionMenu(self.parent, self.role_var_modify, "user", "user", "admin")
        self.option_role_modify.grid(row=2, column=1, pady=5)

        self.button_update_role = ttk.Button(self.parent, text="Actualizar Role", command=self.update_role)
        self.button_update_role.grid(row=3, column=0, columnspan=2, pady=10)

        self.button_delete_user = ttk.Button(self.parent, text="Eliminar Usuario", command=self.delete_user)
        self.button_delete_user.grid(row=4, column=0, columnspan=2, pady=10)

    def update_role(self):
        # Lógica para actualizar rol de usuario
        pass

    def delete_user(self):
        # Lógica para eliminar usuario
        pass
