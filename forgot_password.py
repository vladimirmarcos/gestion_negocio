import ttkbootstrap as ttk
from tkinter import messagebox
from connect.account import update_password, user_exists
from basic.basic import clear_entry
class ForgotPasswordScreen:
    """_summary_
    """    
    def __init__(self, root, login_screen):
        self.root = root
        self.login_screen = login_screen
        self.forgotPasswordField()

    def forgotPasswordField(self):
        """_summary_
        """        
        self.frame_forgot = ttk.Frame(self.root, padding=20)

        self.label_forgot_password = ttk.Label(self.frame_forgot, text="Usuario:")
        self.label_forgot_password.grid(row=0, column=0, pady=10)

        self.entry_forgot_username = ttk.Entry(self.frame_forgot)
        self.entry_forgot_username.grid(row=0, column=1, pady=10)

        self.label_new_password = ttk.Label(self.frame_forgot, text="Nueva Contraseña:")
        self.label_new_password.grid(row=1, column=0, pady=10)

        self.entry_new_password = ttk.Entry(self.frame_forgot, show="*")
        self.entry_new_password.grid(row=1, column=1, pady=10)

        self.label_confirm_password = ttk.Label(self.frame_forgot, text="Confirmar Contraseña:")
        self.label_confirm_password.grid(row=2, column=0, pady=10)

        self.entry_confirm_password = ttk.Entry(self.frame_forgot, show="*")
        self.entry_confirm_password.grid(row=2, column=1, pady=10)

        self.button_back_to_login = ttk.Button(self.frame_forgot, text="Volver a Login", command=self.back_to_login)
        self.button_back_to_login.grid(row=3, columnspan=2, pady=10)

        self.frame_forgot.pack(pady=5)

        # Bindear la tecla Enter a los entry para modificar contraseña
        self.entry_forgot_username.bind("<Return>", self.change_password)
        self.entry_new_password.bind("<Return>", self.change_password)
        self.entry_confirm_password.bind("<Return>", self.change_password)

    def change_password(self, event):
        """_summary_

        Args:
            event (_type_): _description_
        """        
        if not self.entry_forgot_username.get():
            messagebox.showerror("Error", "Por favor ingrese el nombre de usuario.")
            clear_entry(self.frame_forgot)
        else:
            if user_exists( self.entry_forgot_username.get()):
                if not (self.entry_new_password.get() and self.entry_confirm_password.get()):
                        messagebox.showerror("Error", "Tiene ambos campos de contraseñas vacías.")
                        clear_entry(self.frame_forgot)
                else:   
                 if self.entry_new_password.get() == self.entry_confirm_password.get():
                    if update_password( self.entry_forgot_username.get(), self.entry_new_password.get()):
                        messagebox.showinfo("Éxito", "Contraseña actualizada correctamente.")
                        self.back_to_login()
                    else:
                        messagebox.showerror("Error", "No se pudo actualizar la contraseña.")
                        clear_entry(self.frame_forgot)
                 else:
                    messagebox.showerror("Error", "Las contraseñas no coinciden. Inténtelo de nuevo.")
                    clear_entry(self.frame_forgot)
            else:
                messagebox.showerror("Error", f"Usuario {self.entry_forgot_username.get()} no existe.")
                clear_entry(self.frame_forgot)

    def back_to_login(self):
        self.frame_forgot.destroy()
        self.login_screen.show_login_screen()

    