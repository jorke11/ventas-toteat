from fastapi import FastAPI
from enum import Enum
from typing import Optional
from pydantic import BaseModel

import json
import requests
import jmespath
from tools.extraction import Extraction
from tools.processing_data import ProcessinData
from config.database_redis import rd
from routes.product_router import router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.include_router(router)

origins = [
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {"message": "Api For Sales"}


@app.get("/sync-remote-data")
async def sync_remote_data(limit: int = 2):
    data = requests.get(
        'https://storage.googleapis.com/backupdatadev/ejercicio/ventas.json')

    jsondata = data.json()

    print(jsondata[:2])

    rd.set("sales", data.text)
    extraction = Extraction(jsondata)
    rd.set("categories", json.dumps(extraction.getCategories()))
    rd.set("products", json.dumps(extraction.getProducts()))
    rd.set("method_payments", json.dumps(extraction.getMethodPayments()))
    rd.set("waiters", json.dumps(extraction.getWaiters()))
    rd.set("cashiers", json.dumps(extraction.getCashiers()))
    rd.set("zones", json.dumps(extraction.getZones()))
    rd.set("dining_table", json.dumps(extraction.getDiningTable()))
    return {"message": "Todo sync"}


@app.get("/sales")
async def get_sales(page: int = 0, limit: int = 10):
    cache = rd.get("sales")
    cache = json.loads(cache)
    # return {"total": len(cache), "page": page, "results": cache[:page + limit]}
    return {"total": len(cache), "page": page, "results": cache[:20]}


@app.get("/sales/{id}")
async def get_sale_by_id(id: str):
    cache = rd.get("sales")
    jsonData = json.loads(cache)
    string_query = f"[?id=='{id}']"
    result = jmespath.search(string_query, jsonData)
    return result


@app.get("/method-payments")
async def get_sales(page: int = 0, limit: int = 10):
    cache = rd.get("method_payments")
    cache = json.loads(cache)
    return {"total": len(cache), "page": page, "results": cache[:page + limit]}


@app.get("/category")
async def get_sales(page: int = 0, limit: int = 10):
    cache = rd.get("categories")
    cache = json.loads(cache)
    return {"total": len(cache), "page": page, "results": cache[:page + limit]}


@app.get("/waiter")
async def get_sales(page: int = 0, limit: int = 10):
    cache = rd.get("waiters")
    cache = json.loads(cache)
    return {"total": len(cache), "page": page, "results": cache[:page + limit]}


@app.get("/cashier")
async def get_sales(page: int = 0, limit: int = 10):
    cache = rd.get("cashiers")
    cache = json.loads(cache)
    return {"total": len(cache), "page": page, "results": cache[:page + limit]}


@app.get("/zones")
async def get_sales(page: int = 0, limit: int = 10):
    cache = rd.get("zones")
    cache = json.loads(cache)
    return {"total": len(cache), "page": page, "results": cache[:page + limit]}


@app.get("/dining-table")
async def get_sales(page: int = 0, limit: int = 10):
    cache = rd.get("dining_table")
    cache = json.loads(cache)
    return {"total": len(cache), "page": page, "results": cache[:page + limit]}


@app.get("/report")
async def get_report(page: int = 0, limit: int = 10):
    jsondata = rd.get("sales")
    obj = ProcessinData(json.loads(jsondata))
    data = obj.serializeData()
    return data
