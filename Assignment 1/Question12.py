def relu(x):
    if x >= 0:
        return x
    else:
        return 0


x = float(input("Enter a number: "))


result = relu(x)


print("ReLU(", x, ") =", result)