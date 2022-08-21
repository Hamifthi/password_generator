import random
import string


def generate_password(password_length, include_numbers, include_lowercase_chars,
                      include_uppercase_chars, include_special_chars) -> str:
    numbers = string.digits
    lowercase_chars = string.ascii_lowercase
    uppercase_chars = string.ascii_uppercase
    special_chars = string.punctuation
    character_list = []
    if include_numbers:
        character_list.append(numbers)
    if include_lowercase_chars:
        character_list.append(lowercase_chars)
    if include_uppercase_chars:
        character_list.append(uppercase_chars)
    if include_special_chars:
        character_list.append(special_chars)

    length_chars_list = len(character_list)

    generated_chars = list()
    generated_password = ""
    # If user or settings config to not include any characters return empty string
    if length_chars_list == 0:
        return generated_password
    elif length_chars_list == 1:
        generated_chars = random.sample(character_list[0], password_length)
    else:
        # Because the character list could have at max length of 4, and password length might at least 8 characters,
        # use modulo operator to get index of next character in character list correctly for example: 5 % 3 = 2
        for i in range(password_length):
            generated_chars.append(random.choice(character_list[i % length_chars_list]))
    random.shuffle(generated_chars)
    generated_password = "".join(generated_chars)
    return generated_password
