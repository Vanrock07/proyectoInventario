import tkinter as tk
from tkinter import ttk

class MenuFrame(ttk.Frame):
    """Vista principal de la aplicación"""
    def __init__(self, parent, controller2):
        super().__init__(parent)
        self.controller = controller2
        self.pack_propagate(False)
        self.grid_propagate(False)
        
        self._setup_ui()
        
    def _setup_ui(self):       
        self.frame = ttk.Frame(self, padding="20")
        self.frame.pack(fill='both', expand=True) 
        
        self.frame.columnconfigure(0, weight=1)
        self.frame.columnconfigure(1, weight=1)
        self.frame.columnconfigure(2, weight=1)
        self.frame.rowconfigure(99, weight=1) 
        
        self.btn1_open = ttk.Button(
            self.frame, 
            text="Nuevo Registro",
          command= self.controller.show_place_frame   #//En este punto se genera un nuevo registro para la misma sede
        )                               # //navegar a la ventana de user con los datos de la sede ya cargados
        self.btn1_open.grid(row=100, column=2, padx=10, pady=10, sticky="se")
        
        self.btn2_open = ttk.Button(
            self.frame, 
            text="Salir",
            command= self.controller.main_view.root.destroy  
        )
        self.btn2_open.grid(row=100, column=0, padx=10, pady=10, sticky="sw")
        