import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk


class MainFrame():
    """Vista principal de la aplicación"""
    def __init__(self, controller2):
        self.controller = controller2
        self.root = tk.Tk()
        self.root.title("MVC - INVENTARIO CB")
        self.root.minsize(width=800, height=400)
        self.root.config(bg="#365d83")
        self.root.resizable(False, False)
        self.root.iconbitmap("Media\Corchetes.ico")
 
        
        self.style = ttk.Style() 
        self.style.configure("Custom.Title",
                            font=("Verdana", 18, "bold"),  # Fuente grande y negrita
                            foreground="#FFFFFF", # Color del texto
                            bg="#008069", 
                            borderwidth=0, 
                            highlightthickness=0,
                            width= 20,
                            height= 2,)
        
        self.style = ttk.Style()
        self.style.configure("Custom.TFrame", 
                    background="#008069", 
                    borderwidth=0, 
                    relief="flat")
        
        self.style = ttk.Style()
        self.style.configure("TButton", 
                foreground="black",  # Color del texto
                background="#365d83",  # Color de fondo (no aplica en todos los temas)
                font=("Verdana", 12),  # Fuente
                padding=5,  # Espacio interno
                relief="raised")  # Efecto del borde (raised, flat, etc.)
        
        self.style2 = ttk.Style()
        self.style2.configure("TLabel", 
                foreground="black",  # Color del texto
                background="#008069",  # Color de fondo (no aplica en todos los temas)
                font=("Verdana", 12),  # Fuente
                padding=0,  # Espacio interno
                )  # Efecto del borde (raised, flat, etc.)
            
        self.style3 = ttk.Style()
        self.style3.configure("TEntry", 
                foreground="black",  # Color del texto
                background="#FFFFFF",  # Color de fondo (no aplica en todos los temas)
                font=("Verdana", 12,),  # Fuente
                padding=0,  # Espacio interno
                )  # Efecto del borde (raised, flat, etc.)           
        self._setup_ui()
       
    def _setup_ui(self):
                 
    #Imagen    
        try:
            imagen = Image.open("Media\LogoCB2.png")  # Cambia por tu archivo
            
            new_width = 300 
            width_percent = (new_width / float(imagen.size[0]))
            new_height = int((float(imagen.size[1]) * float(width_percent)))
            
            resized_img = imagen.resize((new_width, new_height), Image.LANCZOS)
            self.img_tk = ImageTk.PhotoImage(resized_img)  # Guardar referencia
             
            # Mostrar la imagen en un Label dentro del Frame
            tk.Label(self.root, image=self.img_tk, 
                     bg="#365d83", borderwidth=0, 
                     highlightthickness=0).pack(side="left", anchor="w")
              
        except Exception as e:
            print("Error al cargar la imagen:", e)
            ttk.Label(self, text="Imagen no encontrada").pack()
            

    def mainloop(self):  #"""Inicia el bucle principal de la aplicación"""
        self.root.mainloop()       
            