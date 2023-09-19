n = int(input("Enter the number of rows and columns : "))

# Take values for matrix 1
print("Enter the values for matrix 1 : ")
matrix1 = []
for i in range(n):
    row = input().split()
    matrix1.append(row)

# Take values for matrix 2
print("Enter the values for matrix 2 : ")
matrix2 = []
for i in range(n):
    row = input().split()
    matrix2.append(row)

# Multiply the matrices
result = []
for i in range(n):
    row = []
    for j in range(n):
        row.append(0)
    result.append(row)

for i in range(n):
    for j in range(n):
        for k in range(n):
            result[i][j] += int(matrix1[i][k]) * int(matrix2[k][j])

# Calculate the sum of the diagonal elements
sum = 0
for i in range(n):
    sum += result[i][i]

# Print the sum
print("The sum of the diagonal elements is", sum)
