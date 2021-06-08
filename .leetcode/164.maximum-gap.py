# @lc app=leetcode id=164 lang=python3
#
# [164] Maximum Gap
#
# https://leetcode.com/problems/maximum-gap/description/
#
# algorithms
# Hard (37.47%)
# Likes:    1448
# Dislikes: 243
# Total Accepted:    117.7K
# Total Submissions: 297.6K
# Testcase Example:  '[3,6,9,1]'
#
# Given an integer array nums, return the maximum difference between two
# successive elements in its sorted form. If the array contains less than two
# elements, return 0.
#
# You must write an algorithm that runs in linear time and uses linear extra
# space.
#
#
# Example 1:
#
#
# Input: nums = [3,6,9,1]
# Output: 3
# Explanation: The sorted form of the array is [1,3,6,9], either (3,6) or (6,9)
# has the maximum difference 3.
#
#
# Example 2:
#
#
# Input: nums = [10]
# Output: 0
# Explanation: The array contains less than 2 elements, therefore return 0.
#
#
#
# Constraints:
#
#
# 1 <= nums.length <= 10^4
# 0 <= nums[i] <= 10^9
#
#
#

# @lc tags=sort

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 给定一个数组，求排序后两个相邻元素的最大间隔。O n，O n。
# 不考虑复杂度，就可以直接排序，O nlgn。
# 先计算最大值maximum和最小值minimum，那么最大间隔maxgap一定不小于 (maximum-minimum)/(n-1)，因为总长度是一定的，若一个间隔小于平均值，那么必然有另一个大于平均值，所以至少为平均值，那么就可以设置(n-1)个bucket，每个bucket存放在此区间的最小值最大值，记为左值右值。
# 忽略没有值的bucket，之后计算较大bucket的左值，减较小bucket的右值，就是间隔gap。
#
#
# @lc idea=end

# @lc group=sort;bucket

# @lc rank=10


# @lc code=start
class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return 0

        maximum = max(nums)
        minimum = min(nums)
        gap = (maximum - minimum) // (len(nums) - 1) + 1
        # bucket l r
        buckets = [[-1, -1] for _ in range(len(nums))]
        for n in nums:
            # set bucket
            index = (n - minimum) // gap
            if buckets[index][0] == -1 or n < buckets[index][0]:
                buckets[index][0] = n
            if buckets[index][1] == -1 or n > buckets[index][1]:
                buckets[index][1] = n

        # bigger bucket's left value reduce smaller bucket's right
        maxGap = 0
        l, r = buckets[0][0], buckets[0][1]
        for bucket in buckets:
            r = max(r, bucket[0])
            maxGap = max(maxGap, r - l)
            l = max(l, bucket[1])
        return maxGap


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print(str(Solution().maximumGap([1, 10000000])))

    print('Example 1:')
    print('Input : ')
    print('nums = [3,6,9,1]')
    print('Exception :')
    print('3')
    print('Output :')
    print(str(Solution().maximumGap([3, 6, 9, 1])))
    print()

    print('Example 2:')
    print('Input : ')
    print('nums = [10]')
    print('Exception :')
    print('0')
    print('Output :')
    print(str(Solution().maximumGap([10])))
    print()

    pass
# @lc main=end