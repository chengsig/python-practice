def is_palindrome(str):
    """returns true if str is a palindrome"""
    lower_str = str.replace(" ", "").lower()
    return lower_str == lower_str[::-1]