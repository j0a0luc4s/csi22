def mult(a, b):
    if len(a[0]) != len(b):
        raise ValueError("Wrong dimensions")

    result = [[0 for j in range(len(b[0]))] for i in range(len(a))]

    for i in range(len(a)):
        for j in range(len(b[0])):
            for k in range(len(b)):
                    result[i][j] = result[i][j] + a[i][k] * b[k][j]

    return result
