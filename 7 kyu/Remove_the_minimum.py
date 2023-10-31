def remove_smallest(numbers):
    lst = []
    
    for i in numbers:
        lst.append(i)
    if len(numbers) == 0:
        return numbers
    else:
        lst.remove(min(lst))
    return lst