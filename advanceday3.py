# eShoper
def add(x, y):
    return x + y


# 2
def multiply(x, y):
    return x * y


# 3
def is_even(x):
    if x % 2 == 0:
        return True
    else:
        return False


# 4

def find_max(given_list):
    if not given_list:
        raise ValueError("empty list")
    return max(given_list)
