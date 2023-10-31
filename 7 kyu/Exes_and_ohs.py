def xo(s):
    countx = 0
    counto = 0
    s = s.lower()
    for i in range(len(s)):
        if s[i] == "x":
            countx += 1
        if s[i] == "o":
            counto += 1
    if counto == countx:
        return True
    else:
        return False