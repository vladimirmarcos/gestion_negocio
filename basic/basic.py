import tkinter as tk
class BasicMethods:
     def __init__(self):
         pass
    
     def delete_frame(self,frame_delete):
         if frame_delete:
            frame_delete.destroy()
    
     def clear_entry(self,frame):
         widgets = frame.winfo_children()
         j=0
         for widget in widgets:
            if isinstance(widget, tk.Entry):
                 widget.delete(0, tk.END)
                 if j==0:
                    widget.focus()
                    j+=1
         

            