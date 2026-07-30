from pydantic_settings import BaseSettings, SettingsConfigDict
import os
from pydantic import SecretStr

current_directory = os.path.dirname(os.path.abspath(__file__))
env_file_path = os.path.join(current_directory, "..", ".env")

class Settings(BaseSettings):
    app_name: str

    model_config = SettingsConfigDict(env_file=env_file_path)

    # CONNECT TO DATABASE DBEAVER AND AFTER SAME INSIDE .env file too but use = NOT : inside file .env

    db_host: str
    db_port: str
    db_user: str
    db_pass: SecretStr
    db_name: str


settings = Settings()

#dopo lo importo nel main.py così from src.config import settings