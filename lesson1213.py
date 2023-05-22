users = []

def register():
    username = input("Enter a username: ")
    password = input("Enter your password: ")

    if not validate_password(password):
        print("Invalid password. Password should have at least 6 characters.")
        return

    users.append(username + ":" + password)
    print("Registration successful!")

def validate_password(password):
    return len(password) >= 6

def login():
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    for user in users:
        stored_username, stored_password = user.split(":")
        if stored_username == username and stored_password == password:
            print("Login successful!")
            return

    print("Invalid username or password.")

def main():
    while True:
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            register()
        elif choice == "2":
            login()
        elif choice == "3":
            break
        else:
            print("Invalid choice. Try again.")