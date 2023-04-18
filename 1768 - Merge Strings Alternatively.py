class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        new_word = ""

        diff = len(word1) - len(word2)

        if diff == 0:
            for i in range(len(word1)):
                new_word += word1[i] + word2[i]
        elif diff < 0:
            for i in range(len(word1)):
                new_word += word1[i] + word2[i]
            new_word += word2[i + 1:]
        else:
            for i in range(len(word2)):
                new_word += word1[i] + word2[i]
            new_word += word1[i + 1:]

        return new_word