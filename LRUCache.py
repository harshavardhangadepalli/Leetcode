class LRUCache:
    counter = 0

    def __init__(self, capacity: int):
        self.d = dict()
        self.c = capacity

    def get(self, key: int) -> int:
        LRUCache.counter += 1
        if key in self.d:
            self.d[key][1] = LRUCache.counter
            return self.d[key][0]
        return -1

    def put(self, key: int, value: int) -> None:
        LRUCache.counter += 1
        if key in self.d:
            self.d[key][0] = value
            self.d[key][1] = LRUCache.counter
            return
        if len(self.d) == self.c:
            # we need to remove some element here
            to_be_r = self.get_element()
            self.d.pop(to_be_r, None)
            self.d[key] = [value, LRUCache.counter]
        else:
            self.d[key] = [value, LRUCache.counter]

    def get_element(self):
        least = float('inf')
        curr_element = -1
        for i in self.d:
            if self.d[i][1] < least:
                least = self.d[i][1]
                curr_element = i
        return curr_element
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
