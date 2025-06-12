import openpyxl
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment

workbook = openpyxl.load_workbook("datosMantenimiento1.xlsx")
sheet = workbook.active

class ExportData:
    def __init__(self):
        self.dataToExport = {}
        
    def saveDataToExcel(self, datos):
        self.dataToExport = datos  # Asignar los datos a exportar
  
   # Obtener los datos del modelo
# {
#     "Fecha":"12 de octubre de 2025",
#     "Ciudad":"Bogotá", 
#     "Sede": "Granada",    
#     "Centro de costos": 124578,
#     "Nombre de Usuario":"Ivan Ramirez",
#     "No de documento": 80232200, 
#     "Marca de computador": "HP", 
#     "Modelo": "EliteBook 840 G3", 
#     "Serial": "CND123456789", 
#     "Activo": "ML2324",
#     "Marca de monitor": "HP",
#     "SerialM": "MND987654321", 
#     "ActivoM": "ML9876", 
#     "Accesorios": "Cargador, Mouse",
#     "Observaciones": "Ninguna"
# }

        row = 2 # La fila en la que empezar a escribir # La columna en la que empezar a escribir
        cell = sheet['A2']

        if cell.value:  #si hay dato en la celda inserte un fila vacia
            sheet.insert_rows(idx=2, amount=1) 
    
        for col, key in enumerate(self.dataToExport.keys(), start=1):    #iteracion sobre el diccionario 
            sheet.cell(row=row, column=col).value = self.dataToExport[key] # Escribe el valor en la celda indicada  
            sheet.cell(row=row, column=col).alignment = Alignment(horizontal="center", vertical="center")
            column_letter = sheet.cell(row=row, column=col).column_letter # Obtener la letra de la columna
            sheet.column_dimensions[column_letter].width = len(self.dataToExport) + 2 
        #column += 1
    
        workbook.save('datosMantenimiento1.xlsx')