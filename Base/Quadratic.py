import cmath

a = float(input("input a:"))
b = float(input("input b:"))
c = float(input("input c:"))

d = (b ** 2) - 4 * a * c

# 两种答案
res1 = (-b + cmath.sqrt(d))/(2 * a)
res2 = (-b - cmath.sqrt(d))/(2 * a)

print("result is {0} and {1} ". format(res1, res2))