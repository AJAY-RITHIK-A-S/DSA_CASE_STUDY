
from bloom_filter import BloomFilter


class UsernameService:
    FILTER_SIZE = 1_000_000
    HASH_COUNT = 3

    def __init__(self):
        self.filter = BloomFilter(
            self.FILTER_SIZE, self.HASH_COUNT
        )
        self.database = set()

        self.register_username("ajay123")
        self.register_username("rithik45")
        self.register_username("student2026")

    @staticmethod
    def normalize(username):
        return username.strip().lower()

    def register_username(self, username):
        username = self.normalize(username)

        if not username:
            print("Username cannot be empty.")
            return False

        if username in self.database:
            print("Username is already registered.")
            return False

        self.filter.add(username)
        self.database.add(username)

        print("Username registered successfully.")
        return True

    def check_username(self, username):
        username = self.normalize(username)

        if not username:
            print("Username cannot be empty.")
            return

        if not self.filter.might_contain(username):
            print("Username is AVAILABLE.")
            print("Bloom Filter confirms it is not registered.")

        elif username in self.database:
            print("Username is NOT AVAILABLE.")
            print("It is already registered.")

        else:
            print("Bloom Filter gave a FALSE POSITIVE.")
            print("Database verification: username is AVAILABLE.")

    def show_statistics(self):
        print("\n--- Project Statistics ---")
        print("Registered usernames:", len(self.database))
        print("Bloom Filter bits:", self.filter.get_size())
        print("Hash functions:", self.filter.get_hash_count())
        print("Bits currently set:", self.filter.get_set_bit_count())
        print(
            "Approximate filter size:",
            self.filter.get_size() // 8,
            "bytes"
        )

    def display_usernames(self):
        if not self.database:
            print("No usernames registered.")
            return

        print("\n--- Registered Usernames ---")

        for username in sorted(self.database):
            print(username)
