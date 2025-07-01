# from tkinter import ttk


from tkinter import ttk
import tkinter as tk

class MenuFrame(ttk.Frame):
    """Vista principal de la aplicación"""
    def __init__(self, parent, controller2):
        super().__init__(parent)
        self.controller = controller2
        self.pack_propagate(False)
        self.grid_propagate(False)
        
        self._setup_ui() 
        
    def _setup_ui(self):  
        
    #fondo         
        self.frame = ttk.Frame(self, padding="20",
                               style="Custom.TFrame")
        self.frame.pack(fill='both', expand=True) 
                
    #titulo
        tk.Label(self.frame, 
                text="Bienvenido a Ikaro", 
                font=("Verdana", 20, "bold"),  # Fuente grande y negrita
                        foreground="#FFFFFF", # Color del texto
                bg="#008069", 
                borderwidth=0, 
                highlightthickness=0,
                width= 20,
                height= 2,).pack(side="top",padx=55, pady=10, anchor="e")    
          
    #botones    
        botones_frame = tk.Frame(self.frame, bg="#008069")
        botones_frame.pack(side="bottom", pady=40)

        ttk.Button(
            botones_frame, 
            text="Salir",
            style="TButton", 
            command=self.controller.main_view.root.destroy
        ).pack(side="left", padx=20)  
        
        ttk.Button(
            botones_frame, 
            text    ="Comenzar",
            style="TButton", 
            command=self.controller.show_place_frame
            ).pack(side="left", padx=20)      
        
        