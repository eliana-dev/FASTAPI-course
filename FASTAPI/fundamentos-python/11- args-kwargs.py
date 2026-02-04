# kwargs= keyword argument


def big_function(*args, **kwargs):
    print(args)
    print(kwargs)


print(big_function(1, 2, 3, 4, 5, 6, num1=77, num2=100))
