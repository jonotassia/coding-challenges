from typing import List


def maxProfit(prices: List[int]) -> int:
    # Peak-Valley Method
    local_min: int = prices[0]
    local_max: int = prices[0]
    max_sum: int = 0

    for i in range(1, len(prices)):
        diff = prices[i] - prices[i - 1]

        # If the slope is negative (ie we've just passed a peak), add local diff to sum, then reset local min and max
        if diff < 0:
            max_sum += local_max - local_min

            local_min = prices[i]
            local_max = prices[i]

        local_min = min(local_min, prices[i])
        local_max = max(local_max, prices[i])

    # Add the final local diff to sum
    max_sum += local_max - local_min

    return max_sum

    # Space-optimized (too-slow)
    # n = len(prices)
    # dp = [0] * (n)
    #
    # max_dp = 0
    #
    # for i in range(1, n):
    #     for j in range(1, n):
    #         if prices[i] > prices[i-1]:
    #             dp[i] = max_dp + prices[i] - prices[i-1]
    #         else:
    #             dp[i] = max_dp
    #
    #     max_dp = max(dp)
    #
    # return dp[n-1]

    # Dynamic programming (too-slow)
    # n = len(prices)
    # dp = [[0 for _ in range(n + 1)] for i in range(n + 1)]
    #
    # for i in range(len(prices)):
    #     for j in range(len(prices) + 1):
    #         if i == 0 or j == 0:
    #             dp[i][j] = 0
    #         elif prices[i - 1] < prices[i]:
    #             dp[i][j] = dp[i - 1][j - 1] + prices[i] - prices[i - 1]
    #         else:
    #             dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])
    #
    # return dp[n-1][n]


maxProfit([7,6,4,3,1])
