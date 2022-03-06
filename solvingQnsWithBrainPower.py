from typing import List

""" Solves https://leetcode.com/problems/solving-questions-with-brainpower/
"""

def mostPoints(questions: List[List[int]]) -> int:
    """
    :type questions: List[List[int]]
    :rtype: int
    """
    # Use dynamic programming for this question
    # If we know what optimal decision needs to be made at index i, then
    # at index i - 1, we know whether to solve i - 1 and then questions[i - 1 + questions[i - 1][2] + 1] or if we need to skip
    # it and move on to the index i

    maxPointsAtIndex = []

    for i, question in enumerate(reversed(questions)):
        # Points from solving the current problem
        solveCurrentPoints = question[0]
        solveCurrentPoints += maxPointsAtIndex[i - question[1] - 1] if i - question[1] - 1 >= 0 else 0

        solveNextPoints = maxPointsAtIndex[i - 1] if i - 1 >= 0 else 0
        maxPointsAtIndex.append(max(solveNextPoints, solveCurrentPoints))

    return maxPointsAtIndex[-1]


if __name__ == "__main__":
    print(mostPoints([[3, 2], [4, 3], [4, 4], [2, 5]]))
