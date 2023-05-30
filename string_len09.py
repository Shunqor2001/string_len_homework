def main(num1, num2):
    """
    Given two non-negative integers, num1 and num2 represented as string.
    Return the sum of num1 and num2 as a string.

    Args:
        num1: str
        num2: str
    Returns:
        str: answer
    """
    n1 = int(num1)
    n2 = int(num2)


    result = n1 + n2

    
    answer = str(result)

    return answer
print(main())