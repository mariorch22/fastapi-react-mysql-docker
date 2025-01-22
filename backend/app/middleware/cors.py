from fastapi import Request
import os

FRONTEND_URL = os.environ.get("FRONTEND_URL")


async def cors_middleware(request: Request, call_next):

    origin = request.headers.get('origin')
    print(f"Anfrage von Origin: {origin}")

    response = await call_next(request)
    response.headers["Access-Control-Allow-Origin"] = FRONTEND_URL
    response.headers["Access-Control-Allow-Methods"] = "*"
    response.headers["Access-Control-Allow-Headers"] = "*"
    return response
