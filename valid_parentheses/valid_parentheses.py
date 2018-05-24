class Solution():
    """
    input: a string containing only parentheses (i.e. (, [, {, }, ], ))
    output: true if:
        * each open parentheses has a closing parentheses
        * parentheses are closed in the same order they were opened

    example:
        parens = '()[]{}'
        ==> True

        parens = '([)]'
        ==> False

        parens = '(]'
        ==> False
    """

    def valid_parentheses(self, parens):
        if parens == '':
            return True
        open_sequence = []
        open = ['(', '[', '{']
        close = [')', ']', '}']
        for c in parens:
            if c in open:
                open_sequence.append(c)
            elif c in close:
                if open_sequence == []:
                    return False
                opener = open_sequence.pop()
                open_index = open.index(opener)
                close_index = close.index(c)
                if open_index != close_index:
                    return False

        if not open_sequence:
            return True
        else:
            return False

# Testing:
sol = Solution()
print(sol.valid_parentheses('()[]{}'))
print(sol.valid_parentheses('([)]'))
print(sol.valid_parentheses('(]'))
print(sol.valid_parentheses(']'))
print(sol.valid_parentheses('['))
