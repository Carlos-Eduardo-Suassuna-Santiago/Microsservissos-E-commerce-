from fastapi import FastAPI
from routes import router

app = FastAPI(
    title="Order Service",
    description="Serviço de processamento de pedidos",
    version="1.0.0"
)

app.include_router(router)
