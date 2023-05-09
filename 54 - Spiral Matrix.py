from typing import List


def spiralOrder(matrix: List[List[int]]) -> List[int]:
    round: int = 0
    spiral: list = []

    if len(matrix[0]) == 1:
        return [x for index in matrix for x in index]

    while len(spiral) < (len(matrix) * len(matrix[0])):
        spiral += matrix[round][round: len(matrix[0])-round]

        for x in matrix[round+1: -(round+1)]:
            spiral += [x[-(round+1)]]

        if len(spiral) < (len(matrix) * len(matrix[0])):
            spiral += reversed(matrix[-(round+1)][round: len(matrix[0])-round])

        if len(spiral) < (len(matrix) * len(matrix[0])):
            for x in reversed(matrix[round+1: -(round+1)]):
                spiral += [x[round]]

        round += 1

    return spiral


spiralOrder([[2,3,4],[5,6,7],[8,9,10],[11,12,13],[14,15,16]])

# Suggestions for optimization: Remove slicing functions, which add time on top