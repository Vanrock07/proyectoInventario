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
        # fondo         
        self.frame = ttk.Frame(self, padding="20",
                               style="Custom.TFrame")
        self.frame.pack(fill='both', expand=True) 
        
        # titulo
        tk.Label(self.frame, 
                text="Computador", 
                font=("Verdana", 18, "bold"),  # Fuente grande y negrita
                foreground="#FFFFFF", # Color del texto
                bg="#008069", 
                borderwidth=0, 
                highlightthickness=0,
                width= 20,
                height= 2,
                ).grid(row=0, column=0, columnspan=2, padx=70, pady=10, sticky="e")
        
        sub_frame = tk.Frame(self.frame, 
                             bg="#008069",
                             )
        sub_frame.grid(row=1, column=0, padx=(30,25), pady=3, sticky='w')
        
         # Tipo de equipo
        ttk.Label(sub_frame, text="Tipo de equipo:", style="TLabel"
                  ).grid(column=0, row=1, padx=0, pady=(0, 2), sticky='w')
        ttk.Entry(sub_frame, width=20, textvariable=self.tipo, style="TEntry",font=("Verdana", 11)
                  ).grid(column=0, row=2, padx=0, pady=(0, 0), sticky='w')
        
        # Marca
        ttk.Label(sub_frame, text="Marca:", style="TLabel"
                  ).grid(column=0, row=3, pady=(10, 2), sticky='w', padx=(0, 10))
        ttk.Entry(sub_frame, width=20, textvariable=self.marca, style="TEntry",font=("Verdana", 11)
                  ).grid(column=0, row=4, pady=(0, 0), sticky='w', padx=(0, 20))
        
        # Modelo
        ttk.Label(sub_frame, text="Modelo:", style="TLabel"
                  ).grid(column=0, row=5, pady=(10, 2), sticky='w', padx=(0, 10))
        ttk.Entry(sub_frame, width=20, textvariable=self.modelo, style="TEntry",font=("Verdana", 11)
                  ).grid(column=0, row=6, pady=(0, 0), sticky='w', padx=(0, 20))
        
          # Serial
        ttk.Label(sub_frame, text="Serial:", style="TLabel"
                  ).grid(column=0, row=7, pady=(10, 2), sticky='w', padx=(0, 10))
        ttk.Entry(sub_frame, width=20, textvariable=self.serial, style="TEntry",font=("Verdana", 11)
                  ).grid(column=0, row=8, pady=(0, 0), sticky='w', padx=(0, 20))
        
          # Activo
        ttk.Label(sub_frame, text="Activo:", style="TLabel"
                  ).grid(column=0, row=9, pady=(10, 2), sticky='w')
        ttk.Entry(sub_frame, width=20, textvariable=self.activo, style="TEntry",font=("Verdana", 11)
                  ).grid(column=0, row=10, pady=(0, 0), sticky='w')
        
        # sistema operativo
        ttk.Label(sub_frame, text="Sistema Operativo:", style="TLabel"
                  ).grid(column=1, row=1, pady=(0, 2), sticky='w')
        ttk.Entry(sub_frame, width=15, textvariable=self.so, style="TEntry",font=("Verdana", 11)
                  ).grid(column=1, row=2, pady=(0, 0), sticky='w')
        
        # self.so_var = tk.StringVar()
        # accesorios_opciones = ["Windows 10", "Windows 11"]
        # for idx, opcion in enumerate(accesorios_opciones):
        #     rbtn = ttk.Radiobutton(sub_frame, text=opcion, variable=self.so_var, value=opcion)
        #     rbtn.grid(column=1+idx, row=2, sticky='w', padx=(0,0))
        # self.so_var.set(accesorios_opciones[1])  # Valor por defecto
        
         # Tipo de disco
        ttk.Label(sub_frame, text="Tipo de disco:", style="TLabel"
                  ).grid(column=1, row=3, pady=(10, 2), sticky='w')
        ttk.Entry(sub_frame, width=15, textvariable=self.disco, style="TEntry",font=("Verdana", 11)
                  ).grid(column=1, row=4, pady=(0, 0), sticky='w')
        
         # Tamaño de disco
        ttk.Label(sub_frame, text="Tamaño del disco:", style="TLabel"
                  ).grid(column=1, row=5, pady=(10, 2), sticky='w')
        ttk.Entry(sub_frame, width=15, textvariable=self.tamano, style="TEntry",font=("Verdana", 11)
                  ).grid(column=1, row=6, pady=(0, 0), sticky='w')
        
         # Ram
        ttk.Label(sub_frame, text="Memoria RAM:", style="TLabel"
                  ).grid(column=1, row=7, pady=(10, 2), sticky='w')
        ttk.Entry(sub_frame, width=15, textvariable=self.ram, style="TEntry",font=("Verdana", 11)
                  ).grid(column=1, row=8, pady=(0, 0), sticky='w')
        
         # procesador
        ttk.Label(sub_frame, text="Procesador:", style="TLabel"
                  ).grid(column=1, row=9, pady=(10, 2), sticky='w')
        ttk.Entry(sub_frame, width=18, textvariable=self.procesador, style="TEntry",font=("Verdana", 11)
                  ).grid(column=1, row=10, pady=(0, 0), sticky='w')
        
        #botones    
        botones_frame = tk.Frame(self.frame, bg="#008069")
        botones_frame.grid(row=11, column=0, padx=(28, 0), pady=(93,40), sticky="s")

        ttk.Button(
            botones_frame, 
            text="Atras",
            style="TButton", 
            command=self.controller.show_gadgets_frame
        ).pack(side="left", padx=20)  
        
        ttk.Button(
            botones_frame, 
            text    ="Siguiente",
            style="TButton", 
            command=self.controller.guardarDatosPc
            ).pack(side="left", padx=20) 
        
        
        
        # Configurar valores por defecto
        self.tipo.set("LAPTOP")  # Valor por defecto
        self.marca.set("HP")        
        self.modelo.set("PROBOOK 440 G9")
        self.so.set("Windows 11")
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
            "sistema operativo": self.so.get()         
         }
    
    def mostrar_mensaje(self, titulo, mensaje):
        messagebox.showinfo(titulo, mensaje)    

 
    
