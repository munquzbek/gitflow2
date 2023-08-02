def letter(value):
    """uppering letters"""
    total = ""
    for i in value:
        if i.isupper():
            total += i
    return total


def uppercase_letter(value):
    """"capitalize word"""
    return value.capitalize()
