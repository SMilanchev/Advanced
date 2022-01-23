class HashTable:
    def __init__(self, capacity=5):
        self.array = [None] * capacity
        self.capacity = capacity
        self.length = 0

    def get(self, target_key, default=None):
        idx = self.hash(target_key)
        if self.array[idx] is None:
            return default
        key_values = self.array[self.hash(target_key)]
        for k, v in reversed(key_values):
            if k == target_key:
                return v

        return default


    def set(self, key, value):
        idx = self.hash(key)
        if self.array[idx] is None:
            self.array[idx] = []

        self.length += 1
        self.array[idx].append((key, value))
        percent_filled = self.length / self.capacity
        if percent_filled > 0.5:
            self.increase_size()

    def increase_size(self):
        new_table = HashTable(capacity=self.capacity * 2)
        for chain in self.array:
            if chain is None:
                continue
            for (k, v) in chain:
                new_table.set(k, v)

        self.array = new_table.array
        self.capacity = new_table.capacity

    def hash(self, key):
        return hash(key) % self.capacity
