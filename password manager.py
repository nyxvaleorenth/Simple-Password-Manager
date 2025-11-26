# text encoding
import base64

# save data into a file
import json

# random password generation
import random
import string


# --------------- load and save data ---------------
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


# --------------- main functions ---------------
def list_all(data):
    """list all data entries"""
    if not data:
        print("No entries found!")
        return

    border()
    for entry in data:
        print(f"{entry}:")
        print(f"    Username: {data[entry]['username']}")
        print(f"    Password: {data[entry]['password']}")
    border()


def search(data):
    """search for a specific entry in data"""
    border()
    entry = input("Enter the website name: ")
    if entry in data:
        print(f"{entry}:")
        print(f"    Username: {data[entry]['username']}")
        print(f"    Password: {data[entry]['password']}")
    else:
        print(f"{entry} not found!")
    border()


def add(data):
    """add a new entry to data"""
    border()
    entry = input("Enter the website name: ")

    if entry in data:
        print(f"{entry} already exists!")
        border()
        return data

    username = input("Enter the username: ")
    password = input("Enter the password: ")

    data[entry] = {"username": username, "password": password}

    print(f"{entry} added successfully!")
    border()

    return data


def delete(data):
    """delete entry from data"""
    border()
    entry = input("Enter the website name: ")

    if entry not in data:
        print(f"{entry} not found!")
        border()
        return data

    data.pop(entry)
    print(f"{entry} deleted successfully!")

    return data


# --------------- encode and decode ---------------
# --------------- random password generation ---------------
# --------------- text decoration ---------------
def border():
    """Draws a simple line of '='"""
    print("\n" + "=" * 60 + "\n")
