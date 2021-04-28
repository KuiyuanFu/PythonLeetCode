# @lc app=leetcode id=42 lang=python3
#
# [42] Trapping Rain Water
#
# https://leetcode.com/problems/trapping-rain-water/description/
#
# algorithms
# Hard (51.57%)
# Likes:    10752
# Dislikes: 159
# Total Accepted:    719.2K
# Total Submissions: 1.4M
# Testcase Example:  '[0,1,0,2,1,0,1,3,2,1,2,1]'
#
# Given n non-negative integers representing an elevation map where the width
# of each bar is 1, compute how much water it can trap after raining.
#
#
# Example 1:
#
#
# Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6
# Explanation: The above elevation map (black section) is represented by array
# [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section)
# are being trapped.
#
#
# Example 2:
#
#
# Input: height = [4,2,0,3,2,5]
# Output: 9
#
#
#
# Constraints:
#
#
# n == height.length
# 0 <= n <= 3 * 10^4
# 0 <= height[i] <= 10^5
#
#
#
#
#

# @lc tags=array;two-pointers;stack

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 求一系列柱子，最多可以接到多少水。每个柱子宽度为1，间距也为1，即等高的两个相邻柱子中间不能盛水。
# 双指针，初始状态为最左和最右两根柱子，每一次根据较小的高度和指针距离确定这个高度的容积。
# 计算的容积比实际要多，因为之间有的柱子高度不一定为零，之后减去之后遍历时遇到的高度与水平面的较小值，也就是之前多计算的水的体积。
#
# @lc idea=end

# @lc group=two-pointers

# @lc rank=10


# @lc code=start
class Solution:
    def trap(self, height: List[int]) -> int:

        # 一根怎么可能成功
        if len(height) < 2:
            return 0

        water = 0
        l, r = 0, len(height) - 1
        hPre = 0
        while l < r:
            # 当前水面高度
            h = min(height[l], height[r])
            # 增加的容积
            water += (h - hPre) * (r - l - 1)
            hPre = h
            if r - l == 1:
                break
            # 左侧较低
            if height[l] < height[r]:
                lPre = l
                while l + 1 < r:
                    l = l + 1
                    # 减掉多算的容积
                    water -= min(height[l], hPre)
                    # 找到一根更高的柱子
                    if height[lPre] < height[l]:
                        break
            else:
                rPre = r
                while l < r - 1:
                    r = r - 1
                    water -= min(height[r], hPre)
                    if height[rPre] < height[r]:
                        break

        return water

        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('height = [0,1,0,2,1,0,1,3,2,1,2,1]')
    print('Output :')
    print(str(Solution().trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1])))
    print('Exception :')
    print('6')
    print()

    print('Example 2:')
    print('Input : ')
    print('height = [4,2,0,3,2,5]')
    print('Output :')
    print(str(Solution().trap([4, 2, 0, 3, 2, 5])))
    print('Exception :')
    print('9')
    print()

    pass
# @lc main=end