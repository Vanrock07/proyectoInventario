
class modeloDatos:
    
    def __init__(self):
        self.data = {}

    def saveData(self, data):
        self.data.update(data)
        return True
    
    def obtener_datos(self):
        """Devuelve los datos almacenados"""
        return self.data.copy()   
    
    