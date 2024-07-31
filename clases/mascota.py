class Mascota:
    def __init__(self, nombre, raza, edad, salud, precio):
        self.nombre = nombre
        self.raza = raza
        self.edad = edad
        self.salud = salud
        self.precio = precio

    def actualizar_info(self, edad=None, salud=None, precio=None):
        if edad:
            self.edad = edad
        if salud:
            self.salud = salud
        if precio:
            self.precio = precio

    def mostrar_info(self):
        return f"Mascota: {self.nombre}, Edad: {self.edad}, Salud: {self.salud}, Precio: {self.precio}"
    
class Perro(Mascota):
    def __init__(self, nombre, raza, edad, salud, precio, vivacidad):
        super().__init__(nombre, raza, edad, salud, precio)
        self.vivacidad = vivacidad
    
    def mostrar_caracteristicas(self):
        return f"Raza: {self.raza}, Vivacidad: {self.vivacidad}"
    
class Gato(Mascota):
    def __init__(self, nombre, raza, edad, salud, precio, independencia):
        super().__init__(nombre, raza, edad, salud, precio)
        self.independencia = independencia
    
    def mostrar_caracteristicas(self):
        return f"Raza: {self.raza}, Independencia: {self.independencia}"