import tkinter as tk
def clear_entry(frame):
         widgets = frame.winfo_children()
         j=0
         for widget in widgets:
            if isinstance(widget, tk.Entry):
                 widget.delete(0, tk.END)
                 if j==0:
                    widget.focus()
                    j+=1
         

            