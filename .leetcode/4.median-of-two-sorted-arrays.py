# @lc app=leetcode id=4 lang=python3
#
# [4] Median of Two Sorted Arrays
#
# https://leetcode.com/problems/median-of-two-sorted-arrays/description/
#
# algorithms
# Hard (31.35%)
# Likes:    9663
# Dislikes: 1486
# Total Accepted:    904.5K
# Total Submissions: 2.9M
# Testcase Example:  '[1,3]\n[2]'
#
# Given two sorted arrays nums1 and nums2 of size m and n respectively, return
# the median of the two sorted arrays.
#
#
# Example 1:
#
#
# Input: nums1 = [1,3], nums2 = [2]
# Output: 2.00000
# Explanation: merged array = [1,2,3] and median is 2.
#
#
# Example 2:
#
#
# Input: nums1 = [1,2], nums2 = [3,4]
# Output: 2.50000
# Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
#
#
# Example 3:
#
#
# Input: nums1 = [0,0], nums2 = [0,0]
# Output: 0.00000
#
#
# Example 4:
#
#
# Input: nums1 = [], nums2 = [1]
# Output: 1.00000
#
#
# Example 5:
#
#
# Input: nums1 = [2], nums2 = []
# Output: 2.00000
#
#
#
# Constraints:
#
#
# nums1.length == m
# nums2.length == n
# 0 <= m <= 1000
# 0 <= n <= 1000
# 1 <= m + n <= 2000
# -10^6 <= nums1[i], nums2[i] <= 10^6
#
#
#
# Follow up: The overall run time complexity should be O(log (m+n)).
#

# @lc tags=array;binary-search;divide-and-conquer

# @lc imports=start
from imports import *
# @lc imports=end

# @lc idea=start
#
# 求两个排序过的数组的中位数，同时要求时间复杂度是 lg n+m 级别，所以只能用分治法。
# 若是一个数组求中位数，直接在左侧移除一定数量的元素，剩下的最小的就是中位数了，但现在有两个数组，那么就需要比较两个数组中的元素大小了。 
# 首先的想法是，先计算左右两侧个需要移除多少个元素，之后直接比较两个数组当前范围内的中位数大小，若较小的一方左侧元素少于左侧需要移除的元素个数，就移除较小的一方所有左侧元素，较大一方同理。
# 但这样有几个问题，最突出的是虽然少于需要移除的元素个数，但是较大的一方的左侧元素可能小于较小的一方左侧元素，这样有可能直接删掉了中位数。
# 所以现在不是比较中位数，而是通过一侧需要移除的元素数来确定比较位置，由于这里是两个数组，取比较元素与边界的距离就是元素数的一半，之后比较，就可以安全的移除元素了，因为即使另一个数组的元素更小，那么现在移除的元素也是在需要移除元素的范围内的。
#
# @lc idea=end

# @lc group=

# @lc rank=

# @lc code=start


class Solution:

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # 若只有一个数组就可以直接获得中位数
        if (len(nums1) == 0):
            return (nums2[(len(nums2)-1)//2] + nums2[(len(nums2)-1)//2 + 1-len(nums2) % 2])/2
        elif (len(nums2) == 0):
            return (nums1[(len(nums1)-1)//2] + nums1[(len(nums1)-1)//2 + 1 - len(nums1) % 2])/2

        # 中位数的第一个位置
        firstTarget = (len(nums1) + len(nums2)-1)//2
        # 若长度为偶数，则第二个位置在第一个位置的右侧一位
        secondTarget = firstTarget + 1 - (len(nums1) + len(nums2)) % 2

        # 数组的范围
        firstLeft = 0
        firstRight = len(nums1)-1
        secondLeft = 0
        secondRight = len(nums2) - 1

        # 需要删除的数量
        leftNeedRemove = firstTarget 
        rightNeedRemove = (len(nums1) + len(nums2)-1) - secondTarget
        # print([firstTarget, secondTarget])

        while(True):
            # 其中一个已经是空的了
            if (firstRight+1 == firstLeft):
                return (nums2[secondLeft+leftNeedRemove] +nums2[secondLeft+leftNeedRemove + secondTarget - firstTarget] )/2
            if (secondRight+1 == secondLeft):
                return (nums1[firstLeft+leftNeedRemove] +nums1[firstLeft+leftNeedRemove + secondTarget - firstTarget] )/2
        
            # 数组很小的之后，可以直接排序
            # 6 items
            if (firstRight - firstLeft + secondRight - secondLeft) < 4:
                temp = nums1[firstLeft:firstRight+1] + \
                    nums2[secondLeft:secondRight+1]
                temp.sort()
                # print(temp)

                return (temp[firstTarget-(firstLeft+secondLeft)] + temp[secondTarget-(firstLeft+secondLeft)])/2

            # 取需要移除数量较大的一侧
            if (leftNeedRemove > rightNeedRemove):

                # 取一半
                half = (leftNeedRemove - 1)//2

                # 不能越界呀
                firstT =( firstLeft + half )if firstLeft + half <= firstRight else firstRight
                secondT = (secondLeft + half )if secondLeft + half <= secondRight else secondRight

                # 移除较小的
                if (nums1[firstT] < nums2[secondT]):
                    leftNeedRemove -= firstT + 1 - firstLeft
                    firstLeft = firstT + 1
                else:
                    leftNeedRemove -= secondT + 1 - secondLeft
                    secondLeft = secondT + 1
            else:

                # 同理
                half = (rightNeedRemove - 1)//2
                firstT = (firstRight - half) if firstRight - half >= firstLeft else firstLeft
                secondT = (secondRight - half )if (secondRight - half )>= secondLeft else secondLeft

                # 移除较大的
                if (nums1[firstT] < nums2[secondT]):
                    rightNeedRemove -= secondRight - (secondT - 1)
                    secondRight = secondT - 1
                else:
                    rightNeedRemove -= firstRight - (firstT - 1)
                    firstRight = firstT - 1

            pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('nums1 = [1,3], nums2 = [2]')
    print('Output :')
    print(str(Solution().findMedianSortedArrays([1,3],[2])))
    print('Exception :')
    print('2.00000')
    print()
    
    print('Example 2:')
    print('Input : ')
    print('nums1 = [1,2], nums2 = [3,4]')
    print('Output :')
    print(str(Solution().findMedianSortedArrays([1,2],[3,4])))
    print('Exception :')
    print('2.50000')
    print()
    
    print('Example 3:')
    print('Input : ')
    print('nums1 = [0,0], nums2 = [0,0]')
    print('Output :')
    print(str(Solution().findMedianSortedArrays([0,0],[0,0])))
    print('Exception :')
    print('0.00000')
    print()
    
    print('Example 4:')
    print('Input : ')
    print('nums1 = [], nums2 = [1]')
    print('Output :')
    print(str(Solution().findMedianSortedArrays([],[1])))
    print('Exception :')
    print('1.00000')
    print()
    
    print('Example 5:')
    print('Input : ')
    print('nums1 = [2], nums2 = []')
    print('Output :')
    print(str(Solution().findMedianSortedArrays([2],[])))
    print('Exception :')
    print('2.00000')
    print()
    
    pass
# @lc main=end