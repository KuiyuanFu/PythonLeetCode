# @lc app=leetcode id=84 lang=python3
#
# [84] Largest Rectangle in Histogram
#
# https://leetcode.com/problems/largest-rectangle-in-histogram/description/
#
# algorithms
# Hard (37.49%)
# Likes:    5660
# Dislikes: 112
# Total Accepted:    355.2K
# Total Submissions: 946.8K
# Testcase Example:  '[2,1,5,6,2,3]'
#
# Given an array of integers heights representing the histogram's bar height
# where the width of each bar is 1, return the area of the largest rectangle in
# the histogram.
#
#
# Example 1:
#
#
# Input: heights = [2,1,5,6,2,3]
# Output: 10
# Explanation: The above is a histogram where width of each bar is 1.
# The largest rectangle is shown in the red area, which has an area = 10
# units.
#
#
# Example 2:
#
#
# Input: heights = [2,4]
# Output: 4
#
#
#
# Constraints:
#
#
# 1 <= heights.length <= 10^5
# 0 <= heights[i] <= 10^4
#
#
#

# @lc tags=array;stack

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 给定一个直方图，求最大的矩形区域。
# 从左至右依次遍历，用一个栈表示到此索引时，左侧能保持的高度及起始索引值。栈中的元素是递增的，因为若右侧高度比左侧低，左侧就不能保持高度了。
#
# @lc idea=end

# @lc group=stack

# @lc rank=7


# @lc code=start
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        if len(heights) == 0:
            return 0

        hStack = [heights[0]]
        iStack = [0]
        maxArea = heights[0]

        for i, h in enumerate(heights):
            if h > hStack[-1]:

                hStack.append(h)
                iStack.append(i)
            else:
                iRight = iStack[-1]
                while len(hStack) > 0 and h <= hStack[-1]:
                    area = (i - iStack[-1]) * hStack[-1]
                    if area > maxArea:
                        maxArea = area

                    hStack.pop()
                    iRight = iStack.pop()
                hStack.append(h)
                iStack.append(iRight)

        while len(hStack) > 0:
            h = hStack.pop()
            i = iStack.pop()
            area = (len(heights) - i) * h
            if area > maxArea:
                maxArea = area
        return maxArea
        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('heights = [2,1,5,6,2,3]')
    print('Output :')
    print(str(Solution().largestRectangleArea([2, 1, 5, 6, 2, 3])))
    print('Exception :')
    print('10')
    print()

    print('Example 2:')
    print('Input : ')
    print('heights = [2,4]')
    print('Output :')
    print(str(Solution().largestRectangleArea([2, 4])))
    print('Exception :')
    print('4')
    print()

    pass
# @lc main=end