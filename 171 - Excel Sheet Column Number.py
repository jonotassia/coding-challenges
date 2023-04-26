class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        value: int = 0

        for i, letter in enumerate(reversed(columnTitle)):
            # Convert the letter to the numeric value of its ASCII char
            # Subtract 64 from it, then multiply by 26 to the power of i to account for digit placement
            value += (ord(letter) - 64) * 26 ** i

        return value