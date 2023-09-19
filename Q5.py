class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.isEmpty():
            print("underflow")
            return None
        return self.items.pop()

    def peek(self):
        if self.isEmpty():
            return None
        return self.items[-1]

    def isEmpty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def returnList(self):
        return self.items


stack = Stack()

while True:

    print("1. Push")
    print("2. Pop")
    print("3. Display")
    print("4. Quit")

    choice = int(input("Enter your choice : "))

    if choice == 1:
        item = int(input("Enter the item to be pushed : "))
        stack.push(item)
    elif choice == 2:
        item = stack.pop()
        if item is not None:
            print("Popped item is", item)
    elif choice == 3:
        returnList = stack.returnList()
        print("Stack contains : ", end="")
        for item in returnList:
            print(item, end=" ")
        print()

    elif choice == 4:
        break
    else:
        print("Wrong choice")
    print()
