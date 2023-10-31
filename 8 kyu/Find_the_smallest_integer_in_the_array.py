def find_smallest_int(arr):
    x = arr[0]
    for i in arr:
        if x > i:
            x = i
    return x