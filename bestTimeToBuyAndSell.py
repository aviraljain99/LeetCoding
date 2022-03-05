from typing import List

""" Solves https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
"""


def maxProfit(prices: List[int]) -> int:
    """
    :type prices: List[int]
    :rtype: int
    """
    maxDiff = 0
    minVal = 10 ** 6
    minValIndex = 0
    maxVal = -1
    maxValIndex = 0
    after = True  # Has the maxVal occured after minVal?

    for i, price in enumerate(prices):
        if price < minVal:
            minVal = price
            minValIndex = i
        if price > maxVal:
            maxVal = price
            maxValIndex = i

        after = maxValIndex >= minValIndex

        if after:
            if maxVal - minVal > maxDiff:
                maxDiff = maxVal - minVal
        else:
            maxVal = price

    return maxDiff


if __name__ == "__main__":
    prices = [7, 1, 5, 3, 6, 4]
    print(maxProfit(prices))
