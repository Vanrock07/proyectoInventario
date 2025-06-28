import tkinter as tk
from tkinter import ttk, messagebox
from tkinter import StringVar

class MonitorDataFrame(ttk.Frame):  
    def __init__(self, parent, controller2):
        super().__init__(parent)                # Configuración de la ventana principal
        self.controller = controller2
        self.pack_propagate(False)
        self.grid_propagate(False)
        
        # Variables para almacenar los datos
        self.marca = StringVar()
        self.modelo = StringVar()
        self.serial = StringVar()
        self.activo = StringVar()
        
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
        
        # Marca
        ttk.Label(self.frame, text="Marca").grid(column=0, row=1, pady=(0, 5))
        ttk.Entry(self.frame, width=40, textvariable=self.marca).grid(column=0, row=2, pady=(0, 10))
        
        # Modelo
        # ttk.Label(self.frame, text="Modelo").grid(column=0, row=3, pady=(0, 5))
        # ttk.Entry(self.frame, width=30, textvariable=self.modelo).grid(column=0, row=4, pady=(0, 10))
        
          # Serial
        ttk.Label(self.frame, text="Serial").grid(column=0, row=5, pady=(0, 5))
        ttk.Entry(self.frame, width=30, textvariable=self.serial).grid(column=0, row=6, pady=(0, 10))
        
          # Activo
        ttk.Label(self.frame, text="Activo").grid(column=0, row=7, pady=(0, 5))
        ttk.Entry(self.frame, width=30, textvariable=self.activo).grid(column=0, row=8, pady=(0, 10))
        
        tk.Button(
            self.frame, 
            text="Atras", 
            command=self.controller.show_computer_frame
            ).grid(row=100, column=0, padx=(10, 0), pady=10, sticky="sw")
         
        ttk.Button(
            self.frame, 
            text="Siguiente", 
            command=self.controller.guardarDatosMonitor
            ).grid(row=100, column=2, padx=(10, 0), pady=10, sticky="se")
        
    def get_mon_data(self):
        """Método para manejar el guardado de datos"""
        return {
            "marcaM": self.marca.get(),
           # "modeloM": self.modelo.get(),
            "serialM": self.serial.get(),
            "activoM": self.activo.get(),         
         }
    
    def mostrar_mensaje(self, titulo, mensaje):
        messagebox.showinfo(titulo, mensaje) 

   

