a = [[54, 63, 81, 64, 35, 56, 46, 23],
     [44, 65, 67, 38, 24, 32, 14, 40],
     [13, 25, 39, 34, 45, 66, 20, 45],
     [96, 87, 56, 35, 34, 45, 49, 22],
     [34, 34, 35, 60, 16, 75, 60, 49],
     [65, 36, 37, 23, 12, 78, 45, 60]]


def peak(mat):

    n = len(mat)
    m = len(mat[0])

    if m == 1:
        return max([mat[x][0] for x in range(n)])

    j = m // 2
    col = [mat[x][j] for x in range(n)]
    maxi = 0
    maxnum = 0
    for i, num in enumerate(col):
        if num > maxnum:
            maxnum = num
            maxi = i

    for x in [-1, 1]:
        try:
            if mat[maxi][j] < mat[maxi][j+x]:
                return peak([x[j+1:] for x in mat])
        except IndexError:
            pass

    return mat[maxi][j]


print(peak(a))






