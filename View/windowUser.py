from tkinter import StringVar
from tkinter import ttk, messagebox
import tkinter as tk


class UserDataWindow:
    def __init__(self, controller):
        # Configuración de la ventana principal
        self.controller = controller
        self.window_Usr = tk.Toplevel()
        self.window_Usr.title("Datos de usuario")
        self.window_Usr.minsize(width=280, height=200)
        self.window_Usr.config(padx=50, pady=30)
        
        # Variables para almacenar los datos
        self.name = StringVar()
        self.document = StringVar()
        
        self._setup_ui_()
    
    def _setup_ui_(self):
        """Crea y organiza todos los elementos de la interfaz"""
        # Frame principal para mejor organización
        self.frame = ttk.Frame(self.window_Usr, padding="20")
        self.frame.pack(fill='both', expand=True)
        
        # Nombre
        ttk.Label(self.frame, text="Nombre").grid(column=0, row=1, pady=(0, 5))
        ttk.Entry(self.frame, width=40, textvariable=self.name).grid(column=0, row=2, pady=(0, 10))
        
        # Documento
        ttk.Label(self.frame, text="Num Documento").grid(column=0, row=3, pady=(0, 5))
        ttk.Entry(self.frame, width=30, textvariable=self.document).grid(column=0, row=4, pady=(0, 10))
        
        ttk.Button(
            self.frame, 
            text="Guardar", 
            command=self.controller.guardarDatosUsuario
            ).grid(column=0, row=7)
        
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

    def runUsr(self):
        """Inicia el bucle principal de la aplicación"""
        self.window_Usr.mainloop()    
               