
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
    # fondo         
        self.frame = ttk.Frame(self, padding="20",
                               style="Custom.TFrame")
        self.frame.pack(fill='both', expand=True) 
        
    # titulo
        tk.Label(self.frame, 
                text="Accesorios", 
                font=("Verdana", 18, "bold"),  # Fuente grande y negrita
                        foreground="#FFFFFF", # Color del texto
                bg="#008069", 
                borderwidth=0, 
                highlightthickness=0,
                width= 20,
                height= 2,).pack(side="top",padx=60, pady=10, anchor="e") 
        
    # Estilo para los checboxes
        style = ttk.Style()
        style.configure(
                "Accesorio.TCheckbutton",
                    font=("Verdana", 12),
                    foreground="#000000",
                    background="#008069" 
                    )  
           
    # Accesorios
        self.check_vars = {}
        accesorios_opciones = ["Guaya", "Maleta", "Teclado", "Mouse", "Base", "Diadema"]
        for idx, opcion in enumerate(accesorios_opciones):
            var = tk.BooleanVar()
            chk = ttk.Checkbutton(self.frame, text=opcion, style="Accesorio.TCheckbutton", variable=var)
            chk.pack(side="top", anchor='w', padx=30, pady=(2, 2))
            self.check_vars[opcion] = var
            
        # Otros accesorios
        ttk.Label(self.frame, style="TLabel", text="Otros:").pack(side="top",anchor="w", padx=30, pady=(10, 2))
        ttk.Entry(self.frame, width=30, style="TEntry",textvariable=self.gadgets, 
                  font=("Verdana", 11)).pack(side="top",anchor="w", padx=30, pady=(0, 0))   
        
        #observaciones
        ttk.Label(self.frame, text="Observaciones").pack(side="top",anchor="w", padx=30, pady=(10, 2))
        self.observaciones = tk.Text(self.frame, width=40, height=4)
        self.observaciones.pack(side="top",anchor="w", padx=30, pady=(0, 2))
       
        #botones    
        botones_frame = tk.Frame(self.frame, bg="#008069")
        botones_frame.pack(side="bottom", pady=10)

        ttk.Button(
            botones_frame, 
            text="Atras",
            style="TButton", 
            command=self.controller.show_user_frame
        ).pack(side="left", padx=20)  
        
        ttk.Button(
            botones_frame, 
            text    ="Siguiente",
            style="TButton", 
            command=self.controller.guardarDatosGadgets
            ).pack(side="left", padx=20)  
        
           
    def get_gadgets_data(self):
        """Método para manejar el guardado de datos"""
        accesorios_seleccionados = [nombre for nombre, var in self.check_vars.items() if var.get()]
        return {
            "accesorios": f"{', '.join(accesorios_seleccionados)}, {self.gadgets.get()}",
            "observaciones": self.observaciones.get("1.0", tk.END).strip()
         }
    
    def mostrar_mensaje(self, titulo, mensaje):
        messagebox.showinfo(titulo, mensaje)
  
  