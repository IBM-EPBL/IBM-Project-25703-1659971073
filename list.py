A = [35, 30, 52, 30, 112, 38, 99]

def insertIntoList(value, ind):
    A.insert(ind, value)

def removeFromList(value):
    A.remove(value)

def appendToList(value):
    A.append(value)

def sortList():
    A.sort()

def popFromList():
    A.pop()

def reverseList():
    A.reverse()

def printList():
    print(A)

print("Choose any operation given below:\n")
print("a. Insert\nb. Delete\nc. Insert at end\nd. Sort the list\ne. Reverse the list\nf. Delete last value\ng. Print")
choice = str(input("Please enter choice: "))

if choice == 'a':
    value, ind = map(int, input("Enter value and index: ").split())
    insertIntoList(value, ind)
    printList()

elif choice == 'b':
   value = int(input("Enter a value: "))
   removeFromList(value)
   printList()

elif choice == 'c':
    print("Enter a value: ")
    value = int(input())
    appendToList(value)
    printList()
    
elif choice == 'd':
    sortList()
    printList()

elif choice == 'e':
    reverseList()
    printList()

elif choice == 'f':
    popFromList()
    printList()

elif choice == 'g':
    printList()

else:
   print("Invalid input")