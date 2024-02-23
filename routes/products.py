from fastapi import APIRouter

router = APIRouter(prefix="/products", tags=["products"], responses={404: {"messages": "No encontrado"}})

products_list = ["Banana", "Azucar", "Pan"]

@router.get("")
def get_products():
    return products_list

@router.get("/{id}")
def get_product_by_id(id: int):
    return products_list[id]