row = int(input("Enter the Number of Rows: "))
num = 1
i = 1  
while i <= row:
    column = 1 
    while column <= i:
        print(num, "", end="")
        num += 1
        column += 1  
    print() 
    i += 1