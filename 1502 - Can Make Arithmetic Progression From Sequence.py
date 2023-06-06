from typing import List


def canMakeArithmeticProgression(arr: List[int]) -> bool:
    arr.sort()

    diff = arr[0] - arr[1]

    for i in range(1, len(arr)):
        if arr[i-1] - arr[i] == diff:
            continue

        return False

    return True

val = canMakeArithmeticProgression([3,5,1])
val
