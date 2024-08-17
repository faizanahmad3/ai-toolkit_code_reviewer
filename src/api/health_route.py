from fastapi import APIRouter, Depends
from src.core.auth import get_api_key

health_router = APIRouter()


health_router.add_api_route("/ok", lambda: "OK", methods=["GET"], dependencies=[Depends(get_api_key)])
