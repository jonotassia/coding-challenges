class Solution:
    def reverseString(self, s: str) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # Iterative solution
        for i in range(len(s)//2):
            s[i], s[-i-1] = s[-i-1], s[i]

        # Pythonic solution
        s[:] = s[::-1]


if __name__ == "__main__":
    sol = Solution()

    s = "Hello"
    sol.reverseString(s)
    print(s)