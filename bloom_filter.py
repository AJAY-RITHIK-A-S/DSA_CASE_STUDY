
class BloomFilter:
    def __init__(self, size, hash_count):
        self.size = size
        self.hash_count = hash_count
        self.bits = set()

    def get_index(self, username, i):
        hash1 = 0

        for ch in username:
            hash1 = (31 * hash1 + ord(ch)) & 0xFFFFFFFF

        hash2 = hash1 ^ (hash1 >> 16)

        if hash2 == 0:
            hash2 = 1

        combined = hash1 + i * hash2
        return combined % self.size

    def add(self, username):
        for i in range(self.hash_count):
            self.bits.add(self.get_index(username, i))

    def might_contain(self, username):
        for i in range(self.hash_count):
            if self.get_index(username, i) not in self.bits:
                return False
        return True

    def get_size(self):
        return self.size

    def get_hash_count(self):
        return self.hash_count

    def get_set_bit_count(self):
        return len(self.bits)
