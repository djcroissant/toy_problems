class Node(object):
    def __init__(self, data=None, next_node=None):
        self.data=data
        self.next_node = next_node

    def __str__(self):
        string = ""
        node = self
        while not node == None:
            string += str(node.data)
            string += " -> "
            node = node.next_node
        string = "(" + string[:-4] + ")"
        return string

class Solution(object):
    def add_two_numbers(self, l1, l2, carry=False):
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
        node1 = l1
        node2 = l2

        if node1 == None and node2 == None:
            # Catch base case for recursive call
            if carry == True:
                num1 = 0
                num2 = 0
            else:
                return None
        elif node1 == None:
            num1 = 0
            num2 = node2.data
        elif node2 == None:
            num1 = node1.data
            num2 = 0
        else:
            num1 = node1.data
            num2 = node2.data

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
        new_l1 = node1.next_node
        new_l2 = node2.next_node


        new_node = Node(num_sum, self.add_two_numbers(new_l1, new_l2, carry))

        return new_node




sol = Solution()
l1 = Node(2, Node(4, Node(3, None)))
l2 = Node(5, Node(6, Node(4, None)))

sum_list = sol.add_two_numbers(l1, l2)

print(sum_list)
