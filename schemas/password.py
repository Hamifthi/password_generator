from typing import Union
from pydantic import BaseModel, Field


class PasswordFeatures(BaseModel):
    password_length: Union[None, int] = Field(gt=8, lt=200)
    include_numbers: Union[None, bool] = None
    include_lowercase_chars: Union[None, bool] = None
    include_uppercase_chars: Union[None, bool] = None
    include_special_chars: Union[None, bool] = None


class Password(BaseModel):
    generated_password: str
