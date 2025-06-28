
# from View.windowPlace import PlaceDataWindow
# from View.windowUser import UserDataWindow
# from View.mainWindow import MainWindow
# from View.windowComputer import ComputerDataWindow
# from View.windowMonitor import MonitorDataWindow
# from View.windowGadgets import GadgetsDataWindow
# from View.windowSheet import SheetWindow
# from Model.dataPlace import modeloDatos
# from Model.saveData import ExportData
# from Model.generarFormato import saveDataToPDF
# from utils.path import resource_path



# class AppController:
#     """Controlador principal que maneja la lógica de la aplicación"""
#     def __init__(self):
#         self.excel_path = resource_path("files2/datosMantenimiento1.xlsx") # Ruta al archivo Excel
#         self.pdf_path = resource_path("files2/FORMATO MMTO CBOLIVAR.pdf") # Ruta al archivo PDF
#         self.model = modeloDatos() 
#         self.main_view = MainWindow(self)
#         self.place_view = None
#         self.user_view = None
#         self.computer_view = None
#         self.monitor_view = None
#         self.gadgets_view = None
#         self.sheet_view = None

# #CONTROLADOR DE DESPLIEGUE DE VENTANAS        
#     def open_place_window(self):
#          # Si ya existe una ventana de sede, ciérrala antes de abrir una nueva
#         if self.place_view is not None:
#             try:
#                 self.place_view.window_Place.destroy()
#             except:
#                 pass
#             self.place_view = None
#         self.place_view = PlaceDataWindow(self)
        
         
#     def open_user_window(self):
#         if self.user_view is not None:
#             try:
#                 self.user_view.window_Usr.destroy()
#             except:
#                 pass
#             self.user_view_view = None
#         self.user_view = UserDataWindow(self)
            
#     def open_computer_window(self):
#         if self.computer_view is not None:
#             try:
#                 self.computer_view.window_Pc.destroy()
#             except:
#                 pass
#             self.computer_view = None
#         self.computer_view = ComputerDataWindow(self)
                   
#     def open_monitor_window(self): 
#         if self.monitor_view is not None:
#             try:
#                 self.monitor_view.window_Mon.destroy()
#             except:
#                 pass
#             self.monitor_view = None
#         self.monitor_view = MonitorDataWindow(self)  
            
#     def open_gadgets_window(self): 
#         if self.gadgets_view is not None:
#             try:
#                 self.gadgets_view.window_Gdt.destroy()
#             except:
#                 pass
#             self.gadgets_view = None
#         self.gadgets_view = GadgetsDataWindow(self)
            
#     # def open_sheet_window(self): 
#     #     if not self.sheet_view:
#     #         self.sheet_view = SheetWindow(self)      
        
#     # def export_data(self):
#     #     self.export = ExportData(self, excel_path=self.excel_path)  # Crear instancia de ExportData

# #CONTROLADOR DE GUARDADO DE DATOS
#     def guardarDatoSede(self):

#         datos = self.place_view.get_place_data()
        
#         if not all(datos.values()):
#             self.place_view.mostrar_mensaje("Error", "Todos los campos son obligatorios")
#             return
        
#         if self.model.saveData(datos):
#             self.place_view.mostrar_mensaje("Éxito", f"Datos guardados:\n{self.model.data}")
#             self.place_view.window_Place.destroy()
            
#         self.open_user_window()
#         self.place_view.window_Place.destroy()    
     
#     def guardarDatosUsuario(self):
        
#         datos = self.user_view.get_user_data()
        
#         if not all(datos.values()):
#             self.user_view.mostrar_mensaje("Error", "Todos los campos son obligatorios")
#             return
        
#         if self.model.saveData(datos):
#             self.user_view.mostrar_mensaje("Éxito", f"Datos guardados:\n{self.model.data}")
#             self.user_view.window_Usr.destroy()
            
#         self.open_computer_window()
#         self.user_view.window_Usr.destroy()  
        
#     def guardarDatosPc(self):
        
#         datos = self.computer_view.get_pc_data()
        
#         if not all(datos.values()):
#             self.user_view.mostrar_mensaje("Error", "Todos los campos son obligatorios")
#             return
        
#         if self.model.saveData(datos):
#             self.computer_view.mostrar_mensaje("Éxito", f"Datos guardados:\n{self.model.data}")
#             self.computer_view.window_Pc.destroy()
            
#         self.open_monitor_window()
#         self.computer_view.window_Pc.destroy()   
        
#     def guardarDatosMonitor(self):
        
#         datos = self.monitor_view.get_mon_data()
        
#         if not all(datos.values()):
#             self.monitor_view.mostrar_mensaje("Error", "Todos los campos son obligatorios")
#             return
        
#         if self.model.saveData(datos):
#             self.monitor_view.mostrar_mensaje("Éxito", f"Datos guardados:\n{self.model.data}")
#             self.monitor_view.window_Mon.destroy()
            
#         self.open_gadgets_window()
#         self.computer_view.window_Pc.destroy()    
        
#     def guardarDatosGadgets(self):
        
#         datos = self.gadgets_view.get_gadget_data()
        
#         # if not all(datos.values()):
#         #     self.gadgets_view.mostrar_mensaje("Error", "Todos los campos son obligatorios")
#         #     return
        
#         if self.model.saveData(datos):
#             self.export_data(self.model.data) #Crear metodo para guardar en excel
#             self.gadgets_view.mostrar_mensaje("Éxito", f"Datos guardados")
#             self.gadgets_view.window_Gdt.destroy()
                
#         self.computer_view.window_Pc.destroy()

# # CONTROLADOR DE EXPORTACION DE DATOS
#     def export_data(self, datos):
#        exporter = ExportData(self.excel_path) 
#        exporter.saveDataToExcel(datos)
#        acta = saveDataToPDF(datos, self.pdf_path)
#        print("Se guardaron los datos en la base de datos") 
#        return acta 
#        #enviar a excel
              
# # CONTROLADOR DE CREACION DE ACTA
#     def generar_acta():
#         saveDataToPDF()
#       #  print("Se generara el acta con los datos:" f"\n{datos}")
              
                                                        
#     def run(self):
#         self.main_view.mainloop()