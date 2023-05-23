import heapq
from typing import List


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.stream = []
        self.index = k
        heapq.heapify(self.stream)

        for item in nums:
            self.add(item)

    def add(self, val: int) -> int:
        if len(self.stream) < self.index:
            heapq.heappush(self.stream, val)

        elif self.stream[0] < val:
            heapq.heappop(self.stream)
            heapq.heappush(self.stream, val)

        return self.stream[0]


# Your KthLargest object will be instantiated and called as such:
obj = KthLargest(3, [4, 5, 8, 2])
obj.add(3)
obj.add(5)
obj.add(10)
obj.add(9)
obj.add(4)
