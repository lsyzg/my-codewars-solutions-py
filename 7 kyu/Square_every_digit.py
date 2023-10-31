def square_digits(num):
    lst = []
    numstring = str(num)
    for i in numstring:
        lst.append(str(int(i)**2))
    return int(''.join(lst))