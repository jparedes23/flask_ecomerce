from app import app
from controllers.productos_controller import ProductoController


@app.route("/productos/listar", methods=['GET'])
def productosListar():
    controller = ProductoController()
    return controller.listarProductos()
