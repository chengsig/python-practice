def flip_case(str, letter):
    """given a string and a letter, if the string contains any letter in them, swap the letter case"""
    result = ""
    for s in str:
        if s == letter or s == letter.swapcase():
            s = s.swapcase()
        result += s
    return result 