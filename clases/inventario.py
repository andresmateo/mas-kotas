class Inventario:
    def __init__(self):
        self.lista_productos = []
    
    def agregar_producto(self, producto):
        self.lista_productos.append(producto)
    
    def actualizar_inventario(self, producto, stock):
        for prod in self.lista_productos:
            if prod.nombre == producto.nombre:
                prod.actualizar_stock(stock)
    
    def generar_alerta(self, stock_minimo):
        alertas= [prod.nombre for prod in self.lista_productos if prod.stock < stock_minimo]
        return f"Productos por debajo del stock mínimo: {', '.join(alertas)}" if alertas else "No hay ningún producto con stock menor al mínimo."