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
       # fondo         
        self.frame = ttk.Frame(self, padding="20",
                               style="Custom.TFrame")
        self.frame.pack(fill='both', expand=True) 
        
        # titulo
        tk.Label(self.frame, 
                text="Datos del usuario", 
                font=("Verdana", 18, "bold"),  # Fuente grande y negrita
                        foreground="#FFFFFF", # Color del texto
                bg="#008069", 
                borderwidth=0, 
                highlightthickness=0,
                width= 20,
                height= 2,).pack(side="top",padx=60, pady=10, anchor="e") 
        
       # Nombre
        ttk.Label(self.frame, style="TLabel", text="Nombre:").pack(side="top",anchor="w", padx=30, pady=(0, 2))
        ttk.Entry(self.frame, width=30, style="TEntry",textvariable=self.name, 
                  font=("Verdana", 11)).pack(side="top",anchor="w", padx=30, pady=(0, 0))
        
        # Documento
        ttk.Label(self.frame, style="TLabel", text="Documento:").pack(side="top",anchor="w", padx=30, pady=(10, 2))
        ttk.Entry(self.frame, width=30, style="TEntry",textvariable=self.document, 
                  font=("Verdana", 11)).pack(side="top",anchor="w", padx=30, pady=(0, 0))
        
        #botones    
        botones_frame = tk.Frame(self.frame, bg="#008069")
        botones_frame.pack(side="bottom", pady=40)

        ttk.Button(
            botones_frame, 
            text="Atras",
            style="TButton", 
            command=self.controller.show_place_frame
        ).pack(side="left", padx=20)  
        
        ttk.Button(
            botones_frame, 
            text    ="Siguiente",
            style="TButton", 
            command=self.controller.guardarDatosUsuario
            ).pack(side="left", padx=20) 
        
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

