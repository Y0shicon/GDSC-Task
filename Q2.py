''' 
For n = 5, the output should be
1
2 3
4 5 1
2 3 4 5
1 2 3 4 5
'''

n = int(input("Enter the number of rows : "))
count = 0
for i in range(1, n+1):
    for j in range(1, i+1):
        print(count%n+1, end=" ")
        count += 1
    print()