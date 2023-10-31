def find_needle(haystack):
    pos = 0
    for i in haystack:
        if i == 'needle':
            return f"found the needle at position {pos}"
        else:
            pos += 1