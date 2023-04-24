class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.sort(key=lambda x: x != 0, reverse=True)

        """
        Lower-level solution
        
        # Keeps total count of zeros. Used to track offset for in-place mod and append remaining zeros at end.
        zero_count = 0
        
        # Loop through number in list and pop from list if it is a zero, then incrememnt zero_count
        for index in range(len(nums)):
            if nums[index - zero_count] == 0:
                nums.pop(index - zero_count)
                zero_count += 1

        # Append number of zeros that were found
        nums += [0] * zero_count
        """