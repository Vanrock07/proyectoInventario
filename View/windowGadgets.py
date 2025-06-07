
from tkinter import StringVar
from tkinter import ttk, messagebox
import tkinter as tk

class GadgetsDataWindow:
    def __init__(self, controller):
        # Configuración de la ventana principal
        self.controller = controller
        self.window_Gdt = tk.Toplevel()
        self.window_Gdt.title("Accesorios")
        self.window_Gdt.minsize(width=280, height=200)
        self.window_Gdt.config(padx=50, pady=30)
        
        # Variables para almacenar los datos
        self.gadgets = StringVar()
        
        self._setup_ui()
        
        # Crear los widgets
        #self.create_widgets()
        
    def _setup_ui(self):
        """Crea y organiza todos los elementos de la interfaz"""
        # Frame principal para mejor organización
        self.frame = ttk.Frame(self.window_Gdt, padding="20")
        self.frame.pack(fill='both', expand=True)
        
        # Accesorios
        ttk.Label(self.frame, text="Accesorios").grid(column=0, row=1, pady=(0, 5))
        ttk.Entry(self.frame, width=40, textvariable=self.gadgets).grid(column=0, row=2, pady=(0, 10))
       
        # Botón de guardar
        ttk.Button(
            self.frame, 
            text="Guardar", 
            command=self.controller.guardarDatosGadgets
        ).grid(column=0, row=7) 
        
    def get_gadget_data(self):
        """Método para manejar el guardado de datos"""
        return {
            "accesorios": self.gadgets.get(),       
         }
    
    def mostrar_mensaje(self, titulo, mensaje):
        messagebox.showinfo(titulo, mensaje)
  
    def runGadgets(self):
        """Inicia el bucle principal de la aplicación"""
        self.window_Gdt.mainloop()