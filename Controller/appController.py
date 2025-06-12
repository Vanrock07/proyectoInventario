
from View.windowPlace import PlaceDataWindow
from View.windowUser import UserDataWindow
from View.mainWindow import MainWindow
from View.windowComputer import ComputerDataWindow
from View.windowMonitor import MonitorDataWindow
from View.windowGadgets import GadgetsDataWindow
from View.windowSheet import SheetWindow
from Model.dataPlace import modeloDatos
from Model.saveData import ExportData

class AppController:
    """Controlador principal que maneja la lógica de la aplicación"""
    def __init__(self):
        self.model = modeloDatos()
        self.main_view = MainWindow(self)
        self.place_view = None
        self.user_view = None
        self.computer_view = None
        self.monitor_view = None
        self.gadgets_view = None
        self.sheet_view = None
        #self.export = ExportData()

  #CONTROLADOR DE DESPLIEGUE DE VENTANAS        
    def open_place_window(self):
        if not self.place_view:
           self.place_view =  PlaceDataWindow(self)
         
    def open_user_window(self):
        if not self.user_view:
            self.user_view = UserDataWindow(self)
            
    def open_computer_window(self):
        if not self.computer_view:
            self.computer_view = ComputerDataWindow(self)
                   
    def open_monitor_window(self): 
        if not self.monitor_view:
            self.monitor_view = MonitorDataWindow(self)  
            
    def open_gadgets_window(self): 
        if not self.gadgets_view:
            self.gadgets_view = GadgetsDataWindow(self)
            
    def open_sheet_window(self): 
        if not self.sheet_view:
            self.sheet_view = SheetWindow(self)      
        
    def export_data(self):
        self.export = ExportData(self)

    #CONTROLADOR DE GUARDADO DE DATOS

    def guardarDatoSede(self):

        datos = self.place_view.get_place_data()
        
        if not all(datos.values()):
            self.place_view.mostrar_mensaje("Error", "Todos los campos son obligatorios")
            return
        
        if self.model.saveData(datos):
            self.place_view.mostrar_mensaje("Éxito", f"Datos guardados:\n{self.model.data}")
            self.place_view.window_Place.destroy()
            
        self.open_user_window()
        self.place_view.window_Place.destroy()    
     
    def guardarDatosUsuario(self):
        
        datos = self.user_view.get_user_data()
        
        if not all(datos.values()):
            self.user_view.mostrar_mensaje("Error", "Todos los campos son obligatorios")
            return
        
        if self.model.saveData(datos):
            self.user_view.mostrar_mensaje("Éxito", f"Datos guardados:\n{self.model.data}")
            self.user_view.window_Usr.destroy()
            
        self.open_computer_window()
        self.user_view.window_Usr.destroy()  
        
    def guardarDatosPc(self):
        
        datos = self.computer_view.get_pc_data()
        
        if not all(datos.values()):
            self.user_view.mostrar_mensaje("Error", "Todos los campos son obligatorios")
            return
        
        if self.model.saveData(datos):
            self.computer_view.mostrar_mensaje("Éxito", f"Datos guardados:\n{self.model.data}")
            self.computer_view.window_Pc.destroy()
            
        self.open_monitor_window()
        self.computer_view.window_Pc.destroy()   
        
    def guardarDatosMonitor(self):
        
        datos = self.monitor_view.get_mon_data()
        
        if not all(datos.values()):
            self.monitor_view.mostrar_mensaje("Error", "Todos los campos son obligatorios")
            return
        
        if self.model.saveData(datos):
            self.monitor_view.mostrar_mensaje("Éxito", f"Datos guardados:\n{self.model.data}")
            self.monitor_view.window_Mon.destroy()
            
        self.open_gadgets_window()
        self.computer_view.window_Pc.destroy()    
        
    def guardarDatosGadgets(self):
        
        datos = self.gadgets_view.get_gadget_data()
        
        if not all(datos.values()):
            self.gadgets_view.mostrar_mensaje("Error", "Todos los campos son obligatorios")
            return
        
        if self.model.saveData(datos):
            self.export_data(self.model.data) #Crear metodo para guardar en excel
            self.gadgets_view.mostrar_mensaje("Éxito", f"Datos guardados:\n{self.model.data}")
            self.gadgets_view.window_Gdt.destroy()
                
        self.computer_view.window_Pc.destroy()

    def export_data(self, datos):
       exporter = ExportData() 
       exporter.saveDataToExcel(datos)
       print("Se guardaran los datos en la base de datos:" f"\n{datos}") #enviar a excel
                                                        
    def run(self):
        self.main_view.mainloop()