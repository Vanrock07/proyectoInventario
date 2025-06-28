
from tkinter import StringVar
from tkinter import ttk, messagebox
import tkinter as tk


#constructor
class PlaceDataFrame(ttk.Frame):
    def __init__(self, parent, controller2, anterior = None):  
        super().__init__(parent)                # Configuración de la ventana principal
        self.controller = controller2
        self.anterior = anterior
        self.pack_propagate(False)
        self.grid_propagate(False)

        # Variables para almacenar los datos
        self.fecha = StringVar()
        self.city = StringVar()
        self.site = StringVar()
        self.cost_center = StringVar()
        self.ubicacion = StringVar()  
        
        self._setup_ui()

    #metodos de la clase        
    def _setup_ui(self):       
        """Crea y organiza todos los elementos de la interfaz"""
           
        self.frame = ttk.Frame(self, padding="20")  # Frame principal para mejor organización
        self.frame.pack(fill='both', expand=False)
        
        self.frame.columnconfigure(0, weight=1)
        self.frame.columnconfigure(1, weight=1)
        self.frame.columnconfigure(2, weight=1)
        self.frame.rowconfigure(99, weight=1) 

        # Fecha
        ttk.Label(self.frame, text="Fecha").grid(column=0, row=2, pady=(0, 5))
        ttk.Entry(self.frame, width=30, textvariable=self.fecha).grid(column=0, row=3, pady=(0, 10))
        # Ciudad
        ttk.Label(self.frame, text="Ciudad").grid(column=0, row=4, pady=(0, 5))
        ttk.Entry(self.frame, width=30, textvariable=self.city).grid(column=0, row=5, pady=(0, 10))
        # Sede
        ttk.Label(self.frame, text="Sede").grid(column=0, row=6, pady=(0, 5))
        ttk.Entry(self.frame, width=30, textvariable=self.site).grid(column=0, row=7, pady=(0, 10))
        # Centro de costos
        ttk.Label(self.frame, text="Centro de costos").grid(column=0, row=8, pady=(0, 5))
        ttk.Entry(self.frame, width=30, textvariable=self.cost_center).grid(column=0, row=9, pady=(0, 15))
        # Ubicación
        ttk.Label(self.frame, text="Ubicacion").grid(column=0, row=10, pady=(0, 5))
        ttk.Entry(self.frame, width=30, textvariable=self.ubicacion).grid(column=0, row=11, pady=(0, 15))
        # Botón de guardar
  
        ttk.Button(
            self.frame,
            text="Atras",
            command=self.controller.dataErase_advertisement
        ).grid(row=100, column=0, padx=(10, 0), pady=10, sticky="sw")
        
        ttk.Button(
            self.frame,
            text="Siguiente",
            command=self.controller.guardarDatoSede
        ).grid(row=100, column=2, padx=(10, 0), pady=10, sticky="se")        
        
        self.fecha.set("1 de julio de 2025")  # Valor por defecto
        self.city.set("Bogotá")        
        self.site.set("Tintal")
        self.ubicacion.set("Oficina Tintal")
    
    def get_place_data(self):

        return {
            "fecha": self.fecha.get(),
            "ciudad": self.city.get(),
            "sede": self.site.get(),
            "centro de costos": self.cost_center.get(),
            "ubicacion": self.ubicacion.get()
         }
        
    def mostrar_mensaje(self, titulo, mensaje):
        messagebox.showinfo(titulo, mensaje)
        
             