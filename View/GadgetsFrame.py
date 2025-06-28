
from tkinter import StringVar
from tkinter import ttk, messagebox
import tkinter as tk

class GadgetsDataFrame(ttk.Frame):
    def __init__(self, parent, controller2):
        super().__init__(parent)                # Configuración de la ventana principal
        self.controller = controller2
        self.pack_propagate(False)
        self.grid_propagate(False)
        
        # Variables para almacenar los datos
        self.gadgets = StringVar()
        
        self._setup_ui()
        
        # Crear los widgets
        #self.create_widgets()
        
    def _setup_ui(self):
        """Crea y organiza todos los elementos de la interfaz"""
        # Frame principal para mejor organización
        self.frame = ttk.Frame(self, padding="20")
        self.frame.pack(fill='both', expand=True)
        
        self.frame.columnconfigure(0, weight=1)
        self.frame.columnconfigure(1, weight=1)
        self.frame.columnconfigure(2, weight=1)
        self.frame.rowconfigure(99, weight=1)
        
        # Accesorios
        self.check_vars = {}
        accesorios_opciones = ["Guaya", "Maleta", "Teclado", "Mouse", "Base", "Diadema"]
        for idx, opcion in enumerate(accesorios_opciones):
            var = tk.BooleanVar()
            chk = ttk.Checkbutton(self.frame, text=opcion, variable=var)
            chk.grid(column=0, row=1+idx, sticky='w')
            self.check_vars[opcion] = var
        # Otros accesorios
        ttk.Label(self.frame, text="Otros").grid(column=0, row=7, pady=(0, 5))
        ttk.Entry(self.frame, width=40, textvariable=self.gadgets).grid(column=0, row=8, pady=(0, 10))    
        #observaciones
        ttk.Label(self.frame, text="Observaciones").grid(column=0, row=9, pady=(0, 5))
        self.observaciones = tk.Text(self.frame, width=40, height=4)
        self.observaciones.grid(column=0, row=10, pady=(0, 10))
       
        ttk.Button(
            self.frame, 
            text="Atras", 
            command=self.controller.show_monitor_frame
        ).grid(row=100, column=0, padx=(10, 0), pady=10, sticky="sw") 

        tk.Button(
            self.frame, 
            text="Terminar", 
            command=self.controller.guardarDatosGadgets  #implementar anuncio de confirmacion de datos
        ).grid(row=100, column=2, padx=(10, 0), pady=10, sticky="se") 
        
           
    def get_gadgets_data(self):
        """Método para manejar el guardado de datos"""
        accesorios_seleccionados = [nombre for nombre, var in self.check_vars.items() if var.get()]
        return {
            "accesorios": f"{', '.join(accesorios_seleccionados)}, {self.gadgets.get()}",
            "observaciones": self.observaciones.get("1.0", tk.END).strip()
         }
    
    def mostrar_mensaje(self, titulo, mensaje):
        messagebox.showinfo(titulo, mensaje)
  
  