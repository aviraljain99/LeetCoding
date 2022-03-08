"""
Solves https://leetcode.com/problems/flood-fill/
"""

from typing import List
import queue

### Simple application of Breadth First Search
# Only move 4 directionally, up, down, left and right, and only move if it is
# the same color


def floodFill(image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
    q = queue.Queue()
    dimX = len(image)
    dimY = len(image[0])
    existingColor = image[sr][sc]

    q.put((sr, sc))

    def validDimensions(r, c) : return 0 <= r < dimX and 0 <= c < dimY
    visited = set()

    while not q.empty():
        cell = q.get()

        if cell in visited:
            continue

        image[cell[0]][cell[1]] = newColor
        visited.add(cell)

        for direction in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
            newCell = (cell[0] + direction[0], cell[1] + direction[1])

            if (newCell not in visited) and \
                    validDimensions(newCell[0], newCell[1]) \
                    and image[newCell[0]][newCell[1]] == existingColor:
                q.put(newCell)

    return image


if __name__ == "__main__":
    print(floodFill([[1, 1, 1], [1, 1, 0], [1, 0, 1]], 1, 1, 2))
