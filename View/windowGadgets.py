
from tkinter import StringVar
from tkinter import ttk, messagebox
import tkinter as tk

class GadgetsDataWindow:
    def __init__(self, controller, anterior = None):
        # Configuración de la ventana principal
        self.controller = controller
        self.anterior = anterior
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
        #ttk.Entry(self.frame, width=40).grid(column=0, row=4, pady=(0, 10))
        self.observaciones = tk.Text(self.frame, width=40, height=4)
        self.observaciones.grid(column=0, row=10, pady=(0, 10))
       
        ttk.Button(
            self.frame, 
            text="Atras", 
            command=self.volver_atras
            ).grid(column=0, row=11)
        
        # Botón de guardar
        ttk.Button(
            self.frame, 
            text="Guardar", 
            command=self.controller.guardarDatosGadgets
        ).grid(column=1, row=11) 
           
    def volver_atras(self):
        self.window_Gdt.destroy()
        if self.anterior:
            self.anterior.deiconify()
    
    def get_gadget_data(self):
        """Método para manejar el guardado de datos"""
        accesorios_seleccionados = [nombre for nombre, var in self.check_vars.items() if var.get()]
        return {
            "accesorios": f"{', '.join(accesorios_seleccionados)}, {self.gadgets.get()}",
           # "otros": self.gadgets.get(),
            "observaciones": self.observaciones.get("1.0", tk.END).strip()
         }
    
    def mostrar_mensaje(self, titulo, mensaje):
        messagebox.showinfo(titulo, mensaje)
  
    def runGadgets(self):
        """Inicia el bucle principal de la aplicación"""
        self.window_Gdt.mainloop()