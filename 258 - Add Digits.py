def addDigits(num: int) -> int:
    # Iterative
    while len(str(num)) > 1:
        sum: int = 0

        for i in range(len(str(num))):
            # Add the next digit in the number, removing previous digits from the final position.
            # Then adjust for current digit position by dividing by the correct power of 10
            sum += (num % 10 ** (i + 1) - sum) // 10 ** i

        num = sum

    return num

    # Recursive
    # if not num:
    #     return 0
    #
    # power = len(str(num))
    #
    # while power > 1:
    #     prev_dig = addDigits(num % 10)
    #     num = (num % 10 ** power - prev_dig) // 10 + prev_dig
    #     power = len(str(num))

    # return num


addDigits(88)