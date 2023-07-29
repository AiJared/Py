def is_multiple(n, m):
    i = 2
    if n == m * i:
        return True
    return False

a = is_multiple(7, 2)
print(a)