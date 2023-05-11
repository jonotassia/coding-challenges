from typing import List


def maxUncrossedLines(nums1: List[int], nums2: List[int]) -> int:
    # Dynamic programming solution using LCS
    m, n = len(nums1), len(nums2)

    dp_array = [[0 for j in range(n + 1)] for i in range(m + 1)]

    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                dp_array[i][j] = 0
            elif nums1[i - 1] == nums2[j - 1]:
                dp_array[i][j] = dp_array[i - 1][j - 1] + 1
            else:
                dp_array[i][j] = max(dp_array[i - 1][j], dp_array[i][j - 1])

    return dp_array[m][n]

    # Space Optimized approach
    # m, n = len(nums1), len(nums2)
    #
    # # If nums2 is longer than nums1, flip all the variables in order to minimise code in for loop
    # if m < n:
    #     m, n, nums1, nums2 = n, m, nums2, nums1
    #
    # # Populate a dp_array to keep track of max connections at teach index
    # # It should be the size of the shorter of the two arrays to minimise space complexity
    # crossed_lines: list = [0] * (n + 1)
    #
    # for i in range(1, m + 1):
    #     prev = 0
    #     for j in range(1, n + 1):
    #         curr = crossed_lines[j]
    #
    #         # Each index in the dynamic programming array should be incremented if the j-1 and i-1 index
    #         # match in their respective arrays
    #         if nums2[j - 1] == nums1[i - 1]:
    #             crossed_lines[j] = prev + 1
    #         # If there is not a match, then return whatever is bigger: The crossed lines including the previous
    #         # constraints, or the crossed lines with the current constraints
    #         else:
    #             crossed_lines[j] = max(curr, crossed_lines[j - 1])
    #
    #         prev = curr
    #
    #         # As this steps through the 2 arrays, the dynamic programming array (crossed_lines) will be incremented
    #         # at the index associated with the current value of j
    #         # Essentially, the goal is to bubble up the max number of uncrossed lines to the final index of the array
    #
    # return crossed_lines[n]


maxUncrossedLines([1, 4, 2], [1, 2, 4])
