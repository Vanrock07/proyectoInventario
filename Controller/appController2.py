from View.mainFrame import MainFrame 
from View.menuFrame import MenuFrame
from View.PlaceFrame import PlaceDataFrame
from View.UserFrame import UserDataFrame
from View.ComputerFrame import ComputerDataFrame
from View.MonitorFrame import MonitorDataFrame
from View.GadgetsFrame import GadgetsDataFrame
from Model.dataPlace import modeloDatos
from Model.saveData import ExportData
from Model.generarFormato import saveDataToPDF

from tkinter import messagebox
from utils.path import resource_path


class AppController2:
    def __init__(self):
        self.excel_path = resource_path("files2/datosMantenimiento1.xlsx") # Ruta al archivo Excel
        self.pdf_path = resource_path("files2/FORMATO MMTO CBOLIVAR.pdf") # Ruta al archivo PDF
        self.current_frame = None
        self.frames = {}
        self.model = modeloDatos() 
        self.main_view = MainFrame(self)
        self.show_menu_frame()

# CONTROL DE BORRAR ESCONDER Y MOSTRAR LOS FORMULARIOS        
    def clear_all_frames(self):
        for frame in self.frames.values():
            frame.destroy()
        self.frames.clear()
    
    def new_data_insert(self):
        for key in list(self.frames.keys()):
            if key != 'place':
                self.frames[key].destroy()
                del self.frames[key]
        self.current_frame.mostrar_mensaje("Atención","Se ha limpiado el formulario")
                                                 
      #  self.show_user_frame()        
        
    def dataErase_advertisement(self):
        conf = messagebox.askyesno("Advertencia",
                                   "Todos los datos serán borrados. \n desea continuar?")
        if conf:
            self.show_menu_frame() 
   
    def hide_frame(self):
        if self.current_frame is not None:
            self.current_frame.pack_forget()
            self.current_frame = None
            
    def show_menu_frame(self):
        self.clear_all_frames()
        self.current_frame = MenuFrame(self.main_view.root, self)
        self.current_frame.pack(fill='both', expand=True)

    def show_place_frame(self):
        if self.current_frame is not None:
                self.hide_frame()
        if 'place' not in self.frames:
            self.frames['place'] = PlaceDataFrame(self.main_view.root, self)
        self.current_frame = self.frames['place']
        self.current_frame.pack(fill='both', expand=True)
         
    def show_user_frame(self):
        if self.current_frame is not None:
                self.hide_frame()
        if 'user' not in self.frames:
            self.frames['user'] = UserDataFrame(self.main_view.root, self)
        self.current_frame = self.frames['user']
        self.current_frame.pack(fill='both', expand=True)

    def show_computer_frame(self):
        if self.current_frame is not None:
                self.hide_frame()
        if 'computer' not in self.frames:
            self.frames['computer'] = ComputerDataFrame(self.main_view.root, self)
        self.current_frame = self.frames['computer']
        self.current_frame.pack(fill='both', expand=True)

    def show_monitor_frame(self):
        if self.current_frame is not None:
                self.hide_frame()
        if 'monitor' not in self.frames:
            self.frames['monitor'] = MonitorDataFrame(self.main_view.root, self)
        self.current_frame = self.frames['monitor']
        self.current_frame.pack(fill='both', expand=True)

    def show_gadgets_frame(self):
        if self.current_frame is not None:
                self.hide_frame()
        if 'gadgets' not in self.frames:
            self.frames['gadgets'] = GadgetsDataFrame(self.main_view.root, self)
        self.current_frame = self.frames['gadgets']
        self.current_frame.pack(fill='both', expand=True)

# CONTROL DE GUARDADO DE DATOS

    def guardarDatoSede(self):
        datos = self.current_frame.get_place_data()
        
        if not all(datos.values()):
            self.current_frame.mostrar_mensaje("Error", "Todos los campos son obligatorios")
            return
        
        if self.model.saveData(datos):
            # self.current_frame.mostrar_mensaje("Éxito", f"Datos guardados") # :\n{self.model.data}
            self.show_user_frame()          

    def guardarDatosUsuario(self):  
        datos = self.current_frame.get_user_data()
        
        if not all(datos.values()):
            self.current_frame.mostrar_mensaje("Error", "Todos los campos son obligatorios")
            return
        
        if self.model.saveData(datos):
            # self.current_frame.mostrar_mensaje("Éxito", f"Datos guardados") # \n{self.model.data}
            self.show_gadgets_frame()
    
    def guardarDatosGadgets(self):
        datos = self.current_frame.get_gadgets_data()
        # if not all(datos.values()):
        #     self.current_frame.mostrar_mensaje("Error", "Todos los campos son obligatorios")
        #     return
        if self.model.saveData(datos):
           #  self.current_frame.mostrar_mensaje("Éxito", f"Datos guardados")  # :\n{self.model.data}
            self.show_computer_frame()  
            
    def guardarDatosPc(self): 
        datos = self.current_frame.get_pc_data()
        
        if not all(datos.values()):
            self.current_frame.mostrar_mensaje("Error", "Todos los campos son obligatorios")
            return
        
        if self.model.saveData(datos):
          #  self.current_frame.mostrar_mensaje("Éxito", f"Datos guardados")  # :\n{self.model.data}
            self.show_monitor_frame()
            
    def guardarDatosMonitor(self):   
        datos = self.current_frame.get_mon_data()
        
        if not all(datos.values()):
            self.current_frame.mostrar_mensaje("Error", "Todos los campos son obligatorios")
            return
        
        if self.model.saveData(datos):
           self.current_frame.mostrar_mensaje("Éxito", f"Datos guardados") # :\n{self.model.data}
        
        self.guardarDatosFinales(datos)  
                                  
    def guardarDatosFinales(self, datos):     
        datos_ordenados = "\n".join(f"{k}: {v}" for k, v in (self.model.data.items()))
        self.current_frame.mostrar_mensaje("CARGA FINALIZADA", f"Datos a exportar:\n{datos_ordenados}")
       
        if self.model.saveData(datos): 
            respuesta = messagebox.askyesno("¿Desea exportar los datos?")
        if respuesta:   # Lógica para exportar los datos
            self.exportar_datos(self.model.data)
            self.show_place_frame()
            self.new_data_insert()
        else:
            messagebox.showinfo("Cancelado", "Exportación cancelada.")
  
# CONTROL DE EXPORTACION DE DATOS        
    def exportar_datos(self, datos):
        exporter = ExportData(self.excel_path) 
        exporter.saveDataToExcel(datos)
        acta = saveDataToPDF(datos, self.pdf_path)
        messagebox.showinfo("Éxito", "Datos exportados correctamente.")
        return acta 
        
    def run(self):
        self.main_view.mainloop()