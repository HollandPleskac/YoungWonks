#02 Recursion
##def function():
##    print("function called")
##    function()
##function()

##import time
##def fibonacci_sequence(a,b):
##    print(a)
##    time.sleep(1)
##    fibonacci_sequence(b,a+b)
##fibonacci_sequence(1,1)


##def factorial(n):
##    if n == 1:
##        return 1
##    return factorial(n-1) * n
##n = int(input("Number? "))
##print(factorial(n))

def pascal(layer):
    if len(layer)>10:
        return
    for e in layer:
        print(e, end=' ')
    print()
    new = []
    for n in range(len(layer)-1):
        new.append(layer[n]+layer[n+1])
    new = [1] + new + [1]
    pascal(new)
print(1)
pascal([1,1])

