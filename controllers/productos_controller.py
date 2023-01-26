from models.productos_model import ProductosModel


class ProductoController:

    def __init__(self) -> None:
        self.model = ProductosModel

    def crearProducto(self):
        return {
            'message':'soy el metodo de crear productos'
        }

    def listarProductos(self):
        productos = ProductosModel.query.all()
        return {
            'message':'lista de productos'
        }

    
