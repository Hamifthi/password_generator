from pydantic import BaseModel, Field

from core.config import settings


class PasswordFeatures(BaseModel):
    length: int = Field(default=settings.PASSWORD_MINIMUM_LENGTH, lt=200)
    include_numbers: bool = Field(default=settings.INCLUDE_NUMBERS)
    include_lowercase_chars: bool = Field(default=settings.INCLUDE_LOWERCASE_CHARS)
    include_uppercase_chars: bool = Field(default=settings.INCLUDE_UPPERCASE_CHARS)
    include_special_chars: bool = Field(default=settings.INCLUDE_SPECIAL_CHARS)


class Password(BaseModel):
    generated_password: str
