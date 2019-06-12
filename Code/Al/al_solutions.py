def is_even(a):
    if a in range(0, 101, 2):
        return True
    elif a in range(1, 100, 2):
        return False
    else:
        return ("Why did you choose that number?")

def is_even_mod(a):
    # if a % 2 == 0:
    #     return True
    # return False
    return a % 2 == 0

def opposite(a, b):
    if str(a)[0] == '-':
        # if str(b)[0] != '-':
        #     return True
        # else:
        #     return False
        return str(b)[0] != '-':
    else:
        if str(b)[0] != '-':
            return False
        else:
            return True


def remainder_div_two(in_num):
    # if in_num % 2 == 0:
    #     return 0
    # if in_num % 2 == 1:
    #     return 1
    return in_num % 2
