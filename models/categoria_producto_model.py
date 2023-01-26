from app import db
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

class CategoriasProductosModel(db.Model):
    __tablename__ ='categorias_productos'

    id = Column(Integer, primary_key=True, autoincrement=True)
    categoria_id= Column(ForeignKey('categoria.id'))
    producto_id= Column(ForeignKey('producto.id'))

    def __init__(self, categoria_id,producto_id ) -> None:
        self.categoria_id= categoria_id
        self.producto_id= producto_id
