
def rotateImage(a):
    n = len(a[0])
    for i in range(n // 2 + n % 2):
        for j in range(n // 2):
            tmp = a[n - 1 - j][i]
            a[n - 1 - j][i] = a[n - 1 - i][n - j - 1]
            a[n - 1 - i][n - j - 1] = a[j][n - 1 - i]
            a[j][n - 1 - i] = a[i][j]
            a[i][j] = tmp
    return a


rotateImage([[1, 2, 3],
             [4, 5, 6],
             [7, 8, 9]])
