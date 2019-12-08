#03 bubble sort
def swapper(numbers, a, b):
    temporary=numbers[a]
    numbers[a]=numbers[b]
    numbers[b]=temporary
    return numbers
def issorted(numbers):
    for i, n in enumerate(numbers):
        if i != len(numbers) - 1:
            if numbers[i] < numbers[i + 1]:
                pass
            else:
                return False
    return True
l = [12, 1, 68, 3, 102, 99, 6]
while not issorted(l):
    for i in range(len(l) - 1):
        num1 = l[i]
        num2 = l[i + 1]
        if num2 < num1:
            l = swapper(l, i, i+1)
print(l)
