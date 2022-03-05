from __future__ import annotations

""" Solving https://leetcode.com/problems/add-two-numbers/
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val: int=0, nextNode: ListNode=None):
        self.val = val
        self.next = nextNode


class Solution(object):
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        tempL1 = l1
        tempL2 = l2

        carryOver = 0

        node = ListNode()
        firstNode = node
        while True:
            if tempL1 is not None:
                first = tempL1.val
                tempL1 = tempL1.next
            else:
                first = 0

            if tempL2 is not None:
                second = tempL2.val
                tempL2 = tempL2.next
            else:
                second = 0

            digit = (first + second + carryOver) % 10
            node.val = digit

            carryOver = 1 if (first + second + carryOver >= 10) else 0

            if tempL1 is not None or tempL2 is not None:
                nextNode = ListNode()
                node.next = nextNode
                node = nextNode
            else:
                if carryOver == 1:
                    nextNode = ListNode(1)
                    node.next = nextNode
                break

        return firstNode


if __name__ == '__main__':
    pass
