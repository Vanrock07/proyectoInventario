
from tkinter import StringVar
from tkinter import ttk, messagebox
from datetime import datetime
import tkinter as tk

#constructor
class PlaceDataFrame(ttk.Frame):
    def __init__(self, parent, controller2):  
        super().__init__(parent)                # Configuración de la ventana principal
        self.controller = controller2
        self.pack_propagate(False)
        self.grid_propagate(False)

        # Variables para almacenar los datos
        self.fecha = StringVar()
        self.city = StringVar()
        self.site = StringVar()
        self.cost_center = StringVar()
        self.ubicacion = StringVar()  

        meses = [
                 "enero", "febrero", "marzo", "abril", "mayo", "junio",
                 "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"
]
        hoy = datetime.now()
        fecha_texto = f"{hoy.day} de {meses[hoy.month - 1]} de {hoy.year}"
        self.fecha.set(fecha_texto)
        
        self._setup_ui()

    #metodos de la clase        
    def _setup_ui(self):       
           
        #fondo         
        self.frame = ttk.Frame(self, padding="20",
                               style="Custom.TFrame")
        self.frame.pack(fill='both', expand=True) 
        
        # titulo
        tk.Label(self.frame, 
                text="Sede", 
                font=("Verdana", 18, "bold"),  # Fuente grande y negrita
                        foreground="#FFFFFF", # Color del texto
                bg="#008069", 
                borderwidth=0, 
                highlightthickness=0,
                width= 20,
                height= 2,).pack(side="top",padx=60, pady=10, anchor="e") 
           
        # Fecha
        ttk.Label(self.frame, style="TLabel", text="Fecha:").pack(side="top",anchor="w", padx=30, pady=(0, 2))
        ttk.Entry(self.frame, width=20, style="TEntry",textvariable=self.fecha, 
                  font=("Verdana", 11)).pack(side="top",anchor="w", padx=30, pady=(0, 0))
        
        # Ciudad
        ttk.Label(self.frame, style="TLabel", text="Ciudad:").pack(side="top",anchor="w", padx=30, pady=(10, 2))
        ttk.Entry(self.frame, width=20, style="TEntry",textvariable=self.city, 
                  font=("Verdana", 11)).pack(side="top",anchor="w", padx=30, pady=(0, 0))
        
        # Sede
        ttk.Label(self.frame, style="TLabel", text="Sede:").pack(side="top",anchor="w", padx=30, pady=(10, 2))
        ttk.Entry(self.frame, width=20, style="TEntry",textvariable=self.site, 
                  font=("Verdana", 11)).pack(side="top",anchor="w", padx=30, pady=(0, 0))
        
        # Centro de costos
        ttk.Label(self.frame, style="TLabel", text="Centro de costos:").pack(side="top",anchor="w", padx=30, pady=(10, 2))
        ttk.Entry(self.frame, width=20, style="TEntry",textvariable=self.cost_center, 
                  font=("Verdana", 11)).pack(side="top",anchor="w", padx=30, pady=(0, 0))
        
        # # Ubicación
        ttk.Label(self.frame, style="TLabel", text="Unidad:").pack(side="top",anchor="w", padx=30, pady=(10, 2))
        ttk.Entry(self.frame, width=20, style="TEntry",textvariable=self.ubicacion, 
                  font=("Verdana", 11)).pack(side="top",anchor="w", padx=30, pady=(0, 0))   
        
        #botones    
        botones_frame = tk.Frame(self.frame, bg="#008069")
        botones_frame.pack(side="bottom", pady=40)

        ttk.Button(
            botones_frame, 
            text="Atras",
            style="TButton", 
            command=self.controller.dataErase_advertisement
        ).pack(side="left", padx=15)  
        
        ttk.Button(
            botones_frame,
            text="Nuevo Registro",
            command=self.controller.new_data_insert
        ).pack(side="left", padx=15)
        
        ttk.Button(
            botones_frame, 
            text    ="Siguiente",
            style="TButton", 
            command=self.controller.guardarDatoSede
            ).pack(side="left", padx=15)    
     
    
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
        
             