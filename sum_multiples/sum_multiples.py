class Solution(object):
    """
    Input:
    - upper limit
    - list of positive integers

    Output:
    Sum of all numbers between 0 and upper limit (exclusive) that are
    multiples of any number in the list

    Examples:
    Input: (10, [2, 3])
    Output: 32

    Assumptions:
    - numbers will be input in correct format (i.e. positive whole numbers)
    """

    def sum_multiples(self, limit, numbers):
        numbers = set(numbers)      # take unique values and sort ascending
        multiples = []
        while numbers != set():
            number = numbers.pop()
            multiplier = 1
            multiple = number * multiplier
            while multiple < limit:
                if multiple not in multiples:
                    multiples.append(multiple)
                if multiple in numbers:
                    numbers.remove(multiple)
                multiplier += 1
                multiple = number * multiplier
        return sum(multiples)



# Testing
sol = Solution()
print(sol.sum_multiples(10, [2,3]))
print(sol.sum_multiples(0, [3,5]))
print(sol.sum_multiples(1000, []))
print(sol.sum_multiples(1000, [3,5]))
