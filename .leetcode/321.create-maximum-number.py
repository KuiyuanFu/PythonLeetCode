# @lc app=leetcode id=321 lang=python3
#
# [321] Create Maximum Number
#
# https://leetcode.com/problems/create-maximum-number/description/
#
# algorithms
# Hard (27.71%)
# Likes:    1037
# Dislikes: 284
# Total Accepted:    45.2K
# Total Submissions: 163.2K
# Testcase Example:  '[3,4,6,5]\n[9,1,2,5,8,3]\n5'
#
# You are given two integer arrays nums1 and nums2 of lengths m and n
# respectively. nums1 and nums2 represent the digits of two numbers. You are
# also given an integer k.
#
# Create the maximum number of length k <= m + n from digits of the two
# numbers. The relative order of the digits from the same array must be
# preserved.
#
# Return an array of the k digits representing the answer.
#
#
# Example 1:
#
#
# Input: nums1 = [3,4,6,5], nums2 = [9,1,2,5,8,3], k = 5
# Output: [9,8,6,5,3]
#
#
# Example 2:
#
#
# Input: nums1 = [6,7], nums2 = [6,0,4], k = 5
# Output: [6,7,6,0,4]
#
#
# Example 3:
#
#
# Input: nums1 = [3,9], nums2 = [8,9], k = 3
# Output: [9,8,9]
#
#
#
# Constraints:
#
#
# m == nums1.length
# n == nums2.length
# 1 <= m, n <= 500
# 0 <= nums1[i], nums2[i] <= 9
# 1 <= k <= m + n
#
#
#

# @lc tags=dynamic-programming;greedy

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 给定两个数字，求这两个数字中的每位组合在一起能组成的最大的k位数值，满足在同意数字中的次序稳定。
# 将问题分解成三个问题，第一个是在一个数字中，组成最大的k位数值；第二个是将两个数组，顺序稳定，组成的最大数值；第三个就是主问题，将k位拆成两个i与j位，满足i+j=k，之后再组合，找最大值。。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def maxNumber(self, nums1: List[int], nums2: List[int],
                  k: int) -> List[int]:
        def maxInOneNums(nums, k):
            result = []
            if k == 0:
                return result
            for m in range(len(nums)):
                while result and len(result) + (
                        len(nums) - m) > k and result[-1] < nums[m]:
                    result.pop()
                if len(result) < k:
                    result.append(nums[m])
                    continue
            return result

        def bigger(nums1: List[int], nums2: List[int], i1, i2):
            while True:
                if i1 == len(nums1):
                    return False
                if i2 == len(nums2):
                    return True

                if nums1[i1] > nums2[i2]:
                    return True
                elif nums1[i1] < nums2[i2]:
                    return False
                i1 += 1
                i2 += 1

        def maxInTwoNums(nums1: List[int], nums2: List[int], i1, i2):
            result = []
            while True:
                if bigger(nums1, nums2, i1, i2):
                    result.append(nums1[i1])
                    i1 += 1
                else:
                    result.append(nums2[i2])
                    i2 += 1
                if i1 == len(nums1) and i2 == len(nums2):
                    return result

        lengthL = max(0, k - len(nums2))
        lengthR = min(len(nums1), k)
        result = nums1[:lengthR] + nums2[:k - lengthR]
        for k1 in range(lengthL, lengthR + 1):
            k2 = k - k1
            result1 = maxInOneNums(nums1, k1)
            result2 = maxInOneNums(nums2, k2)
            resultT = maxInTwoNums(result1, result2, 0, 0)
            if bigger(resultT, result, 0, 0):
                result = resultT
        return result


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print(
        str(Solution().maxNumber([
            6, 9, 2, 3, 6, 7, 9, 9, 0, 9, 6, 2, 3, 3, 3, 4, 7, 4, 5, 6, 8, 5,
            0, 4, 9, 9, 0, 7, 8, 5, 0, 0, 3, 7, 9, 3
        ], [
            1, 6, 5, 7, 6, 0, 6, 5, 1, 0, 1, 0, 8, 2, 7, 4, 5, 4, 2, 6, 2, 4,
            0, 1, 3, 9, 6, 0, 1, 3, 0, 1, 5, 3, 5, 1, 7, 2, 8, 3, 1, 9, 0, 3,
            4, 5, 1, 7, 6, 1, 5, 9, 8, 5, 9, 9, 8, 7, 6, 0, 3, 9, 0, 2, 8, 7,
            5, 4, 0, 5, 1, 8, 3, 2, 2, 7, 8, 9, 8, 5, 7, 4, 8, 1, 1, 1, 6, 5,
            7, 1, 1, 4, 0, 4, 2, 3, 3, 3, 6, 2, 0, 2, 1, 3, 7, 9, 7, 2, 8, 0,
            6, 9, 0, 2, 1, 8, 4, 6, 7, 9, 2, 5, 9, 4, 6, 1, 9, 5, 7, 9, 4, 1,
            0, 6, 8, 0, 1, 3, 9, 4, 2, 9, 8, 0, 6, 9, 0, 7, 3, 4, 6, 2, 4, 8,
            3, 2, 4, 1, 8, 3, 8, 1, 3, 9, 0, 9, 3, 5, 8, 2, 7, 5, 3, 7, 3, 1,
            3, 5, 9, 8
        ], 180)))
    print(
        str(Solution().maxNumber([8, 5, 9, 5, 1, 6, 9],
                                 [2, 6, 4, 3, 8, 4, 1, 0, 7, 2, 9, 2, 8], 20)))
    print(str(Solution().maxNumber([5, 2, 2], [6, 4, 1], 3)))

    print('Example 1:')
    print('Input : ')
    print('nums1 = [3,4,6,5], nums2 = [9,1,2,5,8,3], k = 5')
    print('Exception :')
    print('[9,8,6,5,3]')
    print('Output :')
    print(str(Solution().maxNumber([3, 4, 6, 5], [9, 1, 2, 5, 8, 3], 5)))
    print()

    print('Example 2:')
    print('Input : ')
    print('nums1 = [6,7], nums2 = [6,0,4], k = 5')
    print('Exception :')
    print('[6,7,6,0,4]')
    print('Output :')
    print(str(Solution().maxNumber([6, 7], [6, 0, 4], 5)))
    print()

    print('Example 3:')
    print('Input : ')
    print('nums1 = [3,9], nums2 = [8,9], k = 3')
    print('Exception :')
    print('[9,8,9]')
    print('Output :')
    print(str(Solution().maxNumber([3, 9], [8, 9], 3)))
    print()

    pass
# @lc main=end