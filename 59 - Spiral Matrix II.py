from typing import  List


def generateMatrix(n: int) -> List[List[int]]:
    loops: int = 0
    i: int = 1
    matrix: List[List[int]] = [[0]*n for i in range(n)]

    while i <= n**2:
        start: int = loops

        for x in range(loops, n - loops):
            matrix[loops][x] = i
            i += 1

        start += 1

        for y in range(start, n - loops):
            matrix[y][n - start] = i
            i += 1

        for x in range(loops, n - start):
            matrix[n - start][-x-start+loops-1] = i
            i += 1

        start += 1

        for y in range(loops, n - start):
            matrix[-y-start+loops][loops] = i
            i += 1

        loops += 1

    return matrix


generateMatrix(5)
