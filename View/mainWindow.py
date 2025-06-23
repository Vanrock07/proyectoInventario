import tkinter as tk
from tkinter import ttk

class MainWindow:
    """Vista principal de la aplicación"""
    def __init__(self, controller):
        self.controller = controller
        self.root = tk.Tk()
        self.root.title("MVC - INVENTARIO CB")
        self.root.minsize(width=400, height=300)
        self.root.config(padx=50, pady=30)
        self._setup_ui()
        
    def _setup_ui(self):
        self.frame = ttk.Frame(self.root, padding="20")
        self.frame.pack()
        
        self.btn_open = ttk.Button(
            self.frame, 
            text="Comenzar",      # //se ejecuta la primera vez que se abre el aplicativo
            command=self.controller.open_place_window
        )
        self.btn_open.pack(pady=10)
        
        self.btn2_open = ttk.Button(
            self.frame, 
            text="Nuevo Registro",
         #  command= self.root.destroy    //En este punto se genera un nuevo registro para la misma sede
        )                               # //navegar a la ventana de user con los datos de la sede ya cargados
        self.btn2_open.pack(pady=10)
        
        self.btn3_open = ttk.Button(
            self.frame, 
            text="Salir",
            command= self.root.destroy
        )
        self.btn3_open.pack(pady=10)
        
        self.btn4_open = ttk.Button(
            self.frame, 
            text="Generar Acta",
            command = self.controller.generar_acta  # //navegar a la ventana de acta con los datos de la sede ya cargados
        )
        self.btn4_open.pack(pady=10)
        
        self.label_data = ttk.Label(self.frame, text="")
        self.label_data.pack(pady=10)
        
    def update_data_display(self, data):
        self.label_data.config(text=f"Dato recibido: {data}")
        
    def mainloop(self):
        """Inicia el bucle principal de la aplicación"""
        self.root.mainloop()