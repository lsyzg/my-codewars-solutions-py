def digitize(n):
    lst = []
    n = str(n)
    for i in n:
        i = int(i)
        lst.append(i)
    lst.reverse()
    return lst