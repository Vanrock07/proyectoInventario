from tkinter import ttk
import tkinter as tk

class SheetWindow:
    def __init__(self, controller):
        # Configuración de la ventana principal
        self.controller = controller
        self.window_Sheet = tk.Toplevel()
        self.window_Sheet.title("MVC Generar Acta")
        self.window_Sheet.minsize(width=280, height=200)
        self.window_Sheet.config(padx=50, pady=30)
        
        self._setup_ui()
             
    def _setup_ui(self):
        """Crea y organiza todos los elementos de la interfaz"""
        # Frame principal para mejor organización
        self.frame = ttk.Frame(self.window_Sheet, padding="20")
        self.frame.pack(fill='both', expand=True)

        # Botónes
        self.btn_open = ttk.Button(
            self.frame, 
            text="Generar Acta",
         #   command=controller.Generar_Acta
        )
        self.btn_open.pack(pady=10)
        
        self.btn2_open = ttk.Button(
            self.frame, 
            text="Salir",
            command= self.window_Sheet.destroy
        )
        self.btn2_open.pack(pady=10)
        
        self.label_data = ttk.Label(self.frame, text="")
        self.label_data.pack(pady=10)
        
    def update_data_display(self, data):
        self.label_data.config(text=f"Dato recibido: {data}")
        
    def mainloop(self):
        """Inicia el bucle principal de la aplicación"""
        self.root.mainloop()