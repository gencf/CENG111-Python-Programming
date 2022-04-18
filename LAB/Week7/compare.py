epsilon=0.000001
a = eval(input("expression 1: "))
b = eval(input("expression 2: "))
difference = abs(a - b)
print(difference < epsilon)
