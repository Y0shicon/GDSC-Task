test = int(input("Enter the number of test cases : "))
while (test > 0):
    string1, string2 = input("Enter the two strings : ").split()
    for char in string1:
        if char not in string2:
            print("NO")
            break
    else:
        print("YES")
    test -= 1
