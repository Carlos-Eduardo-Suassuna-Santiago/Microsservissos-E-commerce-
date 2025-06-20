# main.py

from fastapi import FastAPI, Request, Depends, HTTPException
from fastapi.responses import JSONResponse
import httpx
from services import forward_request, verify_token, PRODUCT_SERVICE_URL, CART_SERVICE_URL, ORDER_SERVICE_URL, AUTH_SERVICE_URL

app = FastAPI(title="API Gateway", description="Gateway para microsserviços", version="1.0.0")

# Middleware de autenticação para rotas protegidas
async def require_auth(request: Request):
    auth = request.headers.get("Authorization")
    user_data = await verify_token(auth)
    return user_data

@app.get("/verify-user")
async def verify_user(request: Request, user_data: dict = Depends(require_auth)):
    return {"user_id": user_data["user_id"]}


# 🔓 Rotas públicas
@app.get("/products")
async def get_all_products():
    res = await forward_request("GET", PRODUCT_SERVICE_URL, "/products")
    return res.json()

@app.post("/auth/register")
async def register_user(request: Request):
    data = await request.json()
    res = await forward_request("POST", AUTH_SERVICE_URL, "/register", data=data)
    return res.json()

@app.post("/auth/login")
async def login_user(request: Request):
    body = await request.json()
    async with httpx.AsyncClient() as client:
        response = await client.post(
            f"{AUTH_SERVICE_URL}/login",
            json=body  # <-- agora sim pode usar json
        )
        return JSONResponse(status_code=response.status_code, content=response.json())


# 🔒 Rotas protegidas
@app.post("/cart")
async def add_to_cart(request: Request, user_data: dict = Depends(require_auth)):
    data = await request.json()
    data["user_id"] = user_data["user_id"]
    res = await forward_request("POST", CART_SERVICE_URL, "/cart", data=data)
    return res.json()

@app.get("/cart/{user_id}")
async def get_cart(user_id: int, user_data: dict = Depends(require_auth)):
    if user_id != user_data["user_id"]:
        raise HTTPException(status_code=403, detail="Acesso negado ao carrinho de outro usuário.")
    res = await forward_request("GET", CART_SERVICE_URL, f"/cart/{user_id}")
    return res.json()

@app.post("/orders")
async def create_order(request: Request, user_data: dict = Depends(require_auth)):
    data = await request.json()
    data["user_id"] = user_data["user_id"]
    res = await forward_request("POST", ORDER_SERVICE_URL, "/orders", data=data)
    return res.json()

@app.get("/orders/{user_id}")
async def get_orders(user_id: int, user_data: dict = Depends(require_auth)):
    if user_id != user_data["user_id"]:
        raise HTTPException(status_code=403, detail="Acesso negado aos pedidos de outro usuário.")
    res = await forward_request("GET", ORDER_SERVICE_URL, f"/orders/{user_id}")
    return res.json()

