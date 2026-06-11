class LRUCache:

    def __init__(self, capacity: int):
        self.capacity=capacity
        self.d={}

    def get(self, key: int) -> int:
        if key not in self.d:

            return -1
        
        a=self.d.pop(key)
        self.d[key]=a
        return self.d[key]


        

    def put(self, key: int, value: int) -> None:
        if key in self.d:
            a=self.d.pop(key)
            self.d[key]=a
        
        elif len(self.d)==self.capacity:
            first_key = next(iter(self.d))
            self.d.pop(first_key)

        self.d[key]=value
        
