# @lc app=leetcode id=932 lang=python3
#
# [932] Beautiful Array
#
# https://leetcode.com/problems/beautiful-array/description/
#
# algorithms
# Medium (64.83%)
# Likes:    832
# Dislikes: 1236
# Total Accepted:    36.5K
# Total Submissions: 56.2K
# Testcase Example:  '4'
#
# An array nums of length n is beautiful if:
#
#
# nums is a permutation of the integers in the range [1, n].
# For every 0 <= i < j < n, there is no index k with i < k < j where 2 *
# nums[k] == nums[i] + nums[j].
#
#
# Given the integer n, return any beautiful array nums of length n. There will
# be at least one valid answer for the given n.
#
#
# Example 1:
# Input: n = 4
# Output: [2,1,4,3]
# Example 2:
# Input: n = 5
# Output: [3,1,2,5,4]
#
#
# Constraints:
#
#
# 1 <= n <= 1000
#
#
#

# @lc tags=array

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 生成美丽的数组，即n长的数组，其中元素是1-n的一个排列；其中任意一个元素，在其前后分别任意找一个元素，找不到两个元素，使和为其的二倍。
# 由于是一个数的二倍，所以两个奇偶相同的元素才有中位数，即可以分成奇偶两组，这样这两组之间就不会产生中间数。以只有一个元素1的数组开始迭代，奇数在前，偶数在后，每一次翻倍。奇数部分为原数组元素依次翻倍减一后结果，偶数部分原数组元素依次翻倍结果。由于原来满足要求，且奇偶两部分不影响，在部分内，相对关系也不变，所以满足要求。
#
#
# @lc idea=end

# @lc group=array

# @lc rank=10


# @lc code=start
class Solution:

    def beautifulArray(self, n: int) -> List[int]:
        res = [1]
        while len(res) < n:
            new = []
            for num in res:
                r = num * 2 - 1
                if r <= n:
                    new.append(r)

            for num in res:
                r = num * 2
                if r <= n:
                    new.append(r)

            res = new

        return res

        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('n = 4')
    print('Exception :')
    print('[2,1,4,3]')
    print('Output :')
    print(str(Solution().beautifulArray(4)))
    print()

    print('Example 2:')
    print('Input : ')
    print('n = 5')
    print('Exception :')
    print('[3,1,2,5,4]')
    print('Output :')
    print(str(Solution().beautifulArray(5)))
    print()

    pass
# @lc main=end