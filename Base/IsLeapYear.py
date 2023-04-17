def JudgeIsLeapYear(year):
    if ((year % 4) == 0 and (year % 100)) or ((year % 400) == 0):
        print('{0} is leap year'.format(year))
    else:
        print('{0} is not leap year'.format(year))

year = 1
while(year >= 0):
    year = int(input("input a  an integer :"))
    JudgeIsLeapYear(year)