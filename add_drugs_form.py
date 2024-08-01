import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import messagebox
from basic.basic import clear_entry
class AdddrugsForm:
    def __init__(self, parent_frame):
        print (parent_frame)
        self.parent_frame = parent_frame
        self.create_widgets()

    def create_widgets(self):
        self.label_add_stock = ttk.Label(self.parent_frame, text="Agregar Nueva Droga", font=("Helvetica", 18))
        self.label_add_stock.grid(row=0, column=0, columnspan=2, pady=10)

        self.label_monodroga = ttk.Label(self.parent_frame, text="Monodroga:")
        self.label_monodroga.grid(row=1, column=0, pady=5,sticky="w")
        self.entry_monodroga = ttk.Entry(self.parent_frame,width=21)
        self.entry_monodroga.grid(row=1, column=1, pady=5)

        self.label_nombre_comercial = ttk.Label(self.parent_frame, text="Nombre Comercial:")
        self.label_nombre_comercial.grid(row=2, column=0, pady=5,sticky="w")
        self.entry_nombre_comercial = ttk.Entry(self.parent_frame,width=21)
        self.entry_nombre_comercial.grid(row=2, column=1, pady=5)

        self.label_descripcion = ttk.Label(self.parent_frame, text="Descripción:")
        self.label_descripcion.grid(row=3, column=0, pady=5,sticky="w")
        self.entry_descripcion = ttk.Entry(self.parent_frame,width=21)
        self.entry_descripcion.grid(row=3, column=1, pady=5)

        self.label_social_condition = ttk.Label(self.parent_frame, text="Lista:" )
        self.label_social_condition.grid(row=4, column=0, pady=5,sticky="w")
        self.social_condition = ttk.Combobox(
        self.parent_frame,
        state="readonly",
        values=["Cadena de Frio","Trazado A.N.M.A.T.","Psicotrópico","Ninguna"],width=19
         )
        self.social_condition.set("Ninguna")
        self.social_condition.grid(row=4, column=1, pady=5,sticky="w")

        self.button_add_stock = ttk.Button(self.parent_frame, text="Agregar Droga", command=self.add_stock,width=20)
        self.button_add_stock.grid(row=6, column=1, pady=10)

    def add_stock(self):
        monodroga = self.entry_monodroga.get()
        nombre_comercial = self.entry_nombre_comercial.get()
        descripcion = self.entry_descripcion.get()
        
        lab = self.entry_lab.get()

        if monodroga and nombre_comercial and descripcion and lab:
            # Aquí se agregarían los datos a la base de datos o se haría la lógica necesaria
            messagebox.showinfo("Éxito", "Nueva Droga agregada .")
        else:
            messagebox.showerror("Error", "Por favor complete todos los campos.")
            clear_entry(self.parent_frame)
            
