from fastapi import FastAPI
from routes import router

app = FastAPI(
    title="Cart Service",
    description="Serviço de gerenciamento de carrinho de compras",
    version="1.0.0"
)

app.include_router(router)
