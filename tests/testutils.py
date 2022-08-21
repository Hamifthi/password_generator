import re

def compile_search_regex():
    # This regex ensure there is at least one number one lowercase one uppercase
    # and one special character at string
    return re.compile("^(?=.*[a-z])(?=.*[A-Z])(?=.*\\d)(?=.*\\W).+$")