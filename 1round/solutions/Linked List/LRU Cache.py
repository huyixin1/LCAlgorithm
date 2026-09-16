class LRUCache:
    # need to review
    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = collections.OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.makeRecent(key) # renew the recently used key
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache.keys():
            self.cache[key] = value
            self.makeRecent(key)
            return

        if len(self.cache) >= self.cap:
            oldestKey = next(iter(self.cache)) # what is this
            self.cache.pop(oldestKey)
        self.cache[key] = value
    

    def makeRecent(self, key):
        value = self.cache.pop(key)
        self.cache[key] = value


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)