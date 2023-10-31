def duplicate_count(text):
    lower = text.lower()
    lst = []
    num = 0
    for i in lower:
        lst.append(i)
    for x in lower:
        if lst.count(x) > 1:
            num += 1
            lst = list(filter(x.__ne__, lst)) 
        else:
            continue
    return num