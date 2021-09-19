# @lc app=leetcode id=496 lang=python3
#
# [496] Next Greater Element I
#
# https://leetcode.com/problems/next-greater-element-i/description/
#
# algorithms
# Easy (67.16%)
# Likes:    623
# Dislikes: 42
# Total Accepted:    250.2K
# Total Submissions: 371.8K
# Testcase Example:  '[4,1,2]\n[1,3,4,2]'
#
# The next greater element of some element x in an array is the first greater
# element that is to the right of x in the same array.
#
# You are given two distinct 0-indexed integer arrays nums1 and nums2, where
# nums1 is a subset of nums2.
#
# For each 0 <= i < nums1.length, find the index j such that nums1[i] ==
# nums2[j] and determine the next greater element of nums2[j] in nums2. If
# there is no next greater element, then the answer for this query is -1.
#
# Return an array ans of length nums1.length such that ans[i] is the next
# greater element as described above.
#
#
# Example 1:
#
#
# Input: nums1 = [4,1,2], nums2 = [1,3,4,2]
# Output: [-1,3,-1]
# Explanation: The next greater element for each value of nums1 is as follows:
# - 4 is underlined in nums2 = [1,3,4,2]. There is no next greater element, so
# the answer is -1.
# - 1 is underlined in nums2 = [1,3,4,2]. The next greater element is 3.
# - 2 is underlined in nums2 = [1,3,4,2]. There is no next greater element, so
# the answer is -1.
#
#
# Example 2:
#
#
# Input: nums1 = [2,4], nums2 = [1,2,3,4]
# Output: [3,-1]
# Explanation: The next greater element for each value of nums1 is as follows:
# - 2 is underlined in nums2 = [1,2,3,4]. The next greater element is 3.
# - 4 is underlined in nums2 = [1,2,3,4]. There is no next greater element, so
# the answer is -1.
#
#
#
# Constraints:
#
#
# 1 <= nums1.length <= nums2.length <= 1000
# 0 <= nums1[i], nums2[i] <= 10^4
# All integers in nums1 and nums2 are unique.
# All the integers of nums1 also appear in nums2.
#
#
#
# Follow up: Could you find an O(nums1.length + nums2.length) solution?
#

# @lc tags=stack

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 在数组找第一个大于其的数字。
# 在第二个数组中，使用栈，倒序遍历，找大于其的第一个数字，小于其的可以丢弃。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def nextGreaterElement(self, nums1: List[int],
                           nums2: List[int]) -> List[int]:

        biggers = []
        d = {}
        for i in reversed(range(len(nums2))):
            n = nums2[i]
            while biggers:
                if biggers[-1] <= n:
                    biggers.pop()
                else:
                    break
            d[n] = biggers[-1] if biggers else -1
            biggers.append(n)

        for i, n in enumerate(nums1):
            nums1[i] = d[n]
        return nums1
        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('nums1 = [4,1,2], nums2 = [1,3,4,2]')
    print('Exception :')
    print('[-1,3,-1]')
    print('Output :')
    print(str(Solution().nextGreaterElement([4, 1, 2], [1, 3, 4, 2])))
    print()

    print('Example 2:')
    print('Input : ')
    print('nums1 = [2,4], nums2 = [1,2,3,4]')
    print('Exception :')
    print('[3,-1]')
    print('Output :')
    print(str(Solution().nextGreaterElement([2, 4], [1, 2, 3, 4])))
    print()

    pass
# @lc main=end