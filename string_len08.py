def main(s):
    """
    Given variable type string s. Return the character in the middle.
    If the length is even, return two characters in the middle.

    Args:
        s: str
    Returns:
        str: answer
    """
    length = len(s)
    middle_index = length // 2

    if length % 2 == 0:
        return s[middle_index - 1 : middle_index + 1]
    else:
        return s[middle_index]
print(main())