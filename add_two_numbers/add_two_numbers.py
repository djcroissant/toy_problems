# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, data=None, next_node=None):
        self.data=data
        self.next_node = next_node

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode

        Assumptions:
            * l1 and l2 are non-empty
            * numbers are non-negative
            * digits stored in reverse order

        Test Case:
            Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
            Output: (7 -> 0 -> 8)
            Explanation: 342 + 465 = 807
        """


sol = Solution()
l1 = (ListNode())
