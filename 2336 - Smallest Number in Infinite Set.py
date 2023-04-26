import heapq


class SmallestInfiniteSet:
    def __init__(self):
        """
        Self.list: A heap that we use to capture ONLY numbers that are smaller than the current minimum number
        Self.smallest: The smallest number in the 1 -> Ininite series that has not been added back
        """
        self.list = []
        self.smallest = 1

    def popSmallest(self) -> int:
        # If there is anything in the heap, pop and return that as it is guaranteed to be the smallest.
        if self.list:
            return heapq.heappop(self.list)

        # If there is nothing in the heap, then the next smallest element is incremented and returned-1
        self.smallest += 1
        return self.smallest - 1

    def addBack(self, num: int) -> None:
        # Add the element to the heap if it is smaller than self.smallest.
        # We don't care about adding anything bigger than self.smallest as it is already contained in the "infinite"
        if num < self.smallest and num not in self.list:
            heapq.heappush(self.list, num)

# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)