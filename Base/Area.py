# 三角形
a = float(input("input first side: "))
b = float(input("input second side: "))
c = float(input("input third side: "))
s = (a + b + c) / 2 # 计算半周长
area = (s*(s-a)*(s-b)*(s-c)) ** 0.5 # 计算三角形面积
print("triangle's area: %0.2f" %area)

# 圆
r = float(input("input radius:"))
PI = 3.142
area = PI * (r ** 2)
print("circle's area: %0.6f" %area)