def fibonacci():
    zero = 0
    start = 1
    yield zero
    yield start

    while True:
        yield start + start -1
        start +=1


generator = fibonacci()
for i in range(5):
    print(next(generator))