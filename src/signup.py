import json
import os

class Signup:

    cwd = os.getcwd()
    file_path = os.path.join(cwd, "users.json")
    
    def __init__(self):
        self.users = self.load_users()

    def load_users(self):
        try:
            with open("users.json", "r") as file:
                return json.load(file)
        except FileNotFoundError:
            return {"first_name": [], "last_name": [], "user_name": []}
        except Exception as e:
            print("Error loading users:", e)
            return {"first_name": [], "last_name": [], "user_name": []}

    def create_user(self):
        first_name = input("Enter your first name: ")
        last_name = input("Enter your last name: ")
        user_name = input("Enter your user name: ")
        return (first_name, last_name, user_name)

    def add_user(self, first_name, last_name, user_name):
        self.users["first_name"].append(first_name)
        self.users["last_name"].append(last_name)
        self.users["user_name"].append(user_name)

        print(f"Writing the following data to users.json: {self.users}")

        try:
            with open(self.file_path, "w") as file:
                json.dump(self.users, file)
        except Exception as e:
            print("Error writing to users.json:", e)

        return self.users
