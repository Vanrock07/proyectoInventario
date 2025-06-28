from tkinter import StringVar
from tkinter import ttk, messagebox
import tkinter as tk


class UserDataFrame(ttk.Frame):
    def __init__(self, parent, controller2):  
        super().__init__(parent)                # Configuración de la ventana principal
        self.controller = controller2
        self.pack_propagate(False)
        self.grid_propagate(False)
        
        # Variables para almacenar los datos
        self.name = StringVar()
        self.document = StringVar()
        
        self._setup_ui_()
    
    def _setup_ui_(self):
        """Crea y organiza todos los elementos de la interfaz"""
        # Frame principal para mejor organización
        self.frame = ttk.Frame(self, padding="20")
        self.frame.pack(fill='both', expand=True)
        
        self.frame.columnconfigure(0, weight=1)
        self.frame.columnconfigure(1, weight=1)
        self.frame.columnconfigure(2, weight=1)
        self.frame.rowconfigure(99, weight=1) 
        
        # Nombre
        ttk.Label(self.frame, text="Nombre").grid(column=0, row=1, pady=(0, 5))
        ttk.Entry(self.frame, width=40, textvariable=self.name).grid(column=0, row=2, pady=(0, 10))
        
        # Documento
        ttk.Label(self.frame, text="Num Documento").grid(column=0, row=3, pady=(0, 5))
        ttk.Entry(self.frame, width=30, textvariable=self.document).grid(column=0, row=4, pady=(0, 10))
        
        ttk.Button(
            self.frame, 
            text="Atras", 
            command=self.controller.show_place_frame
            ).grid(row=100, column=0, padx=(10, 0), pady=10, sticky="sw")
        
        ttk.Button(
            self.frame, 
            text="Siguiente", 
            command=self.controller.guardarDatosUsuario
            ).grid(row=100, column=2, padx=(10, 0), pady=10, sticky="se")
        
    def get_user_data(self):
        """Método para manejar el guardado de datos"""  
        # self.controller.open_user_window()
        # self.window_Place.destroy()
        return {
            "nombre": self.name.get(),
            "documento": self.document.get(),
         }
    
    def mostrar_mensaje(self, titulo, mensaje):
        messagebox.showinfo(titulo, mensaje)    

