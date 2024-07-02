import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import tkinter as tk
from tkinter import messagebox
from ttkwidgets.autocomplete import AutocompleteEntry
import requests

# Simulación de datos de stock
STOCK_DATA = [
    {"monodroga": "Paracetamol", "nombre_comercial": "Tylenol", "descripcion": "Pain reliever", "lote": "A123", "vto": "2024-12-31", "lab": "Lab1"},
    {"monodroga": "Ibuprofen", "nombre_comercial": "Advil", "descripcion": "Anti-inflammatory", "lote": "B456", "vto": "2023-11-30", "lab": "Lab2"},
    # Agrega más datos según sea necesario
]

class ViewStockForm:
    def __init__(self, parent_frame):
        self.parent_frame = parent_frame
        self.create_widgets()

    def create_widgets(self):
        self.label_title = ttk.Label(self.parent_frame, text="Ver Stock", font=("Helvetica", 18))
        self.label_title.grid(row=0, column=0, columnspan=2, pady=10)

        self.label_search = ttk.Label(self.parent_frame, text="Buscar:")
        self.label_search.grid(row=1, column=0, pady=5)

        self.entry_search = AutocompleteEntry(self.parent_frame, completevalues=[item["monodroga"] for item in STOCK_DATA])
        self.entry_search.grid(row=1, column=1, pady=5)
        self.entry_search.bind("<KeyRelease>", self.update_listbox)

        self.listbox_results = tk.Listbox(self.parent_frame, height=10, width=50)
        self.listbox_results.grid(row=8, column=0, columnspan=2, pady=5)
        self.listbox_results.bind("<<ListboxSelect>>", self.display_selected_item)

        self.label_monodroga = ttk.Label(self.parent_frame, text="Monodroga:")
        self.label_monodroga.grid(row=2, column=3, pady=5)
        self.entry_monodroga = ttk.Entry(self.parent_frame, state="readonly")
        self.entry_monodroga.grid(row=2, column=4, pady=5)

        self.label_nombre_comercial = ttk.Label(self.parent_frame, text="Nombre Comercial:")
        self.label_nombre_comercial.grid(row=3, column=3, pady=5)
        self.entry_nombre_comercial = ttk.Entry(self.parent_frame, state="readonly")
        self.entry_nombre_comercial.grid(row=3, column=4, pady=5)

        self.label_descripcion = ttk.Label(self.parent_frame, text="Descripción:")
        self.label_descripcion.grid(row=4, column=3, pady=5)
        self.entry_descripcion = ttk.Entry(self.parent_frame, state="readonly")
        self.entry_descripcion.grid(row=4, column=4, pady=5)

        self.label_lote = ttk.Label(self.parent_frame, text="Lote:")
        self.label_lote.grid(row=5, column=3, pady=5)
        self.entry_lote = ttk.Entry(self.parent_frame, state="readonly")
        self.entry_lote.grid(row=5, column=4, pady=5)

        self.label_vto = ttk.Label(self.parent_frame, text="Vencimiento:")
        self.label_vto.grid(row=6, column=3, pady=5)
        self.entry_vto = ttk.Entry(self.parent_frame, state="readonly")
        self.entry_vto.grid(row=6, column=4, pady=5)

        self.label_lab = ttk.Label(self.parent_frame, text="Laboratorio:")
        self.label_lab.grid(row=7, column=3, pady=5)
        self.entry_lab = ttk.Entry(self.parent_frame, state="readonly")
        self.entry_lab.grid(row=7, column=4, pady=5)

        self.label_commercial_value = ttk.Label(self.parent_frame, text="Valor Comercial:")
        self.label_commercial_value.grid(row=8, column=3, pady=5)
        self.entry_commercial_value = ttk.Entry(self.parent_frame, state="readonly")
        self.entry_commercial_value.grid(row=8, column=4, pady=5)

        self.update_listbox()

    def update_listbox(self, event=None):
        search_term = self.entry_search.get().lower()
        self.listbox_results.delete(0, tk.END)
        for item in STOCK_DATA:
            if search_term in item["monodroga"].lower() or search_term in item["nombre_comercial"].lower():
                display_text = f'{item["monodroga"]}, {item["nombre_comercial"]}, {item["descripcion"]}, {item["lote"]}, {item["vto"]}, {item["lab"]}'
                self.listbox_results.insert(tk.END, display_text)

    def display_selected_item(self, event):
        selected_index = self.listbox_results.curselection()
        if selected_index:
            selected_item = self.listbox_results.get(selected_index)
            item_data = selected_item.split(", ")
            self.update_entry(self.entry_monodroga, item_data[0])
            self.update_entry(self.entry_nombre_comercial, item_data[1])
            self.update_entry(self.entry_descripcion, item_data[2])
            self.update_entry(self.entry_lote, item_data[3])
            self.update_entry(self.entry_vto, item_data[4])
            self.update_entry(self.entry_lab, item_data[5])

            drug_name = item_data[0]
            commercial_value = self.fetch_commercial_value(drug_name)
            self.update_entry(self.entry_commercial_value, commercial_value)

    def update_entry(self, entry, value):
        entry.config(state="normal")
        entry.delete(0, tk.END)
        entry.insert(0, value)
        entry.config(state="readonly")

    def fetch_commercial_value(self, drug_name):
        try:
            response = requests.get(f"https://api.drugprices.com/value?name={drug_name}")
            response.raise_for_status()
            data = response.json()
            return data.get("value", "###")
        except Exception:
            return "###"
