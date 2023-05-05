from collections import deque


def maxVowels(s: str, k: int) -> int:
    vowels: list[str] = ["a", "e", "i", "o", "u"]
    max_vowels: int = 0

    # Initialise a list with the positions that each vowel appears
    vowels_indices: list = [i for i, letter in enumerate(s) if letter in vowels]
    vowel_queue: deque = deque()

    # Move through index list in windows of k
    for i in vowels_indices:
        vowel_queue.append(i)

        if vowel_queue[-1] - vowel_queue[0] >= k:
            vowel_queue.popleft()

        max_vowels = max(len(vowel_queue), max_vowels)

    return max_vowels

    # # Naive approach
    # for i in range(len(s) - k + 1):
    #     vowel_count: int = 0
    #
    #     for letter in s[i:i + k]:
    #         if letter in vowels:
    #             vowel_count += 1
    #
    #     max_vowels = max(vowel_count, max_vowels)
    #
    # return max_vowels


maxVowels("weallloveyou", 7)