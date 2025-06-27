
from tkinter import StringVar
from tkinter import ttk, messagebox
import tkinter as tk


#constructor
class PlaceDataWindow:
    def __init__(self, controller):
        # Configuración de la ventana principal
        self.controller = controller
        self.window_Place = tk.Toplevel()
        self.window_Place.title("Datos de Sede")
        self.window_Place.minsize(width=280, height=200)
        self.window_Place.config(padx=50, pady=30)
        
        # Variables para almacenar los datos
        self.fecha = StringVar()
        self.city = StringVar()
        self.site = StringVar()
        self.cost_center = StringVar()
        self.ubicacion = StringVar()  # Variable para ubicación, si es necesario
        
        self._setup_ui()

#metodos de la clase        
    def _setup_ui(self):       
        """Crea y organiza todos los elementos de la interfaz"""
        # Frame principal para mejor organización
        self.frame = ttk.Frame(self.window_Place, padding="20")
        self.frame.pack(fill='both', expand=True)

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
            text="Guardar", 
            command=self.controller.guardarDatoSede
        ).grid(column=0, row=12) 
        
        self.fecha.set("27 de junio de 2025")  # Valor por defecto
        self.city.set("Bogotá")        
        self.site.set("Tintal")
        self.cost_center.set("11601")
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
        
    def runPlace(self):
        """Inicia el bucle principal de la aplicación"""
        self.window_Place.mainloop()
             