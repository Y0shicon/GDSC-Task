test = int(input())
while (test > 0):
    string1, string2 = input().split()
    for char in string1:
        if char not in string2:
            print("NO")
            break
    else:
        print("YES")
    test -= 1
