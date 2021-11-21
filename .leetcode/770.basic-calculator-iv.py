# @lc app=leetcode id=770 lang=python3
#
# [770] Basic Calculator IV
#
# https://leetcode.com/problems/basic-calculator-iv/description/
#
# algorithms
# Hard (54.87%)
# Likes:    104
# Dislikes: 1080
# Total Accepted:    7.6K
# Total Submissions: 13.8K
# Testcase Example:  '"e + 8 - a + 5"\n["e"]\n[1]'
#
# Given an expression such as expression = "e + 8 - a + 5" and an evaluation
# map such as {"e": 1} (given in terms of evalvars = ["e"] and evalints = [1]),
# return a list of tokens representing the simplified expression, such as
# ["-1*a","14"]
#
#
# An expression alternates chunks and symbols, with a space separating each
# chunk and symbol.
# A chunk is either an expression in parentheses, a variable, or a non-negative
# integer.
# A variable is a string of lowercase letters (not including digits.) Note that
# variables can be multiple letters, and note that variables never have a
# leading coefficient or unary operator like "2x" or "-x".
#
#
# Expressions are evaluated in the usual order: brackets first, then
# multiplication, then addition and subtraction.
#
#
# For example, expression = "1 + 2 * 3" has an answer of ["7"].
#
#
# The format of the output is as follows:
#
#
# For each term of free variables with a non-zero coefficient, we write the
# free variables within a term in sorted order lexicographically.
#
# For example, we would never write a term like "b*a*c", only
# "a*b*c".
#
#
# Terms have degrees equal to the number of free variables being multiplied,
# counting multiplicity. We write the largest degree terms of our answer first,
# breaking ties by lexicographic order ignoring the leading coefficient of the
# term.
#
# For example, "a*a*b*c" has degree 4.
#
#
# The leading coefficient of the term is placed directly to the left with an
# asterisk separating it from the variables (if they exist.) A leading
# coefficient of 1 is still printed.
# An example of a well-formatted answer is ["-2*a*a*a", "3*a*a*b", "3*b*b",
# "4*a", "5*c", "-6"].
# Terms (including constant terms) with coefficient 0 are not
# included.
#
# For example, an expression of "0" has an output of [].
#
#
#
#
#
# Example 1:
#
#
# Input: expression = "e + 8 - a + 5", evalvars = ["e"], evalints = [1]
# Output: ["-1*a","14"]
#
#
# Example 2:
#
#
# Input: expression = "e - 8 + temperature - pressure", evalvars = ["e",
# "temperature"], evalints = [1, 12]
# Output: ["-1*pressure","5"]
#
#
# Example 3:
#
#
# Input: expression = "(e + 8) * (e - 8)", evalvars = [], evalints = []
# Output: ["1*e*e","-64"]
#
#
# Example 4:
#
#
# Input: expression = "a * b * c + b * a * c * 4", evalvars = [], evalints = []
# Output: ["5*a*b*c"]
#
#
# Example 5:
#
#
# Input: expression = "((a - b) * (b - c) + (c - a)) * ((a - b) + (b - c) * (c
# - a))", evalvars = [], evalints = []
# Output:
# ["-1*a*a*b*b","2*a*a*b*c","-1*a*a*c*c","1*a*b*b*b","-1*a*b*b*c","-1*a*b*c*c","1*a*c*c*c","-1*b*b*b*c","2*b*b*c*c","-1*b*c*c*c","2*a*a*b","-2*a*a*c","-2*a*b*b","2*a*c*c","1*b*b*b","-1*b*b*c","1*b*c*c","-1*c*c*c","-1*a*a","1*a*b","1*a*c","-1*b*c"]
#
#
#
# Constraints:
#
#
# 1 <= expression.length <= 250
# expression consists of lowercase English letters, digits, '+', '-', '*', '(',
# ')', ' '.
# expression does not contain any leading or trailing spaces.
# All the tokens in expression are separated by a single space.
# 0 <= evalvars.length <= 100
# 1 <= evalvars[i].length <= 20
# evalvars[i] consists of lowercase English letters.
# evalints.length == evalvars.length
# -100 <= evalints[i] <= 100
#
#
#

# @lc tags=greedy;union-find;graph

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 展开表达式。
# 栈。递归。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def basicCalculatorIV(self, expression: str, evalvars: List[str],
                          evalints: List[int]) -> List[str]:
        length = len(expression)

        evals = {}
        for i in range(len(evalvars)):
            evals[evalvars[i]] = evalints[i]

        def genTokens():
            res = []

            idx = -1
            while idx + 1 < length:
                idx += 1
                c = expression[idx]
                if c == ' ':
                    continue
                elif c in '-+*()':
                    res.append(c)
                else:
                    r = idx
                    while r + 1 < length and expression[r + 1] not in '-+*() ':
                        r += 1
                    res.append(expression[idx:r + 1])
                    idx = r
            return res

        tokens = genTokens()
        length = len(tokens)

        # print(tokens)

        def oper(operator, n1, n2):
            if operator == '+':
                for k in n2:
                    n1[k] += n2[k]
                return n1
            elif operator == '-':
                for k in n2:
                    n1[k] -= n2[k]
                return n1
            else:
                n = defaultdict(int)
                for k1 in n1:
                    for k2 in n2:
                        k = tuple(sorted(k1 + k2))
                        n[k] += n1[k1] * n2[k2]
                return n
            pass

        def recur(idx):
            numberStack = []
            operatorStack = []

            while idx < length:
                token = tokens[idx]

                if token == ')':
                    break
                elif token in '-+*':
                    operatorStack.append(token)
                else:
                    if token == '(':
                        number, idx = recur(idx + 1)
                        numberStack.append(number)
                    elif token.isalpha():
                        number = defaultdict(int)
                        if token in evals:
                            number[tuple([])] = evals[token]
                        else:
                            number[tuple([token])] = 1
                        numberStack.append(number)
                    elif token.isdigit():
                        number = defaultdict(int)
                        number[tuple([])] = int(token)
                        numberStack.append(number)

                    if len(operatorStack) > 0 and operatorStack[-1] in '*':
                        operator = operatorStack.pop()
                        n2 = numberStack.pop()
                        n1 = numberStack.pop()
                        numberStack.append(oper(operator, n1, n2))
                    if len(operatorStack) == 2:
                        operator = operatorStack.pop(0)
                        n1 = numberStack.pop(0)
                        n2 = numberStack.pop(0)
                        numberStack.insert(0, oper(operator, n1, n2))

                idx += 1
            if len(operatorStack) == 1:
                operator = operatorStack.pop(0)
                n1 = numberStack.pop(0)
                n2 = numberStack.pop(0)
                numberStack.insert(0, oper(operator, n1, n2))
            return numberStack[0], idx
            pass

        res = recur(0)[0]

        def format(dict):
            priority = []
            for k in dict:
                v = dict[k]
                if v != 0:
                    p = tuple([-len(k)]) + k
                    r = '*'.join(tuple([str(v)]) + k)
                    priority.append((p, r))
            priority.sort()
            res = []
            for p, r in priority:
                res.append(r)
            return res

        return format(res)
        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('expression = "e + 8 - a + 5", evalvars = ["e"], evalints = [1]')
    print('Exception :')
    print('["-1*a","14"]')
    print('Output :')
    print(str(Solution().basicCalculatorIV("e + 8 - a + 5", ["e"], [1])))
    print()

    print('Example 2:')
    print('Input : ')
    print(
        'expression = "e - 8 + temperature - pressure", evalvars = ["e","temperature"], evalints = [1, 12]'
    )
    print('Exception :')
    print('["-1*pressure","5"]')
    print('Output :')
    print(
        str(Solution().basicCalculatorIV("e - 8 + temperature - pressure",
                                         ["e", "temperature"], [1, 12])))
    print()

    print('Example 3:')
    print('Input : ')
    print('expression = "(e + 8) * (e - 8)", evalvars = [], evalints = []')
    print('Exception :')
    print('["1*e*e","-64"]')
    print('Output :')
    print(str(Solution().basicCalculatorIV("(e + 8) * (e - 8)", [], [])))
    print()

    print('Example 4:')
    print('Input : ')
    print(
        'expression = "a * b * c + b * a * c * 4", evalvars = [], evalints = []'
    )
    print('Exception :')
    print('["5*a*b*c"]')
    print('Output :')
    print(
        str(Solution().basicCalculatorIV("a * b * c + b * a * c * 4", [], [])))
    print()

    print('Example 5:')
    print('Input : ')
    print(
        'expression = "((a - b) * (b - c) + (c - a)) * ((a - b) + (b - c) * (c- a))", evalvars = [], evalints = []'
    )
    print('Exception :')
    print(
        '["-1*a*a*b*b","2*a*a*b*c","-1*a*a*c*c","1*a*b*b*b","-1*a*b*b*c","-1*a*b*c*c","1*a*c*c*c","-1*b*b*b*c","2*b*b*c*c","-1*b*c*c*c","2*a*a*b","-2*a*a*c","-2*a*b*b","2*a*c*c","1*b*b*b","-1*b*b*c","1*b*c*c","-1*c*c*c","-1*a*a","1*a*b","1*a*c","-1*b*c"]'
    )
    print('Output :')
    print(
        str(Solution().basicCalculatorIV(
            "((a - b) * (b - c) + (c - a)) * ((a - b) + (b - c) * (c- a))", [],
            [])))
    print()

    pass
# @lc main=end