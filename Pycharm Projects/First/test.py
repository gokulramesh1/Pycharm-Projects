import random
a = [1, 3, 5, 6, 13, 24, 31, 33, 56, 78, 98, 121, 236, 543, 789]
random.shuffle(a)


def insertion_sort(arr):

    i = 1
    while i < len(arr):
        for x in range(i, 0, -1):
            if arr[x] < arr[x-1]:
                arr[x], arr[x-1] = arr[x-1], arr[x]
            else:
                break
        i += 1
    return arr


print(a)
print(insertion_sort(a))

