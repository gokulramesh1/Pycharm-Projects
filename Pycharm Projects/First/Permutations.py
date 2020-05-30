
def perm(lst):
    if len(lst) == 0:
        return []
    elif len(lst) == 1:
        return [lst]
    else:
        a = []
        for i in range(len(lst)):
            x = lst[i]
            xs = lst[:i] + lst[i+1:]
            for p in perm(xs):
                a.append([x] + p)
        return a


b = [1, 2, 3, 4, 5]
for permutation in perm(b):
    print(permutation)
