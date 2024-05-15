import string


def is_ascii(s: str):
    """
    Return True if string s is ASCII, False otherwise.
    :param s: string to be checked
    :return: True if string is ASCII, False otherwise
    """
    return all(char in string.printable for char in s)
