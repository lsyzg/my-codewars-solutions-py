def is_isogram(word):
    letter = []
    clean = word.lower()
    if clean.isalpha():
        for i in clean:
            if i in letter:
                return False
            letter.append(i)
        return True
    if clean == "":
        return True
    else:
        return False