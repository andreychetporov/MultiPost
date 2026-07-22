from pydantic import BaseModel

class AppSettings(BaseModel):

    app_name: str = "Default_name"
    app_env: str = "Default_env"

