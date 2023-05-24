from typing import List
import heapq


def maxScore(nums1: List[int], nums2: List[int], k: int) -> int:
    # Sort numbers in terms of nums2 since this has the larger impact on total value
    nums = sorted(zip(nums1, nums2), key=lambda x: x[1], reverse=True)
    heap = []

    curr_sum = 0
    max_found = 0

    for num in nums:
        num1, num2 = num
        curr_sum += num1

        # Push the current number into the heap
        heapq.heappush(heap, num1)

        # If the heap is already longer than k, pop the smallest value and keep the k largest
        if len(heap) > k:
            curr_sum -= heapq.heappop(heap)

        # Calculate the current total from the current sum and multiply by num2, then take the max of the prev vs curr
        if len(heap) == k:
            curr_tot = curr_sum * num2
            max_found = max(max_found, curr_tot)

    return max_found


maxScore([2,1,14,12], [11,7,13,6], 3)