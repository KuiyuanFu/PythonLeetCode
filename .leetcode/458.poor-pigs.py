# @lc app=leetcode id=458 lang=python3
#
# [458] Poor Pigs
#
# https://leetcode.com/problems/poor-pigs/description/
#
# algorithms
# Hard (54.93%)
# Likes:    578
# Dislikes: 1081
# Total Accepted:    31.9K
# Total Submissions: 58K
# Testcase Example:  '1000\n15\n60'
#
# There are buckets buckets of liquid, where exactly one of the buckets is
# poisonous. To figure out which one is poisonous, you feed some number of
# (poor) pigs the liquid to see whether they will die or not. Unfortunately,
# you only have minutesToTest minutes to determine which bucket is poisonous.
#
# You can feed the pigs according to these steps:
#
#
# Choose some live pigs to feed.
# For each pig, choose which buckets to feed it. The pig will consume all the
# chosen buckets simultaneously and will take no time.
# Wait for minutesToDie minutes. You may not feed any other pigs during this
# time.
# After minutesToDie minutes have passed, any pigs that have been fed the
# poisonous bucket will die, and all others will survive.
# Repeat this process until you run out of time.
#
#
# Given buckets, minutesToDie, and minutesToTest, return the minimum number of
# pigs needed to figure out which bucket is poisonous within the allotted
# time.
#
#
# Example 1:
# Input: buckets = 1000, minutesToDie = 15, minutesToTest = 60
# Output: 5
# Example 2:
# Input: buckets = 4, minutesToDie = 15, minutesToTest = 15
# Output: 2
# Example 3:
# Input: buckets = 4, minutesToDie = 15, minutesToTest = 30
# Output: 2
#
#
# Constraints:
#
#
# 1 <= buckets <= 1000
# 1 <= minutesToDie <= minutesToTest <= 100
#
#
#

# @lc tags=math

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 试出那个桶有毒，每次需要等待时间，问在给定桶数与次数时，最少需要多少猪。
# 每只猪找一个维度，可以试t次，一共n个猪，那么就可以试出来t^n个桶。
#
# @lc idea=end

# @lc group=dynamic-programming

# @lc rank=10


# @lc code=start
class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int,
                 minutesToTest: int) -> int:

        base = minutesToTest // minutesToDie + 1
        counts = 0
        while buckets > 1:
            buckets = (buckets - 1) // base + 1
            counts += 1
        return counts


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('buckets = 1000, minutesToDie = 15, minutesToTest = 60')
    print('Exception :')
    print('5')
    print('Output :')
    print(str(Solution().poorPigs(1000, 15, 60)))
    print()

    print('Example 2:')
    print('Input : ')
    print('buckets = 4, minutesToDie = 15, minutesToTest = 15')
    print('Exception :')
    print('2')
    print('Output :')
    print(str(Solution().poorPigs(4, 15, 15)))
    print()

    print('Example 3:')
    print('Input : ')
    print('buckets = 4, minutesToDie = 15, minutesToTest = 30')
    print('Exception :')
    print('2')
    print('Output :')
    print(str(Solution().poorPigs(4, 15, 30)))
    print()

    pass
# @lc main=end