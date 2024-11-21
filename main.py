def f(x):
    y = -x ** 2 + 3 * x - 2
    return y

h = 0.1
x = 1
print("# # # f(x) = -x^2 + 3x - 2 from a=1 to b=2 # # #")
while x <= 2:
    print("When x =", x, "=> f(x) =", f(x))
    x += h

first = f(1)
last = f(2)

s = 1+h
middlesum = 0

while s < 2:
    middlesum += f(s)
    s += h

print("# # # Example of Trapezium Rule Values # # #")
print("First height: ", first)
print("Last Height: ", last)
print("Middle Sum: ", middlesum)

intergration = (h/2)*(first + last + 2*middlesum)
error = ((1/6) - intergration)/(1/6)*100

print("Intergration is approximately: ", intergration)
print("True value of intergration is 1/6")
print("Therefore the error is ", error, "%")

quit()