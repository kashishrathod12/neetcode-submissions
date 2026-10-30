class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.stack = []
        self.store = {}

    def get(self, key: int) -> int:
        if key not in self.store:
            return -1
        if key in self.stack:
            self.stack.remove(key)
        self.stack.append(key)
        return self.store[key]

    def put(self, key: int, value: int) -> None:
        if key in self.store:
            self.store[key] = value
            if key in self.stack:
                self.stack.remove(key)
            self.stack.append(key)
            return
        if len(self.stack) >= self.capacity:
            oldest = self.stack.pop(0)
            del self.store[oldest]
        self.stack.append(key)
        self.store[key] = value