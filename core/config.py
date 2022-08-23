from typing import Union, List
from pydantic import BaseSettings, AnyHttpUrl, validator


class Settings(BaseSettings):
    APP_NAME: str
    API_VERSION: str
    PASSWORD_LENGTH: int
    INCLUDE_NUMBERS: bool
    INCLUDE_LOWERCASE_CHARS: bool
    INCLUDE_UPPERCASE_CHARS: bool
    INCLUDE_SPECIAL_CHARS: bool

    BACKEND_CORS_ORIGINS: List[AnyHttpUrl]

    @validator("BACKEND_CORS_ORIGINS", pre=True)
    def assemble_cors_origins(cls, v: Union[str, List[str]]) -> Union[List[str], str]:
        if isinstance(v, str) and not v.startswith("["):
            return [i.strip() for i in v.split(",")]
        elif isinstance(v, (list, str)):
            return v
        raise ValueError(v)

    class Config:
        env_file = ".env"
        case_sensitive = True


settings = Settings()
