"""
refactor
"""

import base64
import json
import random
import string


def load_data():
    try:
        with open("data.json", "r") as file:
            data = json.load(file)
        data = run_func(data, decode_text)
        return data
    except FileNotFoundError:
        print("File not found, createing new file...")
        return {}
    except json.JSONDecodeError:
        print("File in corrupted, creating new file...")
        return {}


def write_data(data):
    data = run_func(data, encode_text)
    try:
        with open("data.json", "w") as file:
            json.dump(data, file, indent=4)
    except Exception as error:
        print(f"Error happened while saving the data: {error}")


def list_all_entries(data):
    if not data:
        print("No entries found!")
        return

    for website in data:
        print(
            f"{website}:\n\tUsername: {data[website]['username']}\n\tPassword: {data[website]['password']}"
        )


def search_website(data):
    website = input("Enter the website name: ")
    if website in data:
        print(
            f"{website}:\n\tUsername: {data[website]['username']}\n\tPassword: {data[website]['password']}"
        )
    else:
        print(f"{website} not found!")


def add_entry(data):
    website = input("Enter the website name: ")

    if website in data:
        print(f"{website} is already saved!")
        return data

    username = input("Enter the username: ")
    password = input("Enter the password: ")

    data[website] = {"username": username, "password": password}

    return data


def delete_entry(data):
    entry = input("Enter the website name: ")
    if entry not in data:
        print(f"{entry} not found!")
        return data

    data.pop(entry)
    print(f"{entry} is deleted!")

    return data


def generate_random_password(length=12):
    chars = string.ascii_letters + string.digits + string.punctuation
    password = "".join(random.choice(chars) for _ in range(length))

    return password


# usernames and passwords encoding and decoding
def encode_text(text):
    """encode 1 username or password at a time"""
    return base64.b64encode(text.encode()).decode()


def decode_text(text):
    """encode 1 username or password at a time"""
    return base64.b64decode(text.encode()).decode()


def run_func(data, func):
    """runs a function(encode/decond) over the data. used to encode or decode all data at once"""
    for website in data:
        username = data[website]["username"]
        password = data[website]["password"]

        data[website]["username"] = func(username)
        data[website]["password"] = func(password)

    return data


data = load_data()

while True:
    print(
        "\nPlease chose what to do",
        "[1] List all entries",
        "[2] Search for an entry",
        "[3] Add new entry",
        "[4] Delete an entry",
        "[5] Generate random password",
        "[6] Exit",
        sep="\n",
    )
    user_input = input(">>> ")

    if user_input == "1":
        list_all_entries(data)

    elif user_input == "2":
        search_website(data)

    elif user_input == "3":
        data = add_entry(data)
        write_data(data)

    elif user_input == "4":
        data = delete_entry(data)
        write_data(data)

    elif user_input == "5":
        password = generate_random_password()
        print(password)

    elif user_input == "6":
        print("Thanks for using the app")
        quit()

    else:
        print("Please enter a valid choice")
