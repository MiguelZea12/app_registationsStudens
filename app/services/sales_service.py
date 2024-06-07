from app.models.ventas import ventas
from app.schemas.ventas_schemas import SaleSchemas
from app.extensions import db

def get(id: int):
    sale_object = db.session.query(ventas).filter(ventas.id == id).first()
    sale_schema = SaleSchemas()
    return sale_schema.dump(sale_object)

def get_all():
    sale_objects =  db.session.query(ventas).filter(ventas.status == True).all()
    return sale_objects

def create(id_client: int, date: str, status: bool):
    sale_object = ventas(
        id_client=id_client,
        date=date,
        status=status,
        user_cration_id= 1
    )
    db.session.add(sale_object)
    db.session.commit()
    sale_schema = SaleSchemas()
    return sale_schema.dump(sale_object)

def update(id: int, data: dict):
    sale_object = db.session.query(ventas).filter(ventas.id == id).first()
    for key, value in data.items():
        setattr(sale_object, key, value)
    db.session.commit()
    sale_schema = SaleSchemas()
    return sale_schema.dump(sale_object)

def delete(id: int):
    sale_object = db.session.query(ventas).filter(ventas.id == id).first()
    if sale_object is None:
        return {"message": "Sale not found"}, 404
    db.session.delete(sale_object)
    db.session.commit()
    return {"message": "Sale deleted successfully"}


