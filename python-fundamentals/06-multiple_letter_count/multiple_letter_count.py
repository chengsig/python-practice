def multiple_letter_count(str):

    count = {}

    for letter in str:
        count[letter] = count.get(letter, 0) + 1

    return count