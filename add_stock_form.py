import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import messagebox

class AddStockForm:
    def __init__(self, parent_frame):
        self.parent_frame = parent_frame
        self.create_widgets()

    def create_widgets(self):
        self.label_title = ttk.Label(self.parent_frame, text="Agregar Stock", font=("Helvetica", 18))
        self.label_title.grid(row=0, column=0, columnspan=2, pady=10)

        self.label_monodroga = ttk.Label(self.parent_frame, text="Monodroga:")
        self.label_monodroga.grid(row=1, column=0, pady=5)
        self.entry_monodroga = ttk.Entry(self.parent_frame)
        self.entry_monodroga.grid(row=1, column=1, pady=5)

        self.label_nombre_comercial = ttk.Label(self.parent_frame, text="Nombre Comercial:")
        self.label_nombre_comercial.grid(row=2, column=0, pady=5)
        self.entry_nombre_comercial = ttk.Entry(self.parent_frame)
        self.entry_nombre_comercial.grid(row=2, column=1, pady=5)

        self.label_descripcion = ttk.Label(self.parent_frame, text="Descripción:")
        self.label_descripcion.grid(row=3, column=0, pady=5)
        self.entry_descripcion = ttk.Entry(self.parent_frame)
        self.entry_descripcion.grid(row=3, column=1, pady=5)

        self.label_lote = ttk.Label(self.parent_frame, text="Lote:")
        self.label_lote.grid(row=4, column=0, pady=5)
        self.entry_lote = ttk.Entry(self.parent_frame)
        self.entry_lote.grid(row=4, column=1, pady=5)

        self.label_lab = ttk.Label(self.parent_frame, text="Laboratorio:")
        self.label_lab.grid(row=5, column=0, pady=5)
        self.entry_lab = ttk.Entry(self.parent_frame)
        self.entry_lab.grid(row=5, column=1, pady=5)

        self.label_vto = ttk.Label(self.parent_frame, text="Vto:")
        self.label_vto.grid(row=6, column=0, pady=5)
        self.entry_vto = ttk.Entry(self.parent_frame)
        self.entry_vto.grid(row=6, column=1, pady=5)

        self.button_add_stock = ttk.Button(self.parent_frame, text="Agregar Stock", command=self.add_stock)
        self.button_add_stock.grid(row=7, column=0, columnspan=2, pady=10)

    def add_stock(self):
        monodroga = self.entry_monodroga.get()
        nombre_comercial = self.entry_nombre_comercial.get()
        descripcion = self.entry_descripcion.get()
        lote = self.entry_lote.get()
        lab = self.entry_lab.get()
        vto = self.entry_vto.get()

        if monodroga and nombre_comercial and descripcion and lote and lab and vto:
            # Aquí deberías agregar la lógica para agregar el stock a la base de datos
            print("Stock agregado:", monodroga, nombre_comercial, descripcion, lote, lab, vto)
            messagebox.showinfo("Éxito", "Stock agregado exitosamente.")
        else:
            messagebox.showerror("Error", "Por favor complete todos los campos correctamente.")
