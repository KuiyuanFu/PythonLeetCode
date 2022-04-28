# @lc app=leetcode id=904 lang=python3
#
# [904] Fruit Into Baskets
#
# https://leetcode.com/problems/fruit-into-baskets/description/
#
# algorithms
# Medium (42.83%)
# Likes:    967
# Dislikes: 76
# Total Accepted:    200K
# Total Submissions: 467.6K
# Testcase Example:  '[1,2,1]'
#
# You are visiting a farm that has a single row of fruit trees arranged from
# left to right. The trees are represented by an integer array fruits where
# fruits[i] is the type of fruit the i^th tree produces.
#
# You want to collect as much fruit as possible. However, the owner has some
# strict rules that you must follow:
#
#
# You only have two baskets, and each basket can only hold a single type of
# fruit. There is no limit on the amount of fruit each basket can hold.
# Starting from any tree of your choice, you must pick exactly one fruit from
# every tree (including the start tree) while moving to the right. The picked
# fruits must fit in one of your baskets.
# Once you reach a tree with fruit that cannot fit in your baskets, you must
# stop.
#
#
# Given the integer array fruits, return the maximum number of fruits you can
# pick.
#
#
# Example 1:
#
#
# Input: fruits = [1,2,1]
# Output: 3
# Explanation: We can pick from all 3 trees.
#
#
# Example 2:
#
#
# Input: fruits = [0,1,2,2]
# Output: 3
# Explanation: We can pick from trees [1,2,2].
# If we had started at the first tree, we would only pick from trees [0,1].
#
#
# Example 3:
#
#
# Input: fruits = [1,2,3,2,2]
# Output: 4
# Explanation: We can pick from trees [2,3,2,2].
# If we had started at the first tree, we would only pick from trees [1,2].
#
#
#
# Constraints:
#
#
# 1 <= fruits.length <= 10^5
# 0 <= fruits[i] < fruits.length
#
#
#

# @lc tags=tree;depth-first-search

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 只含有两种类型的最长连续子序列的长度。
# 记录种类。迭代。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:

    def totalFruit(self, fruits: List[int]) -> int:
        res = 0
        p1, p2 = None, None
        c1, c2 = 0, 0
        # continuous count
        c = 0
        for f in fruits:

            if f == p2:
                pass
            elif f == p1:
                p1, p2 = p2, p1
                c1, c2 = c2, c1
                c = 0
            else:
                p1, p2 = p2, f
                c1, c2 = c, 0
                c = 0

            c2 += 1
            c += 1
            res = max(res, c1 + c2)

        return res
        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('fruits = [1,2,1]')
    print('Exception :')
    print('3')
    print('Output :')
    print(str(Solution().totalFruit([1, 2, 1])))
    print()

    print('Example 2:')
    print('Input : ')
    print('fruits = [0,1,2,2]')
    print('Exception :')
    print('3')
    print('Output :')
    print(str(Solution().totalFruit([0, 1, 2, 2])))
    print()

    print('Example 3:')
    print('Input : ')
    print('fruits = [1,2,3,2,2]')
    print('Exception :')
    print('4')
    print('Output :')
    print(str(Solution().totalFruit([1, 2, 3, 2, 2])))
    print()

    pass
# @lc main=end