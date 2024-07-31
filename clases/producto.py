class Producto:
    def __init__(self, nombre, categoria, precio, stock):
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio
        self.stock = stock

    def actualizar_stock(self, stock):
        self.stock = stock
    
    def mostrar_info(self):
        return f"Producto: {self.nombre}, Categoría: {self.categoria}, Precio: {self.precio}, Stock Actual: {self.stock}"