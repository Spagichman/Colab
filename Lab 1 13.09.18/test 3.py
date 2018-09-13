# y = a*x**2 + b*x + c = 0

print("input a")
a = int(input())
print("input b")
b = int(input())
print("input c")
c = int(input())

d = b**2 - 4 *a *c
if d > 0:
    print("x1 = ", (-b + d**0.5)/(2*a))
    print("x2 = ", (-b - d**0.5)/(2*a))
elif d  == 0:
    print("x1 = ", (-b)/(2*a))
else:
    print("Нет корней")

##print("hello")
##input()
