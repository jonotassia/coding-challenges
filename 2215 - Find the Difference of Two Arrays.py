def findDifference(nums1: list[int], nums2: list[int]) -> list[list[int]]:
    # Using set subtraction
    set1 = set(nums1)
    set2 = set(nums2)

    return [list(set1 - set2), list(set2 - set1)]

    # # Using dict lookup and set comprehension + lists
    # dict1 = {i: True for i in nums1}
    # dict2 = {i: True for i in nums2}
    #
    # list1 = list({i for i in dict1.keys() if i not in dict2.keys()})
    # list2 = list({i for i in dict2.keys() if i not in dict1.keys()})
    #
    # return [list1, list2]


findDifference([1, 2, 3], [2, 4, 6])