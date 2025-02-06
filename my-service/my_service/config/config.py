from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import List
from pydantic import AnyHttpUrl
import os
from dotenv import load_dotenv

load_dotenv()


class Settings(BaseSettings):
    BACKEND_ORIGINS: List[AnyHttpUrl] = []
    FASTAPI_PROJECT_NAME: str = "my-service"
    LOG_LEVEL: str = "DEBUG"

    # ArgoCD Config defaults
    ENV: str = os.getenv("ENV", "local")
    ARGOCD_SERVER: str = os.getenv("ARGOCD_SERVER", "localhost")
    ARGOCD_PORT: str = os.getenv("ARGOCD_PORT", 443)
    ARGOCD_URL_LOCAL: str = os.getenv("ARGOCD_URL_LOCAL", "localhost:4040")
    ARGOCD_URL_PROD: str = os.getenv(
        "ARGOCD_URL_PROD", "argocd-server.argocd.svc.cluster.local:443"
    )
    ARGOCD_URL: str = ARGOCD_URL_PROD if ENV == "production" else ARGOCD_URL_LOCAL
    ARGOCD_PASSWORD: str = os.getenv("ARGOCD_PASSWORD", "")
    ARGOCD_USERNAME: str = os.getenv("ARGOCD_USERNAME", "admin")
    TOKEN_CACHE_TTL: int = os.getenv("TOKEN_CACHE_TTL", 600)

    model_config = SettingsConfigDict(env_nested_delimiter="__")


settings = Settings(_env_file=".env")
