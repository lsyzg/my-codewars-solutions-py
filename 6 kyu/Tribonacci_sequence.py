def tribonacci(signature, n):
    times = 0
    if n == 0:
        return []
    for i in range(n):
        signature.append(sum(signature[times : times + 3]))
        times += 1
    return signature[:-3]