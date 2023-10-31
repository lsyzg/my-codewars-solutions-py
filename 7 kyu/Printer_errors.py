def printer_error(s):
    lst = ['a','b','c','d','e','f','g','h','i','j','k','l','m']
    error_count = 0
    length = len(s)
    for i in s:
        if i in lst:
            continue
        else: 
            error_count = error_count + 1
    return f"{error_count}/{length}"