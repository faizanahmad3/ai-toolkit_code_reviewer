from src.api.analyzer_route import analyzer_router
from src.api.uploader_route import upload_router
from src.api.health_route import health_router
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


def create_app() -> FastAPI:
    app = FastAPI(title="ai_toolkit", description="AI toolkit for payever.")

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],  # Specify the correct origins
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.include_router(health_router)
    app.include_router(upload_router)
    app.include_router(analyzer_router)

    return app
