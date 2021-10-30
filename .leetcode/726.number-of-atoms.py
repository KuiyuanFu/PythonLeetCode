# @lc app=leetcode id=726 lang=python3
#
# [726] Number of Atoms
#
# https://leetcode.com/problems/number-of-atoms/description/
#
# algorithms
# Hard (51.23%)
# Likes:    794
# Dislikes: 197
# Total Accepted:    39.1K
# Total Submissions: 75.9K
# Testcase Example:  '"H2O"'
#
# Given a string formula representing a chemical formula, return the count of
# each atom.
#
# The atomic element always starts with an uppercase character, then zero or
# more lowercase letters, representing the name.
#
# One or more digits representing that element's count may follow if the count
# is greater than 1. If the count is 1, no digits will follow.
#
#
# For example, "H2O" and "H2O2" are possible, but "H1O2" is impossible.
#
#
# Two formulas are concatenated together to produce another formula.
#
#
# For example, "H2O2He3Mg4" is also a formula.
#
#
# A formula placed in parentheses, and a count (optionally added) is also a
# formula.
#
#
# For example, "(H2O2)" and "(H2O2)3" are formulas.
#
#
# Return the count of all elements as a string in the following form: the first
# name (in sorted order), followed by its count (if that count is more than 1),
# followed by the second name (in sorted order), followed by its count (if that
# count is more than 1), and so on.
#
#
# Example 1:
#
#
# Input: formula = "H2O"
# Output: "H2O"
# Explanation: The count of elements are {'H': 2, 'O': 1}.
#
#
# Example 2:
#
#
# Input: formula = "Mg(OH)2"
# Output: "H2MgO2"
# Explanation: The count of elements are {'H': 2, 'Mg': 1, 'O': 2}.
#
#
# Example 3:
#
#
# Input: formula = "K4(ON(SO3)2)2"
# Output: "K4N2O14S4"
# Explanation: The count of elements are {'K': 4, 'N': 2, 'O': 14, 'S': 4}.
#
#
# Example 4:
#
#
# Input: formula = "Be32"
# Output: "Be32"
#
#
#
# Constraints:
#
#
# 1 <= formula.length <= 1000
# formula consists of English letters, digits, '(', and ')'.
# formula is always valid.
# All the values in the output will fit in a 32-bit integer.
#
#
#

# @lc tags=hash-table;stack;recursion

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 格式化化学分子式。
# 栈。
#
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def countOfAtoms(self, formula: str) -> str:
        tokens = []
        t = ''
        formula += 'End'
        for c in formula:
            if c == '(' or c == ')':
                if len(t) > 0:
                    tokens.append(t)
                    t = ''
                tokens.append(c)
            elif c.islower():
                t += c
            elif c.isupper():
                if len(t) > 0:
                    tokens.append(t)
                t = c
            elif c.isdigit():
                if t.isdigit():
                    t += c
                else:
                    if len(t) > 0:
                        tokens.append(t)
                    t = c

        ds = []
        d = defaultdict(int)

        i = 0
        while i < len(tokens):
            t = tokens[i]
            if t == '(':
                ds.append(d)
                ds.append('(')
                d = defaultdict(int)
            elif t == ')':
                while ds:
                    dp = ds.pop()
                    if dp == '(':
                        break
                    else:
                        for k in dp.keys():
                            d[k] += dp[k]
                tn = tokens[i + 1] if i + 1 < len(tokens) else ""
                if tn.isdigit():
                    c = int(tn)
                    for k in d.keys():
                        d[k] *= c
                    i += 1
                while ds and ds[-1] != '(':
                    dp = ds.pop()
                    for k in dp.keys():
                        d[k] += dp[k]

            elif t.isalpha():
                tn = tokens[i + 1] if i + 1 < len(tokens) else ""
                if tn.isdigit():
                    d[t] += int(tn)
                    i += 1
                else:
                    d[t] += 1
            i += 1
        res = [(k, d[k]) for k in d.keys()]
        res.sort()
        res = ''.join(k + ("" if c == 1 else str(c)) for k, c in res)
        return res
        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('formula = "H2O"')
    print('Exception :')
    print('"H2O"')
    print('Output :')
    print(str(Solution().countOfAtoms("H2O")))
    print()

    print('Example 2:')
    print('Input : ')
    print('formula = "Mg(OH)2"')
    print('Exception :')
    print('"H2MgO2"')
    print('Output :')
    print(str(Solution().countOfAtoms("Mg(OH)2")))
    print()

    print('Example 3:')
    print('Input : ')
    print('formula = "K4(ON(SO3)2)2"')
    print('Exception :')
    print('"K4N2O14S4"')
    print('Output :')
    print(str(Solution().countOfAtoms("K4(ON(SO3)2)2")))
    print()

    print('Example 4:')
    print('Input : ')
    print('formula = "Be32"')
    print('Exception :')
    print('"Be32"')
    print('Output :')
    print(str(Solution().countOfAtoms("Be32")))
    print()

    pass
# @lc main=end