import numpy as np

input_brackets = "((??))"
total = 0
n = input_brackets.count('(')+input_brackets.count('?')+1
m = len(input_brackets)
matrix = np.zeros((n, m), dtype=int)

if input_brackets[0] == '(' or input_brackets[0] == '?':
    matrix[1][0] = 1

for j in range(m-1):
    for i in range(n):
        print((i,j))
        if i < n-1 and input_brackets[j+1] == '(':
            matrix[i+1][j+1] += matrix[i][j]
        if input_brackets[j + 1] == '?':
            if i < n-1:
                matrix[i + 1][j + 1] += matrix[i][j]
            if i >= 1:
                matrix[i - 1][j + 1] += matrix[i][j]
        elif i >= 1 and input_brackets[j + 1] == ')':
            matrix[i-1][j+1] += matrix[i][j]

total = matrix[0][m-1]
print(matrix)
print(total)