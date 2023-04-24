# Information on Bit Manipulation: https://leetcode.com/problems/sum-of-two-integers/solutions/84278/a-summary-how-to-use-bit-manipulation-to-solve-problems-easily-and-efficiently/
# Information on how to solve: https://leetcode.com/problems/sum-of-two-integers/solutions/167931/Solution-with-ACTUAL-explanation-(how-you-would-work-this-out)/
# Information on Masks (also see comment below): https://leetcode.com/problems/sum-of-two-integers/solutions/489210/read-this-if-you-want-to-learn-about-masks/?languageTags=python3

class Solution:
    def getSum(self, a: int, b: int) -> int:
        # Create a 32-bit mask since Python does not cap at 32-bits
        mask = 0xFFFFFFFF

        while (b & mask) > 0:
            """
             When a and b are both 1, then we've reached the max in this digit place. 
             To account for this, we carry the 1 to the next digit place.
            """
            carry = (a & b) << 1

            """
            If a and b are NOT the same, a will equal 1. 
            if they were the same, a will equal 0. In this situation, carry would be equal to 1.
            We assign carry to b and continue the operation until the mask is exceeded or b is 0 
            """
            a = a ^ b
            b = carry

        """
        Return a if there was no further carry at the end of the loop (ie b > 0).
        If there was a carry remaining, use the mask to ensure the value does not go beyond the size threshold.
        Masks will set any values beyond a specific place to 0 when you & it with another value.
        This ensures that the value of a does not continue carrying to infinity, instead converging on a 32 bit number.
        https://stackoverflow.com/questions/10493411/what-is-bit-masking
        """
        return a & mask if b > 0 else a