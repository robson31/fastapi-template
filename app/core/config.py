from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name: str = "ScalableFastAPIService"
    debug: bool = True

    # Database settings
    db_user: str = ""
    db_password: str = ""
    db_name: str = "test.db"

    @property
    def db_url(self):
        return f"sqlite:///./{self.db_name}"

settings = Settings()

