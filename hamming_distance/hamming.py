class Solution:
    def get_binary(self, n):
        # docs: https://docs.python.org/3/library/string.html#formatspec
        return "{0:b}".format(n)

    def hamming_distance(self, x, y):
        """
        This function takes two integers, x and y, as input and returns the
        hamming distance between them. The hamming distance is an integer
        indicating the number of bits that are different b/w the two
        numbers.

        Limits: 0 <= x, y <= 2^31

        Examples
        ========================
        x = 1, y = 4
        1 (0 0 0 1)
        4 (0 1 0 0)
        hamming_distance = 2

        x = 2, y = 3
        2 (0 0 1 0)
        3 (0 0 1 1)
        hamming_distance = 1
        """
        # Assign larger number to x
        if y > x:
            x,y = y,x
        # Convert integers to binary
        x = self.get_binary(x)
        y = self.get_binary(y)
        # split x so `compare` piece is same length as y
        x_compare = x[-len(y):]
        x_remainder = x[:-len(y)]
        # Count the differences
        counter = x_remainder.count("1")
        for i in range(0, len(y)):
            if y[i] != x_compare[i]:
                counter += 1

        return counter

sol=Solution()
print(sol.hamming_distance(1, 4))
print(sol.hamming_distance(2, 3))
