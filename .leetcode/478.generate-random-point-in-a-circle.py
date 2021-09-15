# @lc app=leetcode id=478 lang=python3
#
# [478] Generate Random Point in a Circle
#
# https://leetcode.com/problems/generate-random-point-in-a-circle/description/
#
# algorithms
# Medium (39.04%)
# Likes:    326
# Dislikes: 626
# Total Accepted:    30.9K
# Total Submissions: 79K
# Testcase Example:  '["Solution","randPoint","randPoint","randPoint"]\n[[1.0,0.0,0.0],[],[],[]]'
#
# Given the radius and the position of the center of a circle, implement the
# function randPoint which generates a uniform random point inside the circle.
#
# Implement the Solution class:
#
#
# Solution(double radius, double x_center, double y_center) initializes the
# object with the radius of the circle radius and the position of the center
# (x_center, y_center).
# randPoint() returns a random point inside the circle. A point on the
# circumference of the circle is considered to be in the circle. The answer is
# returned as an array [x, y].
#
#
#
# Example 1:
#
#
# Input
# ["Solution", "randPoint", "randPoint", "randPoint"]
# [[1.0, 0.0, 0.0], [], [], []]
# Output
# [null, [-0.02493, -0.38077], [0.82314, 0.38945], [0.36572, 0.17248]]
#
# Explanation
# Solution solution = new Solution(1.0, 0.0, 0.0);
# solution.randPoint(); // return [-0.02493, -0.38077]
# solution.randPoint(); // return [0.82314, 0.38945]
# solution.randPoint(); // return [0.36572, 0.17248]
#
#
#
# Constraints:
#
#
# 0 < radius <= 10^8
# -10^7 <= x_center, y_center <= 10^7
# At most 3 * 10^4 calls will be made to randPoint.
#
#
#

# @lc tags=Unknown

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 在给定区域内，随机生成点。
# xy轴分别生成，之后判断位置是否合理。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def __init__(self, radius: float, x_center: float, y_center: float):
        self.r = radius
        self.x = x_center
        self.y = y_center

    def randPoint(self) -> List[float]:

        while True:
            x, y = (random.random() - 0.5) * 2, (random.random() - 0.5) * 2
            if x * x + y * y <= 1:
                x = x * self.r + self.x
                y = y * self.r + self.y
                return [x, y]


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('')
    print('Exception :')
    print('')
    print('Output :')
    print(str(Solution().__init__(error, error, error)))
    print()

    pass
# @lc main=end