import re

from internal.utils import generate_password
from tests.testutils import compile_search_regex


def test_password_generator_with_password_length_zero() -> None:
    generated_password = generate_password(password_length=0, include_numbers=True,
                                           include_lowercase_chars=True,
                                           include_uppercase_chars=True,
                                           include_special_chars=True)
    assert generated_password == ""


def test_password_generator_with_all_options_false() -> None:
    generated_password = generate_password(password_length=10, include_numbers=False,
                                           include_lowercase_chars=False,
                                           include_uppercase_chars=False,
                                           include_special_chars=False)
    assert generated_password == ""


def test_password_generator_with_one_option_true() -> None:
    generated_password = generate_password(password_length=10, include_numbers=False,
                                           include_lowercase_chars=True,
                                           include_uppercase_chars=False,
                                           include_special_chars=False)
    assert generated_password is not None
    check_characters_pattern = compile_search_regex("^(?=.*[a-z]).+$")
    found_object = re.search(check_characters_pattern, generated_password)
    assert found_object is not None
    assert found_object.string


def test_password_generator_with_all_option_true() -> None:
    generated_password = generate_password(password_length=20, include_numbers=True,
                                           include_lowercase_chars=True,
                                           include_uppercase_chars=True,
                                           include_special_chars=True)
    assert generated_password is not None
    check_characters_pattern = compile_search_regex()
    found_object = re.search(check_characters_pattern, generated_password)
    assert found_object is not None
    assert found_object.string
