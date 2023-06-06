from typing import List


def stoneGameII(piles: List[int]) -> int:
    n = len(piles)

    # Initialise an array with dimensions (player, n+1 (size of array), n+1 (largest possible M value)
    # Initialised to values of -1 so we know whether these parameters have been encountered before
    dp = [[[-1] * (n + 1) for y in range(n + 1)] for z in range(2)]

    def optimal(player, i, m):
        # If we are beyond the length of the array, return 0
        if i == n:
            return 0

        # Check if the dynamic programming array has been filled in with a value yet and return it if it exists
        if dp[player][i][m] != -1:
            return dp[player][i][m]

        # Set the value to an extremely large number if player 1, whose goal is to find a minimum num of points for p0
        # Set the value to -1 if player 2, whose goal is to find a maximum num of points for p0
        result = 1000000 if player else -1
        score = 0

        # Loop through the piles array up to either 2*m (AKA Max X) or n-1, whichever is smaller to account for being
        # Close to the end of an array
        for x in range(1, min(2 * m, n - i) + 1):
            score += piles[i + x - 1]

            # If player 0, find the max value between the current result and the score + the result of
            # the next subproblem in the array
            if player == 0:
                result = max(result, score + optimal(1, i + x, max(m, x)))
            # If player 1, find the min value for player 0 between the current result and the next subproblem in array
            else:
                result = min(result, optimal(0, i + x, max(m, x)))

        # Memoize the results
        dp[player][i][m] = result
        return result

    return optimal(0, 0, 1)


stoneGameII([1])