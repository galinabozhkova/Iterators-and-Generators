class take_skip:
    def __init__(self, step, count):
        self.step = step
        self.count = count-1
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count <0:
            raise StopIteration
        number = self.current
        self.count -=1
        self.current += self.step
        return number


numbers = take_skip(2, 6)

for number in numbers:
    print(number)