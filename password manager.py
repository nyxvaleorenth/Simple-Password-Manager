# text encoding
import base64

# save data into a file
import json

# random password generation
import random
import string


# --------------- load and save data ----------------------------------------------
def load():
    """loads the data from a data.json file. returns a dict with the data"""
    try:
        with open("data.json", "r") as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        print("Data file not found. Creating new one...")
        return {}
    except json.JSONDecodeError:
        print("File is corrupted. Creating new one...")
        return {}
    except Exception as error:
        print(f"Error: {error}")


def write(data):
    """write data(dict) into data.json file"""
    try:
        with open("data.json", "w") as file:
            json.dump(data, file, indent=4)
    except Exception as error:
        print(f"Error: {error}")


# --------------- main functions ---------------------------------------------------
def list_all(data):
    """list all data entries"""
    if not data:
        print("No entries found!")
        return

    for entry in data:
        print(f"{entry}:")
        print(f"    Username: {data[entry]['username']}")
        print(f"    Password: {data[entry]['password']}")


def search(data):
    """search for a specific entry in data"""
    entry = input("Enter the website name: ")
    if entry in data:
        print(f"\n{entry}:")
        print(f"    Username: {data[entry]['username']}")
        print(f"    Password: {data[entry]['password']}")
    else:
        print(f"\n{entry} not found!")


def add(data):
    """add a new entry to data"""
    entry = input("Enter the website name: ")

    if entry in data:
        print(f"{entry} already exists!")
        return data

    username = input("Enter the username: ")
    password = input("Enter the password: ")

    data[entry] = {"username": username, "password": password}

    print(f"{entry} added successfully!")

    return data


def delete(data):
    """delete entry from data"""
    entry = input("Enter the website name: ")

    if entry not in data:
        print(f"{entry} not found!")
        return data

    data.pop(entry)
    print(f"{entry} deleted successfully!")

    return data


# --------------- encode and decode ---------------------------------------------
def encode(text):
    """encode giving text"""
    return base64.b64encode(text.encode()).decode()


def decode(text):
    """decode giving text"""
    return base64.b64decode(text.encode()).decode()


def run_encode(data):
    """runs encode over the whole data"""
    for entry in data:
        username = data[entry]["username"]
        password = data[entry]["password"]

        data[entry]["username"] = encode(username)
        data[entry]["password"] = encode(password)

    return data


def run_decode(data):
    """runs decode over the whole data"""
    for entry in data:
        username = data[entry]["username"]
        password = data[entry]["password"]

        data[entry]["username"] = decode(username)
        data[entry]["password"] = decode(password)

    return data


# --------------- random password generation ------------------------------------
# --------------- text decoration -----------------------------------------------
def border():
    """Draws a simple line of '='"""
    print("\n" + "=" * 60 + "\n")


# --------------- main loop -----------------------------------------------------

data = load()
data = run_decode(data)

while True:
    border()
    print(
        "Please chose what to do",
        "[1] List all entries",
        "[2] Search for an entry",
        "[3] Add new entry",
        "[4] Delete an entry",
        "[5] Generate random password",
        "[6] Exit",
        sep="\n",
    )
    user_input = input(">>> ")
    border()

    if user_input == "1":
        border()
        list_all(data)
        border()

    elif user_input == "2":
        border()
        search(data)
        border()

    elif user_input == "3":
        border()
        data = add(data)
        data = run_encode(data)
        write(data)
        data = run_decode(data)
        border()

    elif user_input == "4":
        border()
        data = delete(data)
        data = run_encode(data)
        write(data)
        data = run_decode(data)
        border()

    elif user_input == "5":
        pass

    elif user_input == "6":
        print("Thanks for using the app!")
        border()
        quit()

    else:
        border()
        print("Please enter a valid choice")
        border()
