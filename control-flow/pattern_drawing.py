size = int(input("Enter the size of the pattern:"))
row = size

while(row>0):
    for x in range(1,size+1):
        print("*", end="")
    print()
    row -= 1 