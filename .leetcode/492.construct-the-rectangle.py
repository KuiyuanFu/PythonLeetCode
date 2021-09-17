# @lc app=leetcode id=492 lang=python3
#
# [492] Construct the Rectangle
#
# https://leetcode.com/problems/construct-the-rectangle/description/
#
# algorithms
# Easy (51.45%)
# Likes:    330
# Dislikes: 302
# Total Accepted:    70K
# Total Submissions: 135.9K
# Testcase Example:  '4'
#
# A web developer needs to know how to design a web page's size. So, given a
# specific rectangular web page’s area, your job by now is to design a
# rectangular web page, whose length L and width W satisfy the following
# requirements:
#
#
# The area of the rectangular web page you designed must equal to the given
# target area.
# The width W should not be larger than the length L, which means L >= W.
# The difference between length L and width W should be as small as possible.
#
#
# Return an array [L, W] where L and W are the length and width of the web page
# you designed in sequence.
#
#
# Example 1:
#
#
# Input: area = 4
# Output: [2,2]
# Explanation: The target area is 4, and all the possible ways to construct it
# are [1,4], [2,2], [4,1].
# But according to requirement 2, [1,4] is illegal; according to requirement
# 3,  [4,1] is not optimal compared to [2,2]. So the length L is 2, and the
# width W is 2.
#
#
# Example 2:
#
#
# Input: area = 37
# Output: [37,1]
#
#
# Example 3:
#
#
# Input: area = 122122
# Output: [427,286]
#
#
#
# Constraints:
#
#
# 1 <= area <= 10^7
#
#
#

# @lc tags=Unknown

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 给定面积，求长宽差距最小的两个整数。
# 简单遍历
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        l = int(sqrt(area - 1)) + 1
        while area % l:
            l += 1
        return [l, area // l]
        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('area = 4')
    print('Exception :')
    print('[2,2]')
    print('Output :')
    print(str(Solution().constructRectangle(4)))
    print()

    print('Example 2:')
    print('Input : ')
    print('area = 37')
    print('Exception :')
    print('[37,1]')
    print('Output :')
    print(str(Solution().constructRectangle(37)))
    print()

    print('Example 3:')
    print('Input : ')
    print('area = 122122')
    print('Exception :')
    print('[427,286]')
    print('Output :')
    print(str(Solution().constructRectangle(122122)))
    print()
    print(str(Solution().constructRectangle(2)))
    print(str(Solution().constructRectangle(4)))
    pass
# @lc main=end