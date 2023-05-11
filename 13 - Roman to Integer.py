def romanToInt(s: str) -> int:
    roman: dict = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }

    total: int = roman[s[0]]

    for i in range(1, len(s)):
        if s[i] in ["V", "X"] and s[i - 1] == "I":
            total = total - roman["I"] * 2

        elif s[i] in ["L", "C"] and s[i - 1] == "X":
            total = total - roman["X"] * 2

        elif s[i] in ["D", "M"] and s[i - 1] == "C":
            total = total - roman["C"] * 2

        total = total + roman[s[i]]

    return total


romanToInt("MCMXCIV")