def find_uniq(arr):
    similar = None
    index = 0
    for x in arr:
        if arr[index] == arr[index + 1]:
            similar = arr[index]
        else:
            index += 1
            continue
    for i in arr:
        if i != similar:
            return i
        else:
            continue