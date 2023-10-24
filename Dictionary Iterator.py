class dictionary_iter:

    def __init__(self, my_iter):
        self.my_iter = my_iter
        self.keys = []
        for el in self.my_iter.keys():
            self.keys.append(el)
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count >= len(self.my_iter):
            raise StopIteration
        self.count += 1
        return (self.keys[self.count - 1], self.my_iter[self.keys[self.count - 1]])


result = dictionary_iter({1: "1", 2: "2"})

for x in result:
    print(x)
