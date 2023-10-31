def solution(s):
    lst = []
    for i in s:
        if i.isupper():
            lst.append(" " + i)
        else:
            lst.append(i)
    return ''.join(lst)