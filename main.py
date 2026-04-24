from auth_service import AuthService

auth = AuthService()

while True:
    print("\n===== AUTH SYSTEM ====")
    print("1. Register user")
    print("2. Login ")
    print("3. Logout")
    print("4. Recover User ID (via Email)")
    print("5. Delete User")
    print("6. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        email = input("Enter Email: ")
        password = input("Enter password: ")

        auth.register_user(email, password)

    elif choice == "2":
        user_id = input("Enter your user ID: ")
        password = input("Enter correct password here: ")

        auth.login(user_id, password)

    elif choice == "4":
        email = input("Enter your email: ")

        auth.get_user_id_by_email(email)

    elif choice == "5":
        user_id = input("Enter user ID to delete user: ")
        auth.delete_user(user_id)
    
    elif choice == "6":
        print("Goodbye")
        auth.close()
        break
    
    else:
        print("Invalid choice, try again")