class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Easy Python solution
        return Counter(nums).most_common(1)[0][0]

        # Lower-level solution
        # counter_dict: dict = dict()
        #
        # for num in nums:
        #     try:
        #         counter_dict[num] += 1
        #     except KeyError:
        #         counter_dict[num] = 1
        #
        # return max(counter_dict, key=counter_dict.get)
