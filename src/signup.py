import json

class Signup:
    
    def __init__(self):
        self.users = self.load_users()

    def load_users(self):
        try:
            with open("users.json", "r") as file:
                return json.load(file)
        except FileNotFoundError:
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

        with open("users.json", "w") as file:
            json.dump(self.users, file)

        return self.users

