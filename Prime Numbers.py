
def is_prime(num):
    if num <=1:
        return False

    for i in range (2, num):
        if num%i == 0:
            return False
    return True
# def is_prime(n):
#     return n>1 and all(n%i for i in range(2, n))

def get_primes(seq):
    list_of_primes = filter (lambda x: is_prime(x), seq)
    for el in list_of_primes:
        yield el




print(list(get_primes([2, 4, 3, 5, 6, 9, 1, 0])))