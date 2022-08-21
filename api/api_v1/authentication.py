from fastapi import APIRouter, HTTPException

from schemas import password
from core.config import settings
from internal.utils import generate_password

router = APIRouter()


@router.post("/generate-password/", response_model=password.Password)
async def create_random_password(features: password.PasswordFeatures):
    # First we check if all option were None, then raise exception
    if any(list(features.dict().values())) is False:
        raise HTTPException(status_code=400, detail="All values couldn't be null. At least one option should be set.")
    # Add input data to a dict and add default values from settings in case of None values
    password_features = dict()
    for key, value in features.dict().items():
        if value is None:
            password_features[key] = getattr(settings, key.upper())
        else:
            password_features[key] = value
    # If an error occurred return internal server error
    try:
        generated_password = generate_password(**password_features)
    except Exception:
        raise HTTPException(status_code=500, detail="Internal server error.")
    return {'generated_password': generated_password}
