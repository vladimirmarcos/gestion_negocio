import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from login import LoginScreen
from db import create_db

def main():
    create_db()
    root = ttk.Window(themename="darkly")
    root.state('zoomed')  
    app = LoginScreen(root)
    root.mainloop()

if __name__ == "__main__":
    main()
