class ListNode(object):
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        string = ""
        node = self
        while not node == None:
            string += str(node.val)
            string += " -> "
            node = node.next
        string = "(" + string[:-4] + ")"
        return string

class Solution(object):
    def addTwoNumbers(self, l1, l2, carry=False):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode

        Assumptions:
            * l1 and l2 are non-empty
            * numbers are non-negative
            * digits stored in reverse order
            * l1 and l2 can be different lengths

        Test Case:
            Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
            Output: (7 -> 0 -> 8)
            Explanation: 342 + 465 = 807
        """
        # Redefineing from LeetCode for clarity
        node1 = l1
        node2 = l2

        if node1 == None and node2 == None and carry == False:
            # Catch base case for recursive call
            return None
        elif node1 == None and node2 == None:
            # carry must be True
            num1 = 0
            num2 = 0
        elif node1 == None:
            num1 = 0
            num2 = node2.val
        elif node2 == None:
            num1 = node1.val
            num2 = 0
        else:
            num1 = node1.val
            num2 = node2.val

        num_sum = num1 + num2

        if carry == True:
            # carry set by previous call
            num_sum += 1

        if num_sum >= 10:
            # Set carry for next call
            carry = True
        else:
            carry = False

        num_sum = num_sum % 10

        new_node = ListNode(
            num_sum,
            self.addTwoNumbers(node1.next, node2.next, carry)
        )

        return new_node




sol = Solution()
l1 = ListNode(2, ListNode(4, ListNode(3, None)))
l2 = ListNode(5, ListNode(6, ListNode(4, None)))

sum_list = sol.addTwoNumbers(l1, l2)

print(sum_list)
