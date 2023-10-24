#
# from itertools import permutations
# def possible_permutations(seq):
#     perm = permutations(seq)
#     for el in perm:
#         yield list(el)
    def all_permutation(seq):
        if len(seq) == 0:
            return []
        if len(seq) == 1:
            return [seq]
    l = []
    for i in range(len(seq)):
        el = seq[i]
        perm = seq[:i]+ seq[i+1:]
        for p in all_permutation(perm):
            l.append([el] + p)
    return l


def possible_permutations (seq):
    perms = all_permutation(seq)
    for el in perms:
        yield el


[print(n) for n in possible_permutations([1, 2, 3])]
