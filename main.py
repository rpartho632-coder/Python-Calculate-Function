# Addition function
def add(*args):
    return sum(args)

a = input("Enter the number separated by + sin: ").split("+")
b = [float(i) for i in a]

result = add(*b)
print("Result:", result)