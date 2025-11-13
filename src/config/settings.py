thonimport os

class Settings:
    API_KEY = os.getenv("API_KEY", "default_api_key")
    ALLOWED_PLATFORMS = ["youtube", "tiktok", "linkedin"]

settings = Settings()