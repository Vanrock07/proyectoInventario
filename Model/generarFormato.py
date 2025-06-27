from PyPDF2 import PdfReader, PdfWriter
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
import io
from reportlab.lib.utils import simpleSplit
import os

# class generarFormato:
#     def __init__(self):
#         self.dataToExport = {}
#         self.fileName = "MODELO1"
#         self.input_pdf = "FORMATO MMTO CBOLIVAR.pdf"
#         self.output_pdf = self.fileName + ".pdf"
#         self.acta = None  # Inicializar acta como None
#def saveDataToPDF(datos): 

name = "formato de prueba"

def saveDataToPDF(datos, pdf_path: str):
    
    if not os.path.exists(pdf_path):
        raise FileNotFoundError(f"Plantilla PDF no encontrada: {pdf_path}")
    
    dataToExport = {}
    dataToExport = datos # Asignar los datos a exportar
    rutaPdf = os.path.abspath(pdf_path)  # Obtener la ruta absoluta del PDF
    fileName = dataToExport["activo"]  # Obtener el nombre del usuario o usar un valor por defecto 
    input_pdf = rutaPdf  # Ruta del PDF de entrada"
    output_pdf = fileName + ".pdf"    
    
    generar_pdf(input_pdf, output_pdf, dataToExport) # llamar a la función para generar el PDF
   
# Crear un PDF temporal con el texto a agregar
def write_in_pdf1(dataToExport):
        packet = io.BytesIO()
        can = canvas.Canvas(packet, pagesize=letter)
        can.setFont("Times-Roman", 10)
        can.drawString(110, 660, dataToExport["fecha"])  # Fecha
        can.drawString(80, 635,dataToExport["nombre"]) # Nombre del usuario
        can.drawString(280, 635, dataToExport["documento"]) # Número de cédula
        can.drawString(460, 635, dataToExport["centro de costos"])  # centro de costo
        can.drawString(80, 608, dataToExport["activo"]) # activo del equipo
        can.drawString(175, 608, dataToExport["tipo"]) # Tipo de equipo
        can.drawString(347, 608, dataToExport["serial"]) # Serial del equipo
        can.drawString(80, 582, dataToExport["marcaM"]) # Marca del monitor
        can.drawString(200, 582, dataToExport["serialM"])  # serial del monitor
        can.drawString(347, 582, dataToExport["activoM"]) # activo del monitor
        can.drawString(80, 556, dataToExport["accesorios"]) # accesorios
        can.drawString(110, 530, dataToExport["ciudad"]) # ciudad
        can.drawString(200, 530, dataToExport["sede"])  # sede
        can.drawString(347, 530, dataToExport["ubicacion"])  # ubicación
        can.drawString(115, 448, dataToExport["tamano"])  # tamaño del disco
        can.drawString(200, 448, dataToExport["disco"])  # tipo de disco 
        can.drawString(310, 448, dataToExport["ram"])  # memoria RAM
        can.drawString(375, 448, dataToExport["procesador"])  # procesador
        
        if dataToExport["sistema operativo"] == "Windows 10":
            x = 123  
        elif dataToExport["sistema operativo"] == "Windows 11":
            x = 314
        can.drawString(x, 279, "X")  
    
        can.setFont("Times-Roman", 7)
        can.drawString(246, 608, f'{dataToExport["marca"]} , {dataToExport["modelo"]}') #marca y modelo del equipo
        can.save()
        packet.seek(0) # Crear un objeto PdfReader a partir del contenido del paquete
        return PdfReader(packet)

def write_in_pdf2(dataToExport):
        packet = io.BytesIO()
        can = canvas.Canvas(packet, pagesize=letter)
        can.setFont("Times-Roman", 10)
        textobject = can.beginText()
        textobject.setTextOrigin(60, 695)
        textobject.setFont("Times-Roman", 10)
        
        text =  dataToExport["observaciones"]  # Obtener las observaciones del diccionario de datos
        
        lines = simpleSplit(text,"Times-Roman", 10, 480)  # Ajustar el ancho a 480 puntos
        for line in lines:
            textobject.textLine(line)
        
        can.drawText(textobject) # Dibujar el texto en el PDF
        can.drawString(110, 595, dataToExport["documento"])  # Fecha
        can.save()
        packet.seek(0)
        return PdfReader(packet)

def generar_pdf(input_pdf, output_pdf, dataToExport):
        existing_pdf = PdfReader(open(input_pdf, "rb"))
        output = PdfWriter()

# Combinar la página original con el texto nuevo
        for i, page in enumerate(existing_pdf.pages):
            if i == 0:
                new_pdf = write_in_pdf1(dataToExport)
                page.merge_page(new_pdf.pages[0])
            elif i == 1:
                new_pdf = write_in_pdf2(dataToExport)
                page.merge_page(new_pdf.pages[0])    
            output.add_page(page)
         
        carpeta_destino = os.path.join(os.getcwd(), "actas")
        if not os.path.exists(carpeta_destino):
            os.makedirs(carpeta_destino)
        ruta_salida = os.path.join(carpeta_destino, output_pdf)    
            
# Guardar el PDF resultante
        with open(ruta_salida, "wb") as outputStream:
            output.write(outputStream)
        os.startfile(ruta_salida) # Abrir el PDF resultante
    