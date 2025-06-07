import tkinter as tk
from tkinter import ttk, messagebox
from tkinter import StringVar

class ComputerDataWindow:  
    def __init__(self, controller):
                # Configuración de la ventana principal
        self.controller = controller
        self.window_Pc = tk.Toplevel()
       # self.window_Usr = Tk()
        self.window_Pc.title("MVC Datos del equipo")
        self.window_Pc.minsize(width=280, height=200)
        self.window_Pc.config(padx=50, pady=30)
        
        # Variables para almacenar los datos
        self.marca = StringVar()
        self.modelo = StringVar()
        self.serial = StringVar()
        self.activo = StringVar()
        
        self._setup_ui_()
    
    def _setup_ui_(self):
        """Crea y organiza todos los elementos de la interfaz"""
        # Frame principal para mejor organización
        self.frame = ttk.Frame(self.window_Pc, padding="20")
        self.frame.pack(fill='both', expand=True)
        
        # Marca
        ttk.Label(self.frame, text="Marca").grid(column=0, row=1, pady=(0, 5))
        ttk.Entry(self.frame, width=40, textvariable=self.marca).grid(column=0, row=2, pady=(0, 10))
        
        # Modelo
        ttk.Label(self.frame, text="Modelo").grid(column=0, row=3, pady=(0, 5))
        ttk.Entry(self.frame, width=30, textvariable=self.modelo).grid(column=0, row=4, pady=(0, 10))
        
          # Serial
        ttk.Label(self.frame, text="Serial").grid(column=0, row=5, pady=(0, 5))
        ttk.Entry(self.frame, width=30, textvariable=self.serial).grid(column=0, row=6, pady=(0, 10))
        
          # Activo
        ttk.Label(self.frame, text="Activo").grid(column=0, row=7, pady=(0, 5))
        ttk.Entry(self.frame, width=30, textvariable=self.activo).grid(column=0, row=8, pady=(0, 10))
        
        ttk.Button(
            self.frame, 
            text="Guardar", 
            command=self.controller.guardarDatosPc
            ).grid(column=0, row=9)
        
    def get_pc_data(self):
        """Método para manejar el guardado de datos"""
        return {
            "marca": self.marca.get(),
            "modelo": self.modelo.get(),
            "seria;": self.serial.get(),
            "activo": self.activo.get(),         
         }
    
    def mostrar_mensaje(self, titulo, mensaje):
        messagebox.showinfo(titulo, mensaje)    


    def runUsr(self):
        """Inicia el bucle principal de la aplicación"""
        self.window_Pc.mainloop()  
      
    
