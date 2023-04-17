def isNum(s):
    try:
        float(s)
        return True
    except ValueError as err:
        pass

    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass

    return False

a = ''
while(a != 'End'):
    a = input("Enter the string until you enter end:") 
    print(isNum(a))