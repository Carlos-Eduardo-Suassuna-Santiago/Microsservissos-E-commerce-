# services.py

import os
from dotenv import load_dotenv
import httpx
from fastapi import HTTPException, status
from typing import Dict

load_dotenv()

PRODUCT_SERVICE_URL = os.getenv("PRODUCT_SERVICE_URL")
CART_SERVICE_URL = os.getenv("CART_SERVICE_URL")
ORDER_SERVICE_URL = os.getenv("ORDER_SERVICE_URL")
AUTH_SERVICE_URL = os.getenv("AUTH_SERVICE_URL")

async def forward_request(method: str, service_url: str, endpoint: str, data=None, params=None, headers=None):
    url = f"{service_url}{endpoint}"
    async with httpx.AsyncClient() as client:
        response = await client.request(method, url, json=data, params=params, headers=headers)
        return response

async def verify_token(authorization: str) -> Dict:
    if not authorization or not authorization.startswith("Bearer "):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token ausente ou inválido")

    token = authorization.split(" ")[1]

    async with httpx.AsyncClient() as client:
        response = await client.get(
            f"{AUTH_SERVICE_URL}/verify-token",
            headers={"Authorization": f"Bearer {token}"}
        )

        if response.status_code != 200:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token inválido")

        return response.json()
