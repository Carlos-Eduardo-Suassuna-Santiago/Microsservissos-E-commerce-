from fastapi import FastAPI
from routes import router

app = FastAPI(
    title="Product Service",
    description="Serviço de gerenciamento de produtos do e-commerce",
    version="1.0.0"
)

app.include_router(router)
