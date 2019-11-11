print("Hello World")


def myfunc(*args):
    result = 0
    for x in args:
        result += x
    print(result)


myfunc(8, 9, 10)
