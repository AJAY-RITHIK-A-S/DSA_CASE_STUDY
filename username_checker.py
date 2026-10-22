
from username_service import UsernameService
from test_service import TestService


def main():
    username_service = UsernameService()
    test_service = TestService(username_service)

    while True:
        print("\n=== USERNAME AVAILABILITY CHECKER ===")
        print("1. Register a username")
        print("2. Check username availability")
        print("3. Load 100,000 demo usernames")
        print("4. Find a false positive")
        print("5. Display statistics")
        print("6. Display all registered usernames")
        print("0. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            username = input("Enter username: ")
            username_service.register_username(username)

        elif choice == "2":
            username = input("Enter username to check: ")
            username_service.check_username(username)

        elif choice == "3":
            test_service.load_demo_data()

        elif choice == "4":
            test_service.find_false_positive()

        elif choice == "5":
            username_service.show_statistics()

        elif choice == "6":
            username_service.display_usernames()

        elif choice == "0":
            print("Program ended.")
            break

        else:
            print("Enter a valid menu number.")


if __name__ == "__main__":
    main()
