import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import messagebox
from basic.basic import clear_entry

class AddProviderForm:
    def __init__(self, parent_frame):
        self.parent_frame = parent_frame
        self.create_widgets()
    #drofasa
    def create_widgets(self):
        self.label_add_provider = ttk.Label(self.parent_frame, text="Agregar Proveedor", font=("Helvetica", 18))
        self.label_add_provider.grid(row=0, column=0, columnspan=2, pady=10)

        self.label_razon_social = ttk.Label(self.parent_frame, text="Razón Social:")
        self.label_razon_social.grid(row=1, column=0, pady=5,sticky="w")
        self.entry_razon_social = ttk.Entry(self.parent_frame,width=22)
        self.entry_razon_social.grid(row=1, column=1, pady=5,sticky="w")

        self.label_nombre_comercial = ttk.Label(self.parent_frame, text="Nombre Comercial:")
        self.label_nombre_comercial.grid(row=2, column=0, pady=5,sticky="w")
        self.entry_nombre_comercial = ttk.Entry(self.parent_frame,width=22)
        self.entry_nombre_comercial.grid(row=2, column=1, pady=5,sticky="w")

        self.label_cuit = ttk.Label(self.parent_frame, text="C.U.I.T.:" )
        self.label_cuit.grid(row=3, column=0, pady=5,sticky="w")
        self.entry_cuit = ttk.Entry(self.parent_frame,width=22)
        self.entry_cuit.grid(row=3, column=1, pady=5,sticky="w")

        self.label_telefono = ttk.Label(self.parent_frame, text="Teléfono:" )
        self.label_telefono.grid(row=4, column=0, pady=5,sticky="w")
        self.entry_telefono = ttk.Entry(self.parent_frame,width=22)
        self.entry_telefono.grid(row=4, column=1, pady=5,sticky="w")

        self.label_correo = ttk.Label(self.parent_frame, text="Correo:" )
        self.label_correo.grid(row=5, column=0, pady=5,sticky="w")
        self.entry_correo = ttk.Entry(self.parent_frame,width=22)
        self.entry_correo.grid(row=5, column=1, pady=5,sticky="w")

        self.label_social_condition = ttk.Label(self.parent_frame, text="Condición Social:" )
        self.label_social_condition.grid(row=6, column=0, pady=5,sticky="w")
        self.social_condition = ttk.Combobox(
        self.parent_frame,
        state="readonly",
        values=["Responsable Inscripto","Monostributista"]
         )
        self.social_condition.set("Responsable Inscripto")
        self.social_condition.grid(row=6, column=1, pady=5,sticky="w")

        self.label_modify_stock = ttk.Label(self.parent_frame, text="Modifica Stock:")
        self.label_modify_stock.grid(row=7, column=0, pady=5,sticky="w")

        self.modify_stock = ttk.Combobox(
        self.parent_frame,
        state="readonly",
        values=["Si","No"]
         )
        self.modify_stock.set("Si")
        self.modify_stock.grid(row=7, column=1, pady=5,sticky="w")

        self.button_add_provider = ttk.Button(self.parent_frame, text="Agregar Proveedor", command=self.add_provider,width=21)
        self.button_add_provider.grid(row=8, column=1, pady=10)

    def add_provider(self):
        
        if not (self.entry_razon_social.get()) or not (self.entry_cuit.get()):
            messagebox.showerror("Error", "La razón social y C.U.I.T. no puede estar en blanco.")
            
            clear_entry(self.parent_frame)
        else:
            messagebox.showinfo("Salio Bien","Boca Boca Boca")