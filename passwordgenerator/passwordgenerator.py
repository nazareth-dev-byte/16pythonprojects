import random
import string
import secrets

def generate_password(length, types):
    """Return a random password of the given length. types is a list of 'uppercase', 'lowercase', 'digits', 'punctuations'."""


    selected_sets = []
    pool = ""
    if "uppercase" in types:
        pool += string.ascii_uppercase
        selected_sets.append(string.ascii_uppercase)
    if "lowercase" in types:
        pool += string.ascii_lowercase
        selected_sets.append(string.ascii_lowercase)
    if "digits" in types:
        pool += string.digits
        selected_sets.append(string.digits)
    if "punctuations" in types:
        pool += string.punctuation
        selected_sets.append(string.punctuation)

    if not selected_sets:
        raise ValueError("Choose at least one valid character type")
    if length < len(selected_sets):
        raise ValueError("Length is too short for the chosen types")


    password_chars = []
    for char_set in selected_sets:
        password_chars.append(secrets.choice(char_set))

    remaining = length - len(password_chars)
    for _ in range(remaining):
        password_chars.append(secrets.choice(pool))

    random.SystemRandom().shuffle(password_chars)
    return "".join(password_chars)



if __name__ == "__main__":
    print("************Welcome to the password generator************")

    character_length = 0
    LINE = "*" * 36
    while True:
        try:
            character_length=int(input("How long do you want your password to be(between 8 and 20)?"))

        except ValueError:
             print(LINE)
             print("ERROR CODE: Please enter a valid integer")
             print(LINE)
             continue

        if character_length > 20 or character_length < 8:
            print(LINE)
            print("ERROR CODE: Please enter a number between 8 and 20")
            print(LINE)
            continue

        print(LINE)
        print(LINE)
        print(f"{character_length} characters long password")
        print(LINE)
        break

    allowed_character_types = ["uppercase", "lowercase", "digits", "punctuations"]

    while True:
        print(LINE)
        character_type = input("What characters type do you want?(uppercase,lowercase,digits,punctuations)")
        print(LINE)

        character_type = list(set(character_type.lower().replace(",", " ").split()))
        print(LINE)
        print(f"Chosen character type(s): {character_type}")
        print(LINE)

        if not character_type:
            print(LINE)
            print("ERROR CODE: Please enter at least one valid character type")
            print(LINE)
            continue

        all_valid = True

        for item in character_type:
            if item not in allowed_character_types:
                print(f"ERROR CODE: {item} is not a valid type")
                all_valid = False

        if all_valid:
            break

    password = generate_password(character_length, character_type)

    print(LINE)
    print(f"your password is: {password}")
    print(LINE)










