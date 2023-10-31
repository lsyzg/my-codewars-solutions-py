def get_count(sentence):
    vowel_count = 0
    for i in sentence:
        if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
            vowel_count += 1
        else:
            continue
    return vowel_count