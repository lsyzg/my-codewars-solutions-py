def reverse_seq(n):
    lst = []
    for i in range(n):
        lst.append(i)
    lst.append(n)
    new = list(reversed(lst))
    del new[-1]
    return new