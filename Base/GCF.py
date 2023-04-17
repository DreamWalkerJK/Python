def getGCF(a, b):
    if a > b:
        small = b
    else:
        small = a

    for i in range(1, small + 1):
        if((a % i == 0) and (b % i == 0)):
            gcf = i
    
    return gcf

a = 1
b = 1
while(a >= 1 and b >= 1):
    a = int(input("Enter the first interger until you enter 0:"))
    b = int(input("Enter the second interger until you enter 0:"))
    if a <= 0 or b <= 0:
        break
    gcf = getGCF(a,b)
    print("{0} and {1} gcf is {2}".format(a,b,gcf))