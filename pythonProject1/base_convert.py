def convert(num, b):
    if num == 0:
        return ""
    else:
        return convert(num // b, b) + str(num % b)


