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
        # fondo         
        self.frame = ttk.Frame(self, padding="20",
                               style="Custom.TFrame")
        self.frame.pack(fill='both', expand=True) 

    # titulo
        tk.Label(self.frame, 
                text="Monitor", 
                font=("Verdana", 18, "bold"),  # Fuente grande y negrita
                        foreground="#FFFFFF", # Color del texto
                bg="#008069", 
                borderwidth=0, 
                highlightthickness=0,
                width= 20,
                height= 2,).pack(side="top",padx=60, pady=10, anchor="e") 
        
          # Marca
        ttk.Label(self.frame, style="TLabel", text="Marca:").pack(side="top",anchor="w", padx=30, pady=(0, 2))
        ttk.Entry(self.frame, width=20, style="TEntry",textvariable=self.marca, 
                  font=("Verdana", 11)).pack(side="top",anchor="w", padx=30, pady=(0, 0))
        
          # Serial
        ttk.Label(self.frame, style="TLabel", text="Serial:").pack(side="top",anchor="w", padx=30, pady=(10, 2))
        ttk.Entry(self.frame, width=20, style="TEntry",textvariable=self.serial, 
                  font=("Verdana", 11)).pack(side="top",anchor="w", padx=30, pady=(0, 0))
        
          # Activo
        ttk.Label(self.frame, style="TLabel", text="Activo:").pack(side="top",anchor="w", padx=30, pady=(10, 2))
        ttk.Entry(self.frame, width=20, style="TEntry",textvariable=self.activo, 
                  font=("Verdana", 11)).pack(side="top",anchor="w", padx=30, pady=(0, 0))
        
          #botones    
        botones_frame = tk.Frame(self.frame, bg="#008069")
        botones_frame.pack(side="bottom", pady=10)

        ttk.Button(
            botones_frame, 
            text="Atras",
            style="TButton", 
            command=self.controller.show_computer_frame
        ).pack(side="left", padx=20)  
        
        ttk.Button(
            botones_frame, 
            text    ="Terminar",
            style="TButton", 
            command=self.controller.guardarDatosMonitor
            ).pack(side="left", padx=20)
        
    def get_mon_data(self):
        """Método para manejar el guardado de datos"""
        return {
            "marcaM": self.marca.get(),
            "serialM": self.serial.get(),
            "activoM": self.activo.get(),         
         }
    
    def mostrar_mensaje(self, titulo, mensaje):
        messagebox.showinfo(titulo, mensaje) 

   

