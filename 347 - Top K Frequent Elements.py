from collections import Counter
from typing import List


def topKFrequent(nums: List[int], k: int) -> List[int]:
    # Counter approach
    ints = Counter(nums)
    return [x[0] for x in ints.most_common(k)]


topKFrequent([1, 1, 1, 2, 2, 3], 2)
