import string


class Solution():
    """
    Input: two strings
    Output: True if they are permutations of each other; Else False

    Assumptions:
    * Blank spaces are ignored
    * Capitalization is ignored
    * Duplicate letters are NOT ignored
    * Punctuation is ignored

    Examples:
        Input: ["tacos", "catos"]
        >>> True

        Input: ["", ""]
        >>> True

        Input: ["t", "t"]
        >>> True

        Input: ["t    z", "tz "]
        >>> True

        Input: ["TZ", "tz"]
        >>> True

        Input: ["t.", "t"]
        >>> True

        Input: ["tt", "t"]
        >>> False

        Input: ["tz", "t"]
        >>> False
    """

    def clean(self, s):
        table = str.maketrans("", "", string.punctuation)
        output = s.translate(table)                             # remove punctuation
        output = "".join(output.lower().split())                # remove spaces
        return "".join(sorted(output))                          # sort characters

    def permutation(self, s1, s2):
        cs1 = self.clean(s1)
        cs2 = self.clean(s2)
        if len(cs1) != len(cs2):
            return False
        for i in range(0, len(cs1)):
            if cs1[i] != cs2[i]:
                return False

        return True

sol = Solution()
print(sol.permutation("tacos", "catos"))
print(sol.permutation("", ""))
print(sol.permutation("t", "t"))
print(sol.permutation("t    z", "tz "))
print(sol.permutation("TZ", "tz"))
print(sol.permutation("t.", "t"))
print(sol.permutation("tt", "t"))
print(sol.permutation("tz", "t"))
