
class TestService:
    DEMO_USERS = 100_000

    def __init__(self, username_service):
        self.username_service = username_service

    def load_demo_data(self):
        service = self.username_service
        added = 0

        for i in range(1, self.DEMO_USERS + 1):
            username = f"user{i:06d}"

            if username not in service.database:
                service.database.add(username)
                service.filter.add(username)
                added += 1

        print(f"{added} demo usernames added.")
        print(
            "Total registered usernames:",
            len(service.database)
        )

    def find_false_positive(self):
        service = self.username_service

        print("Searching for a false positive...")

        for i in range(1, 1_000_001):
            username = f"newuser{i}"

            if (
                username not in service.database
                and service.filter.might_contain(username)
            ):
                print("Test username:", username)
                service.check_username(username)
                return

        print("No false positive found in this test range.")
        print("Try loading demo data or increasing the search range.")
