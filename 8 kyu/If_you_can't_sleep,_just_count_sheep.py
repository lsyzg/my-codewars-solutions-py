def count_sheep(n):
    num = 1
    lst = []
    if n == 0:
        return ''
    for i in range(n):
        lst.append(f"{num} sheep...")
        num += 1
    return ''.join(lst)