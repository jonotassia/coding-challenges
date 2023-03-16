# See here for working solution https://leetcode.com/problems/house-robber/solutions/2910165/python-c-rust-iterative-recursive-solutions-explained-bonus-one-liner/?page=2

class Solution:
    def rob(self, nums: list[int]) -> int:
        # Create a dictionary of indices for each number with lists to account for dups, then sort for largest values
        list_positions = dict()
        for index, num in enumerate(nums):
            try:
                list_positions[num].append(index)
            except KeyError:
                list_positions[num] = [index]

        nums.sort(reverse=True)

        # Check for largest values by comparing list and dict, tracking accepted values
        # O(n) speed and size, worst case speed O(n^2)
        values_seen = dict()
        selected_values = list()
        selected_index = list()

        for num in nums:
            # Get index for this number, using number of times selected to grab index counter
            try:
                value_count = values_seen[num]
                values_seen[num] += 1
            except KeyError:
                value_count = 0
                values_seen[num] = 1

            index = list_positions[num][value_count]

            # Loop over indices associated with this number and add to list if not adjacent
            if index - 1 not in selected_index and index + 1 not in selected_index:
                selected_index.append(index)
                selected_values.append(num)

        return sum(selected_values)


if __name__ == "__main__":
    sol = Solution()
    sol.rob([2, 3, 2])
