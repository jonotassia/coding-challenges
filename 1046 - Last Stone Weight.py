class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # Validation checking for stones size
        if not stones:
            return 0

        while len(stones) > 1:
            # Sort stones in ascending order so that stones pop off end rather than beginning (O(1))
            stones.sort()

            # If equal in size, pop off 2 collided stones
            if stones[len(stones) - 1] == stones[len(stones) - 2]:
                stones.pop()
                stones.pop()
            # Otherwise, pop off 2 collided stones and append difference to list
            else:
                new_stone = abs(stones[len(stones) - 1] - stones[len(stones) - 2])
                stones.pop()
                stones.pop()
                stones.append(new_stone)

        if not stones:
            return 0
        else:
            return stones[0]