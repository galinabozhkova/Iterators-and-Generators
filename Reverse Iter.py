class reverse_iter:

    def __init__(self, my_iter):
        self.my_iter = my_iter
        self.start = len(my_iter)-1


    def __iter__(self):
        return self

    def __next__(self):

        if self.start <0:
            raise StopIteration()

        index = self.start
        self.start -= 1
        return self.my_iter[index]


reversed_list = reverse_iter([1, 2, 3, 4])

for item in reversed_list:
    print(item)










