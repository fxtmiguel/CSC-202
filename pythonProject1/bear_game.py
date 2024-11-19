def bear(n):
    if n == 42:
        return True
    elif n < 42:
        return False
    elif n % 5 == 0:
        n -= 42
    elif (n % 3 == 0 or n % 4 == 0) and (int(str(n)[-1]) * int(str(n)[-2])) != 0:
        b = str(n)
        c = int(b[-1]) * int(b[-2])
        n -= c
    elif n % 2 == 0:
        n -= n // 2
    try:
        if bear(n):
            return True
        else:
            return False
    except RecursionError:
        return False

