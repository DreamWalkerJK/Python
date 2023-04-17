def getLCM(a, b):
    if a > b:
        greater = a
        smaller = b
    else:
        greater = b
        smaller = a

    while(True):
        if((greater % a == 0) and (greater % b == 0)):
            lcm = greater
            break
        else:
            greater += 1
    return lcm

a = 1
b = 1
while(a >= 1 and b >= 1):
    a = int(input("Enter the first interger until you enter 0:"))
    b = int(input("Enter the second interger until you enter 0:"))
    if a <= 0 or b <= 0:
        break
    lcm = getLCM(a,b)
    print("{0} and {1} lcm is {2}".format(a,b,lcm))