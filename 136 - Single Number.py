class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        num_dict: dict = dict()

        for i in nums:
            try:
                num_dict[i] += 1
            except KeyError:
                num_dict[i] = 1

        for key, value in num_dict.items():
            if value < 2:
                return key