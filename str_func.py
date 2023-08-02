def letter(value):
    """uppering letters"""
    total = ""
    for i in value:
        if i.isupper():
            total += i
    return total
