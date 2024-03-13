users = {
    "firs_name": [],
    "last_name":[],
    "user_name": []
}

class Signup:
    
    def create_user(self):
        first_name = input("enter your first name: ")
        last_name = input("Enter your last name: ")
        user_name = input("enter you user_name: ")

        return (first_name, last_name, user_name)

    def add_user(self, first_name, last_name, user_name):
        users["first_name"].append(first_name)
        users["last_name"].append(last_name)
        users["user_name"].append(user_name)


        return (users)
