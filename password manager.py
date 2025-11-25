import json


def load_data():
    try:
        with open("data.json", "r") as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        print("File not found, createing new file...")
        return {}
    except json.JSONDecodeError:
        print("File in corrupted, creating new file...")
        return {}


def write_data(data):
    try:
        with open("data.json", "w") as file:
            json.dump(data, file, indent=4)
    except Exception as error:
        print(f"Error happened while saving the data: {error}")


def list_all_entries(data):
    if not data:
        print("No entries found!")
        return

    for entry in data:
        print(
            f"{entry} - Username: {data[entry]['username']} - Password: {data[entry]['password']}"
        )


def search_website(data):
    website = input("Enter the website name: ")
    if website in data:
        print(
            f"{website} - Username: {data[website]['username']} - Password: {data[website]['password']}"
        )
    else:
        print(f"{website} not found!")


def add_entry(data):
    website = input("Enter the website name: ")

    if website in data:
        print(f"{website} is already saved!")
        return data

    username = input("Enter the user name: ")
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


data = load_data()


while True:
    print(
        "Please chose what to do",
        "[1] List all entries",
        "[2] Search for an entry",
        "[3] Add new entry",
        "[4] Delete an entry",
        "[5] Exit",
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
        print("Thanks for using the app")
        break

    else:
        print("Please enter a valid choice")
