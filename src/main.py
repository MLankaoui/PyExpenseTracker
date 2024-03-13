from signup import Signup


def main():
    welcome()
    signup_message()
    signup_instance = Signup()
    first_name, last_name, user_name = signup_instance.create_user()
    signup_instance.add_user(first_name, last_name, user_name)
    signup_instance.display_users()


def welcome():
    print("===PyExpenseTracker===")

def signup_message():
    print("please sign up to continue!")

main()