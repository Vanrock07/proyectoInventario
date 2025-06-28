import tkinter as tk
from tkinter import ttk, messagebox
from tkinter import StringVar


class ComputerDataFrame(ttk.Frame):  
    def __init__(self, parent, controller2):
        super().__init__(parent)                # Configuración de la ventana principal
        self.controller = controller2
        self.pack_propagate(False)
        self.grid_propagate(False)
        
        # Variables para almacenar los datos
        self.tipo = StringVar()  # Valor por defecto
        self.marca = StringVar()
        self.modelo = StringVar()
        self.serial = StringVar()
        self.activo = StringVar()
        self.disco = StringVar()
        self.tamano = StringVar()
        self.ram = StringVar()
        self.procesador = StringVar()
        self.so = StringVar()
        
        self._setup_ui_()
    
    def _setup_ui_(self):
        """Crea y organiza todos los elementos de la interfaz"""
        # Frame principal para mejor organización
        self.frame = ttk.Frame(self, padding="20")
        self.frame.pack(fill='both', expand=True)
        
        self.frame.columnconfigure(0, weight=1)
        self.frame.columnconfigure(1, weight=1)
        self.frame.columnconfigure(2, weight=1)
        self.frame.rowconfigure(99, weight=1)
        
        # Tipo de equipo
        ttk.Label(self.frame, text="Tipo de equipo").grid(column=0, row=1, pady=(0, 5), sticky='w', padx=(0, 20))
        ttk.Entry(self.frame, width=30, textvariable=self.tipo).grid(column=0, row=2, pady=(0, 10), sticky='w', padx=(0, 20))
        # Marca
        ttk.Label(self.frame, text="Marca").grid(column=0, row=3, pady=(0, 5), sticky='w', padx=(0, 10))
        ttk.Entry(self.frame, width=30, textvariable=self.marca).grid(column=0, row=4, pady=(0, 10), sticky='w', padx=(0, 20))
        
        # Modelo
        ttk.Label(self.frame, text="Modelo").grid(column=0, row=5, pady=(0, 5), sticky='w', padx=(0, 10))
        ttk.Entry(self.frame, width=30, textvariable=self.modelo).grid(column=0, row=6, pady=(0, 10), sticky='w', padx=(0, 20))
        
          # Serial
        ttk.Label(self.frame, text="Serial").grid(column=0, row=7, pady=(0, 5), sticky='w', padx=(0, 10))
        ttk.Entry(self.frame, width=30, textvariable=self.serial).grid(column=0, row=8, pady=(0, 10), sticky='w', padx=(0, 20))
        
          # Activo
        ttk.Label(self.frame, text="Activo").grid(column=0, row=9, pady=(0, 5), sticky='w')
        ttk.Entry(self.frame, width=30, textvariable=self.activo).grid(column=0, row=10, pady=(0, 10), sticky='w')
        
        # sistema operativo
        ttk.Label(self.frame, text="Sistema Operativo").grid(column=1, row=1, pady=(0, 5), sticky='w')
        self.so_var = tk.StringVar()
        accesorios_opciones = ["Windows 10", "Windows 11"]
        for idx, opcion in enumerate(accesorios_opciones):
            rbtn = ttk.Radiobutton(self.frame, text=opcion, variable=self.so_var, value=opcion)
            rbtn.grid(column=1+idx, row=2, sticky='w')
        self.so_var.set(accesorios_opciones[0])  # Valor por defecto
        
         # Tipo de disco
        ttk.Label(self.frame, text="Tipo de disco").grid(column=1, row=3, pady=(0, 5), sticky='w')
        ttk.Entry(self.frame, width=15, textvariable=self.disco).grid(column=1, row=4, pady=(0, 10), sticky='w')
        
         # Tamaño de disco
        ttk.Label(self.frame, text="Tamaño del disco").grid(column=1, row=5, pady=(0, 5), sticky='w')
        ttk.Entry(self.frame, width=15, textvariable=self.tamano).grid(column=1, row=6, pady=(0, 10), sticky='w')
        
         # Ram
        ttk.Label(self.frame, text="Memoria RAM").grid(column=1, row=7, pady=(0, 5), sticky='w')
        ttk.Entry(self.frame, width=15, textvariable=self.ram).grid(column=1, row=8, pady=(0, 10), sticky='w')
        
         # procesador
        ttk.Label(self.frame, text="Procesador").grid(column=1, row=9, pady=(0, 5), sticky='w')
        ttk.Entry(self.frame, width=25, textvariable=self.procesador).grid(column=1, row=10, pady=(0, 10), sticky='w')
        
        ttk.Button(
            self.frame, 
            text="Atras", 
            command=self.controller.show_user_frame
            ).grid(row=100, column=0, padx=(10, 0), pady=10, sticky="sw")
        
        ttk.Button(
            self.frame, 
            text="Siguiente", 
            command=self.controller.guardarDatosPc
            ).grid(row=100, column=2, padx=(10, 0), pady=10, sticky="se")
        
        # Configurar valores por defecto
        self.tipo.set("LAPTOP")  # Valor por defecto
        self.marca.set("HP")        
        self.modelo.set("PROBOOK 440 G9")
        self.disco.set("SSD")
        self.tamano.set("512 GB")
        self.ram.set("16 GB")
        self.procesador.set("Intel Core i5 12th")    
        
    def get_pc_data(self):
        """Método para manejar el guardado de datos"""
        return {
            "tipo": self.tipo.get(),
            "marca": self.marca.get(),
            "modelo": self.modelo.get(),
            "serial": self.serial.get(),
            "activo": self.activo.get(), 
            "disco": self.disco.get(),
            "tamano": self.tamano.get(),  
            "ram": self.ram.get(), 
            "procesador": self.procesador.get(),
            "sistema operativo": self.so_var.get()         
         }
    
    def mostrar_mensaje(self, titulo, mensaje):
        messagebox.showinfo(titulo, mensaje)    

 
    
