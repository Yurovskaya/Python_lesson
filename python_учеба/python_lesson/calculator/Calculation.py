def sum (num_1, num_2):
    return num_1 + num_2


def sub(num_1, num_2):
    return num_1 - num_2


def mult(num_1, num_2):

     return num_1 * num_2


def div(num_1, num_2):
    try:
     return num_1 / num_2
    except ZeroDivisionError:
        print("Делить на 0 нельзя")


def exponentiation(num_1, num_2):
    return num_1 ** num_2
