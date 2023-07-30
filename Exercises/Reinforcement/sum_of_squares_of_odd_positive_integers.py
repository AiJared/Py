def sum_of_squares(n):
    for i in range(n):
        while i % 2 != 0:
            squares = [i**2]
            i += 1
    return sum(squares)

result = sum_of_squares(4)
print(result)