def letter(value):
    """uppering!"""
    total = ""
    for i in value:
        if i.isupper():
            total += i
    return total


# minimum fix

def uppercase_letter(value):
    """"capitalize word"""
    return value.capitalize()
