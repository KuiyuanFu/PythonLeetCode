# @lc app=leetcode id=970 lang=python3
#
# [970] Powerful Integers
#
# https://leetcode.com/problems/powerful-integers/description/
#
# algorithms
# Medium (43.61%)
# Likes:    277
# Dislikes: 66
# Total Accepted:    47.8K
# Total Submissions: 109.7K
# Testcase Example:  '2\n3\n10'
#
# Given three integers x, y, and bound, return a list of all the powerful
# integers that have a value less than or equal to bound.
#
# An integer is powerful if it can be represented as x^i + y^j for some
# integers i >= 0 and j >= 0.
#
# You may return the answer in any order. In your answer, each value should
# occur at most once.
#
#
# Example 1:
#
#
# Input: x = 2, y = 3, bound = 10
# Output: [2,3,4,5,7,9,10]
# Explanation:
# 2 = 2^0 + 3^0
# 3 = 2^1 + 3^0
# 4 = 2^0 + 3^1
# 5 = 2^1 + 3^1
# 7 = 2^2 + 3^1
# 9 = 2^3 + 3^0
# 10 = 2^0 + 3^2
#
#
# Example 2:
#
#
# Input: x = 3, y = 5, bound = 15
# Output: [2,4,6,8,10,14]
#
#
#
# Constraints:
#
#
# 1 <= x, y <= 100
# 0 <= bound <= 10^6
#
#
#

# @lc tags=Unknown

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 给定x，y及一个区域bound，使x与y的任意次幂的和小于等于bound的数。
# 直接求幂次列表，之后乘积。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:

    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        if bound <= 1:
            return []
        res = set()

        def getList(x):
            if x == 1:
                return [1]
            else:
                return [x**i for i in range(0, int(log(bound, x)) + 1)]

        xs = getList(x)
        ys = getList(y)
        for x, y in product(xs, ys):
            s = x + y
            if s <= bound:
                res.add(s)
        return list(res)
        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('x = 2, y = 3, bound = 10')
    print('Exception :')
    print('[2,3,4,5,7,9,10]')
    print('Output :')
    print(str(Solution().powerfulIntegers(2, 3, 10)))
    print()

    print('Example 2:')
    print('Input : ')
    print('x = 3, y = 5, bound = 15')
    print('Exception :')
    print('[2,4,6,8,10,14]')
    print('Output :')
    print(str(Solution().powerfulIntegers(3, 5, 15)))
    print()

    print('Example 2:')
    print('Input : ')
    print('x = 2 y = 1, bound = 10')
    print('Exception :')
    print('[9,2,3,5]')
    print('Output :')
    print(str(Solution().powerfulIntegers(2, 1, 10)))
    print()
    print('Example 2:')
    print('Input : ')
    print('x = 2 y = 3, bound = 0')
    print('Exception :')
    print('[]')
    print('Output :')
    print(str(Solution().powerfulIntegers(2, 3, 0)))
    print()

    pass
# @lc main=end