# @lc app=leetcode id=11 lang=python3
#
# [11] Container With Most Water
#
# https://leetcode.com/problems/container-with-most-water/description/
#
# algorithms
# Medium (52.91%)
# Likes:    9053
# Dislikes: 697
# Total Accepted:    914.4K
# Total Submissions: 1.7M
# Testcase Example:  '[1,8,6,2,5,4,8,3,7]'
#
# Given n non-negative integers a1, a2, ..., an , where each represents a point
# at coordinate (i, ai). n vertical lines are drawn such that the two endpoints
# of the line i is at (i, ai) and (i, 0). Find two lines, which, together with
# the x-axis forms a container, such that the container contains the most
# water.
#
# Notice that you may not slant the container.
#
#
# Example 1:
#
#
# Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49
# Explanation: The above vertical lines are represented by array
# [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the
# container can contain is 49.
#
#
# Example 2:
#
#
# Input: height = [1,1]
# Output: 1
#
#
# Example 3:
#
#
# Input: height = [4,3,2,1,4]
# Output: 16
#
#
# Example 4:
#
#
# Input: height = [1,2,1]
# Output: 2
#
#
#
# Constraints:
#
#
# n == height.length
# 2 <= n <= 10^5
# 0 <= height[i] <= 10^4
#
#
#
#

# @lc tags=array;two-pointers

# @lc imports=start
from imports import *
# @lc imports=end

# @lc idea=start
#
# 在一系列柱子中，计算选择两个柱子组成的容器最大的容量。从两侧向内依次找比原来大高的柱子。比如从左侧开始，之后向右找到一根更高的柱子，这根柱子与另一侧柱子组成的容器才有可能大于原来的容器，因为移动时，容器的底变小了。每次都移动较矮的一侧的柱子。
#
# @lc idea=end

# @lc group=two-pointers

# @lc rank=10

# @lc code=start


class Solution:
    def maxArea(self, height: List[int]) -> int:

        leftMax = 0
        rightMax = len(height) - 1
        waterMax = min(height[leftMax],
                       height[rightMax]) * (rightMax - leftMax)
        left = leftMax
        right = rightMax
        while left < right:
            if (height[leftMax] < height[rightMax]):
                left += 1
                while left < right:
                    if height[left] > height[leftMax]:
                        leftMax = left
                        break
                    else:
                        left += 1
            else:
                right -= 1
                while left < right:
                    if height[right] > height[rightMax]:
                        rightMax = right
                        break
                    else:
                        right -= 1

            water = min(height[leftMax], height[rightMax]) * \
                (rightMax - leftMax)
            waterMax = water if water > waterMax else waterMax
        return waterMax

        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('height = [1,8,6,2,5,4,8,3,7]')
    print('Output :')
    print(str(Solution().maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7])))
    print('Exception :')
    print('49')
    print()

    print('Example 2:')
    print('Input : ')
    print('height = [1,1]')
    print('Output :')
    print(str(Solution().maxArea([1, 1])))
    print('Exception :')
    print('1')
    print()

    print('Example 3:')
    print('Input : ')
    print('height = [4,3,2,1,4]')
    print('Output :')
    print(str(Solution().maxArea([4, 3, 2, 1, 4])))
    print('Exception :')
    print('16')
    print()

    print('Example 4:')
    print('Input : ')
    print('height = [1,2,1]')
    print('Output :')
    print(str(Solution().maxArea([1, 2, 1])))
    print('Exception :')
    print('2')
    print()

    pass
# @lc main=end