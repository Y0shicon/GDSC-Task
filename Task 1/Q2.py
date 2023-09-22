n = int(input())
count = 0
for i in range(1, n+1):
    for j in range(1, i+1):
        print(count%n+1, end=" ")
        count += 1
    print()