class Solution(object):
    """
    Given a 32 bit signed integer, reverse the digits of an integer.

    Examples:
    Input: 123
    Output: 321

    Input: -123
    Output: -321

    Input: 120
    Output: 21

    Input: 1
    Output: 1

    Assumption: integer will not have leading 0's
    """

    def reverse_integer(self, num_in):
        """
        Pseudo code:

        Input = signed integer
        Output = reversed integer

        if < 0:
            set a flag
            change flag from 1 to -1
            multiply by flag

        convert to string,
        reverse sequence,
        strip leading zeros,
        convert to int,
        multiply by flag

        Refactor to check for length
        """
        if abs(num_in) > 2**32 / 2 - 1 or num_in == 0:
            return 0

        flag = 1
        if num_in < 0:
            flag = -1
            num_in *= -1

        num_out = int(str(num_in)[::-1] * flag

        if abs(num_out) > 2**32 / 2 - 1:
            return 0


        return num_out


# Testing
sol = Solution()
print(sol.reverse_integer(123))
print(sol.reverse_integer(-123))
print(sol.reverse_integer(120))
print(sol.reverse_integer(-120))
print(sol.reverse_integer(9))
print(sol.reverse_integer(-9))
print(sol.reverse_integer(2**32))
print(sol.reverse_integer(2**32 + 1))
