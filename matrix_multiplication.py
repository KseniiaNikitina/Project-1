A = [[1, 4, 7], [3, 6, 2], [1, 2, 1]]
B = [[2, 2, 1], [2, 1, 4], [9, 2, 8]]

result = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for i in range(len(A)):
    for j in range(len(B[0])):
        for k in range(len(B)):
            result[i][j] += A[i][k] * B[k][j]

for row in result:
    print(row)