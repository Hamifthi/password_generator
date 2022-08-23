import re


def compile_search_regex(pattern="^(?=.*[a-z])(?=.*[A-Z])(?=.*\\d)(?=.*\\W).+$"):
    # This regex ensure there is at least one number one lowercase one uppercase
    # and one special character at string
    return re.compile(pattern)
