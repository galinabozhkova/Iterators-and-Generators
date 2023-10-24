class sequence_repeat:

    def __init__(self, sequence, number):
        self.sequence = sequence
        self.number = number
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count+1 > self.number:
            raise StopIteration
        index = self.count
        self.count += 1
        #return self.sequence[index%len(self.sequence)]
        if index > len(self.sequence)-1:
            index -= len(self.sequence)
        return self.sequence[index]






result = sequence_repeat('abc', 5)

for item in result:
    print(item, end='')

