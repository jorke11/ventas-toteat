from fastapi import APIRouter
from model_mongo.product import Product
from config.database_mongo import collection_name
from schema.schema import list_serial
from bson import ObjectId
import json
from config.database_redis import rd

router = APIRouter()


@router.get("/products")
async def get_product(page: int = 0, limit: int = 10):
    # products = list_serial(collection_name.find())
    # return products
    cache = rd.get("products")
    cache = json.loads(cache)
    return {"total": len(cache), "page": page, "results": cache}


@router.post("/products")
async def create_product(product: Product):
    collection_name.insert_one(dict(product))
