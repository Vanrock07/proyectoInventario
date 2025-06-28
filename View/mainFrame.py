import tkinter as tk
from tkinter import ttk

class MainFrame:
    """Vista principal de la aplicación"""
    def __init__(self, controller2):
        self.controller = controller2
        self.root = tk.Tk()
        self.root.title("MVC - INVENTARIO CB")
        self.root.minsize(width=600, height=400)
        self.root.config(padx=50, pady=30)
        self.root.resizable(False, False)
        self._setup_ui()
        
    def _setup_ui(self):
        self.frame = ttk.Frame(self.root, padding="20")
        self.frame.pack()
        
    def mainloop(self):  #"""Inicia el bucle principal de la aplicación"""
        self.root.mainloop()