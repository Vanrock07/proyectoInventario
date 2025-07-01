
from Controller.appController2 import AppController2
from utils.path import resource_path

# Punto de entrada de la aplicación
if __name__ == "__main__":
    excel_path = resource_path("files2/datosMantenimiento1.xlsx") # Ruta al archivo Excel
    pdf_path = resource_path("files2/FORMATO MMTO CBOLIVAR.pdf") # Ruta al archivo PDF
    print(f"Ruta Excel: {excel_path}")  # Verificación en consola
    print(f"Ruta PDF: {pdf_path}")      # Verificación en consola
    app = AppController2()
    app.run()  
    