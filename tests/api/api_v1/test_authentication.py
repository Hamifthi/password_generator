from fastapi.testclient import TestClient

import re

from core.config import settings
from tests.testutils import compile_search_regex

api_version = settings.API_VERSION


def test_create_random_password_endpoint_with_empty_data(client: TestClient) -> None:
    response = client.post(f"{api_version}/authentication/generate-password/")
    assert response.status_code == 422
    response = response.json()
    detail = response["detail"][0]
    location, message, error_type = detail["loc"], detail["msg"], detail["type"]
    assert location == ["body"]
    assert message == "field required"
    assert error_type == "value_error.missing"


def test_create_random_password_endpoint_with_none_data(client: TestClient) -> None:
    response = client.post(f"{api_version}/authentication/generate-password/", json={})
    assert response.status_code == 400
    response = response.json()
    detail = response["detail"]
    assert detail == "All values couldn't be null or false. At least one option should be set."


def test_create_random_password_endpoint_just_set_length(client: TestClient) -> None:
    response = client.post(f"{api_version}/authentication/generate-password/", json={"password_length": 10})
    assert response.status_code == 400
    response = response.json()
    detail = response["detail"]
    assert detail == "All values couldn't be null or false. At least one option should be set."


def test_create_random_password_endpoint_with_length_less_than_eight(client: TestClient) -> None:
    response = client.post(f"{api_version}/authentication/generate-password/", json={"password_length": 4})
    assert response.status_code == 422
    response = response.json()
    detail = response["detail"][0]
    location, message, error_type = detail["loc"], detail["msg"], detail["type"]
    assert location == ["body", "password_length"]
    assert message == "ensure this value is greater than 8"
    assert error_type == "value_error.number.not_gt"


def test_create_random_password_endpoint_with_length_more_than_two_hundred(client: TestClient) -> None:
    response = client.post(f"{api_version}/authentication/generate-password/", json={"password_length": 220})
    assert response.status_code == 422
    response = response.json()
    detail = response["detail"][0]
    location, message, error_type = detail["loc"], detail["msg"], detail["type"]
    assert location == ["body", "password_length"]
    assert message == "ensure this value is less than 200"
    assert error_type == "value_error.number.not_lt"


def test_create_random_password_endpoint_with_all_options_false(client: TestClient) -> None:
    data = {"password_length": 10, "include_numbers": False, "include_lowercase_chars": False,
            "include_uppercase_chars": False, "include_special_chars": False}
    response = client.post(f"{api_version}/authentication/generate-password/", json=data)
    assert response.status_code == 400
    response = response.json()
    detail = response["detail"]
    assert detail == "All values couldn't be null or false. At least one option should be set."


def test_create_random_password_endpoint_with_at_least_one_options_true(client: TestClient) -> None:
    password_length = 10
    data = {"password_length": password_length, "include_numbers": True}
    response = client.post(f"{api_version}/authentication/generate-password/", json=data)
    assert response.status_code == 200
    response = response.json()
    generated_password = response["generated_password"]
    assert len(generated_password) == password_length
    pattern = compile_search_regex()
    found_object = re.search(pattern, generated_password)
    assert found_object is not None
    assert found_object.string


def test_create_random_password_endpoint_with_all_options_true(client: TestClient) -> None:
    password_length = 20
    data = {"password_length": password_length, "include_numbers": True, "include_lowercase_chars": True,
            "include_uppercase_chars": True, "include_special_chars": True}
    response = client.post(f"{api_version}/authentication/generate-password/", json=data)
    assert response.status_code == 200
    response = response.json()
    generated_password = response["generated_password"]
    assert len(generated_password) == password_length
    pattern = compile_search_regex()
    found_object = re.search(pattern, generated_password)
    assert found_object is not None
    assert found_object.string
