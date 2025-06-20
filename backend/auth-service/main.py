from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from routes import router

app = FastAPI(
    title="Auth Service",
    description="Serviço de autenticação do e-commerce",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Aqui está a correção:
app.include_router(router, prefix="/auth")
