t = int(input("Enter the number of test cases : "))

while (t > 0):
    string = input("Enter the string : ")

    # Checking if the alternate ends are different as we move towards the middle
    break_index = len(string)//2 #Assigning gibberish value to break_index
    
    for i in range(len(string)//2):
        if string[i] != string[-1-i]:
            # print("NO")
            continue
        elif string[i] == string[-1-i]:
            break_index = i
            break
    print(len(string[break_index : len(string)-break_index]))
