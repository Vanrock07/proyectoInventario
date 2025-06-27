import tkinter as tk
from tkinter import ttk, messagebox
from tkinter import StringVar

class MonitorDataWindow:  
    def __init__(self, controller, anterior = None):
                # Configuración de la ventana principal
        self.controller = controller
        self.anterior = anterior
        self.window_Mon = tk.Toplevel()
       # self.window_Usr = Tk()
        self.window_Mon.title("MVC Datos del monitor")
        self.window_Mon.minsize(width=280, height=200)
        self.window_Mon.config(padx=50, pady=30)
        
        # Variables para almacenar los datos
        self.marca = StringVar()
        self.modelo = StringVar()
        self.serial = StringVar()
        self.activo = StringVar()
        
        self._setup_ui_()
    
    def _setup_ui_(self):
        """Crea y organiza todos los elementos de la interfaz"""
        # Frame principal para mejor organización
        self.frame = ttk.Frame(self.window_Mon, padding="20")
        self.frame.pack(fill='both', expand=True)
        
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
        
        ttk.Button(
            self.frame, 
            text="Anterior", 
            command=self.volver_atras
            ).grid(column=0, row=9)
        
        ttk.Button(
            self.frame, 
            text="Siguiente", 
            command=self.controller.guardarDatosMonitor
            ).grid(column=1, row=9)
     
    def volver_atras(self):
        self.window_Mon.destroy()
        if self.anterior:
            self.anterior.deiconify()
        
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

    def runUsr(self):
        """Inicia el bucle principal de la aplicación"""
        self.window_Mon.mainloop()  

