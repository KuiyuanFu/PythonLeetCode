# @lc app=leetcode id=135 lang=python3
#
# [135] Candy
#
# https://leetcode.com/problems/candy/description/
#
# algorithms
# Hard (33.72%)
# Likes:    1537
# Dislikes: 202
# Total Accepted:    159.3K
# Total Submissions: 472.5K
# Testcase Example:  '[1,0,2]'
#
# There are n children standing in a line. Each child is assigned a rating
# value given in the integer array ratings.
#
# You are giving candies to these children subjected to the following
# requirements:
#
#
# Each child must have at least one candy.
# Children with a higher rating get more candies than their neighbors.
#
#
# Return the minimum number of candies you need to have to distribute the
# candies to the children.
#
#
# Example 1:
#
#
# Input: ratings = [1,0,2]
# Output: 5
# Explanation: You can allocate to the first, second and third child with 2, 1,
# 2 candies respectively.
#
#
# Example 2:
#
#
# Input: ratings = [1,2,2]
# Output: 4
# Explanation: You can allocate to the first, second and third child with 1, 2,
# 1 candies respectively.
# The third child gets 1 candy because it satisfies the above two
# conditions.
#
#
#
# Constraints:
#
#
# n == ratings.length
# 1 <= n <= 2 * 10^4
# 0 <= ratings[i] <= 2 * 10^4
#
#
#

# @lc tags=greedy

# @lc imports=start
from calendar import c
from textwrap import indent
from urllib3 import Retry
from imports import *

# @lc imports=end

# @lc idea=start
#
# 分糖果，每个孩子有一个等级，高等级要比相邻低等级分得的糖果多。求最少需要多少糖果。
# 主要是根据情况判断，如果此元素大于前驱元素，那么其糖果数较前驱元素大于1即可；若等于，则直接为1即可；比较复杂的是小于前驱元素，那么，此元素为1，但是前驱元素可能大于1，也可能为1。若为1，则需要将前驱元素增加糖果。
# 比较简单的方法是直接查找有多少个连续下降的即可。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def candy(self, ratings: List[int]) -> int:
        if len(ratings) <= 1:
            return len(ratings)
        index = 1
        candy = 1
        candySum = 1
        while index < len(ratings):
            if ratings[index] > ratings[index - 1]:
                candy += 1
                candySum += candy
                index += 1
            elif ratings[index] == ratings[index - 1]:
                candy = 1
                candySum += candy
                index += 1
            else:
                indexNext = index + 1
                while indexNext <len(ratings) \
                    and ratings[indexNext-1]> ratings[indexNext]:
                    indexNext += 1
                length = indexNext - index
                candySum += (length + 1) * length // 2
                candySum += max(length + 1 - candy, 0)
                candy = 1
                index = indexNext

        return candySum
        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print(str(Solution().candy([1, 3, 2, 2, 1])))
    print('Example 1:')
    print('Input : ')
    print('ratings = [1,0,2]')
    print('Exception :')
    print('5')
    print('Output :')
    print(str(Solution().candy([1, 0, 2])))
    print()

    print('Example 2:')
    print('Input : ')
    print('ratings = [1,2,2]')
    print('Exception :')
    print('4')
    print('Output :')
    print(str(Solution().candy([1, 2, 2])))
    print()

    pass
# @lc main=end