


def function_1():
    print('initializing function 1')

def function_2(number=None):
    print('initializing function 2')
    print('Doing something')
    if number==None:
        number = 0
    else:
        pass

    result = number + 55

    return result