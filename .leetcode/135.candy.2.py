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

from imports import *

# @lc imports=end

# @lc idea=start
#
# 分糖果，每个孩子有一个等级，高等级要比相邻低等级分得的糖果多。求最少需要多少糖果。
# 另一种思想，两次遍历，一次满足升序，一次满足降序。
#
# @lc idea=end

# @lc group=greedy

# @lc rank=10


# @lc code=start
class Solution:
    def candy(self, ratings: List[int]) -> int:
        if len(ratings) <= 1:
            return len(ratings)

        candies = [1] * len(ratings)
        for i in range(len(ratings) - 1):
            if ratings[i + 1] > ratings[i]:
                candies[i + 1] = candies[i] + 1
        for i in reversed(range(len(ratings) - 1)):
            if ratings[i] > ratings[i + 1]:
                candies[i] = max(candies[i], candies[i + 1] + 1)
        return sum(candies)


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