import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import messagebox
from connect.account import  delete_user

class ModifyUserForm:
    def __init__(self, parent_frame):
        self.parent_frame = parent_frame
        self.create_widgets()

    def create_widgets(self):
        self.label_modify = ttk.Label(self.parent_frame, text="Modificar Usuario", font=("Helvetica", 18))
        self.label_modify.grid(row=0, column=0, columnspan=2, pady=10)

        self.label_select_user = ttk.Label(self.parent_frame, text="Seleccione Usuario:")
        self.label_select_user.grid(row=1, column=0, pady=5)
        self.user_var = ttk.StringVar()
        self.option_user = ttk.OptionMenu(self.parent_frame, self.user_var, "", *self.get_user_list())
        self.option_user.grid(row=1, column=1, pady=5)
        self.user_var.trace("w", self.load_user_details)

        self.label_username_modify = ttk.Label(self.parent_frame, text="Username:")
        self.label_username_modify.grid(row=2, column=0, pady=5)
        self.entry_username_modify = ttk.Entry(self.parent_frame)
        self.entry_username_modify.grid(row=2, column=1, pady=5)

        self.label_password_modify = ttk.Label(self.parent_frame, text="Password:")
        self.label_password_modify.grid(row=3, column=0, pady=5)
        self.entry_password_modify = ttk.Entry(self.parent_frame, show="*")
        self.entry_password_modify.grid(row=3, column=1, pady=5)

        self.label_role_modify = ttk.Label(self.parent_frame, text="Role:")
        self.label_role_modify.grid(row=4, column=0, pady=5)
        self.role_var_modify = ttk.StringVar()
        self.option_role_modify = ttk.OptionMenu(self.parent_frame, self.role_var_modify, "user", "user", "admin")
        self.option_role_modify.grid(row=4, column=1, pady=5)

        self.button_modify_user = ttk.Button(self.parent_frame, text="Modificar Usuario", command=self.modify_user)
        self.button_modify_user.grid(row=5, column=0, columnspan=2, pady=10)

        self.button_delete_user = ttk.Button(self.parent_frame, text="Eliminar Usuario", command=self.delete_user)
        self.button_delete_user.grid(row=6, column=0, columnspan=2, pady=10)

    def get_user_list(self):
        print()

    def load_user_details(self, *args):
        print ()

    def modify_user(self):
        username = self.entry_username_modify.get()
        password = self.entry_password_modify.get()
        #role = self.role_var_modify.get()
        """
        if username and password:
            if modify_user(username, password, role):
                messagebox.showinfo("Éxito", "Usuario modificado exitosamente.")
            else:
                messagebox.showerror("Error", "No se pudo modificar el usuario.")
        else:
            messagebox.showerror("Error", "Por favor complete todos los campos.")"""

    def delete_user(self):
        username = self.user_var.get()

        if username:
            if delete_user(username):
                messagebox.showinfo("Éxito", "Usuario eliminado exitosamente.")
                self.parent_frame.master.menu.user_menu.entryconfig("Modificar/Eliminar Usuario", state="normal")
                self.parent_frame.master.clear_frame()
                ModifyUserForm(self.parent_frame)
            else:
                messagebox.showerror("Error", "No se pudo eliminar el usuario.")
        else:
            messagebox.showerror("Error", "Por favor seleccione un usuario.")
