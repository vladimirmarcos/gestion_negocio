import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from login import LoginScreen


def main():
    
    root = ttk.Window(themename="darkly")
    root.state('zoomed')  
    app = LoginScreen(root)
    root.mainloop()

if __name__ == "__main__":
    main()