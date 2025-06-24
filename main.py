import sys
import os
from Controller.appController import AppController
from utils.path import resource_path

# Punto de entrada de la aplicación
if __name__ == "__main__":
    excel_path = resource_path("files/datosMantenimiento1.xlsx") # Ruta al archivo Excel
    pdf_path = resource_path("files/FORMATO MMTO CBOLIVAR.pdf") # Ruta al archivo PDF
    print(f"Ruta Excel: {excel_path}")  # Verificación en consola
    print(f"Ruta PDF: {pdf_path}")      # Verificación en consola
    app = AppController()
    app.run()  
    