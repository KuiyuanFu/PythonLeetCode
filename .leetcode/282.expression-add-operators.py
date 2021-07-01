# @lc app=leetcode id=282 lang=python3
#
# [282] Expression Add Operators
#
# https://leetcode.com/problems/expression-add-operators/description/
#
# algorithms
# Hard (37.15%)
# Likes:    1741
# Dislikes: 289
# Total Accepted:    136.2K
# Total Submissions: 365.5K
# Testcase Example:  '"123"\n6'
#
# Given a string num that contains only digits and an integer target, return
# all possibilities to add the binary operators '+', '-', or '*' between the
# digits of num so that the resultant expression evaluates to the target
# value.
#
#
# Example 1:
# Input: num = "123", target = 6
# Output: ["1*2*3","1+2+3"]
# Example 2:
# Input: num = "232", target = 8
# Output: ["2*3+2","2+3*2"]
# Example 3:
# Input: num = "105", target = 5
# Output: ["1*0+5","10-5"]
# Example 4:
# Input: num = "00", target = 0
# Output: ["0*0","0+0","0-0"]
# Example 5:
# Input: num = "3456237490", target = 9191
# Output: []
#
#
# Constraints:
#
#
# 1 <= num.length <= 10
# num consists of only digits.
# -2^31 <= target <= 2^31 - 1
#
#
#

# @lc tags=divide-and-conquer

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 给定数字序列，和一个目标，将运算符插入到数字中，求计算结果为目标的所有组合。
# 直接动态规划。实际上就是将所有可能的划分方式都计算一遍。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        prop = {
            '+': 1,
            '-': 1,
            '*': 2,
        }
        opers = ['+', '-', '*']
        from collections import defaultdict
        ret = []
        numsString = num
        nums = [int(n) for n in num]
        length = len(nums)

        def cal(values: list, operators: list, operator: str):
            while len(operators) != 0:
                if prop[operator] > prop[operators[-1]]:
                    break
                o = operators.pop()
                vr = values.pop()
                vl = values.pop()
                if o == '+':
                    values.append(vl + vr)
                elif o == '-':
                    values.append(vl - vr)
                elif o == '*':
                    values.append(vl * vr)
            operators.append(operator)
            values.append(0)

        def rAddOperators(s: str, values: list, operators: list, index: int):
            if index == length:
                cal(values, operators, '+')
                if values[0] == target:
                    ret.append(s)
                return

            n = nums[index]
            c = numsString[index]

            for operator in opers:
                vc = values.copy()
                oc = operators.copy()
                cal(vc, oc, operator)
                vc[-1] = vc[-1] * 10 + n
                rAddOperators(s + operator + c, vc, oc, index + 1)
            # joint
            if nums[index - 1] != 0 or values[-1] != 0:
                vc = values.copy()
                oc = operators.copy()
                vc[-1] = vc[-1] * 10 + n
                rAddOperators(s + c, vc, oc, index + 1)

        rAddOperators(numsString[0], [0, nums[0]], ['+'], 1)
        return ret


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('num = "123", target = 6')
    print('Exception :')
    print('["1*2*3","1+2+3"]')
    print('Output :')
    print(str(Solution().addOperators("123", 6)))
    print()

    print('Example 2:')
    print('Input : ')
    print('num = "232", target = 8')
    print('Exception :')
    print('["2*3+2","2+3*2"]')
    print('Output :')
    print(str(Solution().addOperators("232", 8)))
    print()

    print('Example 3:')
    print('Input : ')
    print('num = "105", target = 5')
    print('Exception :')
    print('["1*0+5","10-5"]')
    print('Output :')
    print(str(Solution().addOperators("105", 5)))
    print()

    print('Example 4:')
    print('Input : ')
    print('num = "00", target = 0')
    print('Exception :')
    print('["0*0","0+0","0-0"]')
    print('Output :')
    print(str(Solution().addOperators("00", 0)))
    print()

    print('Example 5:')
    print('Input : ')
    print('num = "3456237490", target = 9191')
    print('Exception :')
    print('[]')
    print('Output :')
    print(str(Solution().addOperators("3456237490", 9191)))
    print()

    pass
# @lc main=end