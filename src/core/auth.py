from fastapi import HTTPException, Security
from fastapi.security import APIKeyHeader
from starlette.status import HTTP_403_FORBIDDEN
import logging
from src.config.settings import load_env_vars
from src.utils.logger import setup_logger

warning_logger = setup_logger(__name__, level=logging.WARNING)
info_logger = setup_logger(__name__, level=logging.INFO)

api_key_header = APIKeyHeader(name="Authorization", auto_error=False)

FAST_API_KEY = load_env_vars()


async def get_api_key(api_key_header: str = Security(api_key_header)):
    if api_key_header is None:
        warning_logger.warning("API Key is missing in the request headers.")
        raise HTTPException(
            status_code=HTTP_403_FORBIDDEN, detail="Could not validate credentials"
        )
    if api_key_header != FAST_API_KEY:
        warning_logger.warning("Invalid API Key provided.")
        raise HTTPException(status_code=HTTP_403_FORBIDDEN, detail="Invalid API Key")
    info_logger.info("API Key validated successfully.")
    return api_key_header
