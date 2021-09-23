# @lc app=leetcode id=546 lang=python3
#
# [546] Remove Boxes
#
# https://leetcode.com/problems/remove-boxes/description/
#
# algorithms
# Hard (47.23%)
# Likes:    1318
# Dislikes: 86
# Total Accepted:    31.4K
# Total Submissions: 66.6K
# Testcase Example:  '[1,3,2,2,2,3,4,3,1]'
#
# You are given several boxes with different colors represented by different
# positive numbers.
#
# You may experience several rounds to remove boxes until there is no box left.
# Each time you can choose some continuous boxes with the same color (i.e.,
# composed of k boxes, k >= 1), remove them and get k * k points.
#
# Return the maximum points you can get.
#
#
# Example 1:
#
#
# Input: boxes = [1,3,2,2,2,3,4,3,1]
# Output: 23
# Explanation:
# [1, 3, 2, 2, 2, 3, 4, 3, 1]
# ----> [1, 3, 3, 4, 3, 1] (3*3=9 points)
# ----> [1, 3, 3, 3, 1] (1*1=1 points)
# ----> [1, 1] (3*3=9 points)
# ----> [] (2*2=4 points)
#
#
# Example 2:
#
#
# Input: boxes = [1,1,1]
# Output: 9
#
#
# Example 3:
#
#
# Input: boxes = [1]
# Output: 1
#
#
#
# Constraints:
#
#
# 1 <= boxes.length <= 100
# 1 <= boxes[i] <= 100
#
#
#

# @lc tags=dynamic-programming;depth-first-search

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 移除箱子，每次移除相邻同色箱子，得分为每次移除个数的二次方。求最多分。
# 自顶向下，递归。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def removeBoxes(self, boxes: List[int]) -> int:
        length = len(boxes)
        dp = [[[0 for _ in range(length)] for _ in range(length)]
              for _ in range(length)]

        def recur(l, r, length):
            if l > r:
                return length * length

            if dp[l][r][length] > 0:
                return dp[l][r][length]
            res = (length + 1)**2 + recur(l + 1, r, 0)
            for i in range(l + 1, r + 1):
                if boxes[i] == boxes[l]:
                    resT = recur(l + 1, i - 1, 0) + recur(i, r, length + 1)
                    res = max(resT, res)
            dp[l][r][length] = res
            return res

        return recur(0, len(boxes) - 1, 0)
        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('boxes = [1,3,2,2,2,3,4,3,1]')
    print('Exception :')
    print('23')
    print('Output :')
    print(str(Solution().removeBoxes([1, 3, 2, 2, 2, 3, 4, 3, 1])))
    print()

    print('Example 2:')
    print('Input : ')
    print('boxes = [1,1,1]')
    print('Exception :')
    print('9')
    print('Output :')
    print(str(Solution().removeBoxes([1, 1, 1])))
    print()

    print('Example 3:')
    print('Input : ')
    print('boxes = [1]')
    print('Exception :')
    print('1')
    print('Output :')
    print(str(Solution().removeBoxes([1])))
    print()

    pass
# @lc main=end