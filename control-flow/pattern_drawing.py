size = int(input("Enter the size of the pattern:"))
row = size

while(size>0):
    for x in range(1,row+1):
        print("*", end="")
    print()
    size -= 1 