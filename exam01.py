def is_palin(word):
    return word[::-1]==word[::1]

print is_palin("ana")
