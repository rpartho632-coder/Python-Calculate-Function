# Addition function
def add(*args):
    return sum(args)

a = input("Enter the number separated by + sign: ").split("+")
b = [float(i) for i in a]

result = add(*b)
print("Addition Result:", result)

# Subtraction function
def sub(*args):
    if not args:
        return 0
    result = args[0]
    for i in args[1:]:
        result -= i
    return result
user_input = input("Enter the number separated by - sign: ").strip()
if not user_input:
    print("Subtraction Result:", 0)
else:
    a = user_input.split("-")
    b = [float(i) for i in a]
    final_result = sub(*b)

    if final_result.is_integer():
        print("Subtraction Result:", int(final_result))
    else:
        print("Subtraction Result:", final_result)