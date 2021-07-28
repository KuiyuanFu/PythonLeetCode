# @lc app=leetcode id=331 lang=python3
#
# [331] Verify Preorder Serialization of a Binary Tree
#
# https://leetcode.com/problems/verify-preorder-serialization-of-a-binary-tree/description/
#
# algorithms
# Medium (41.41%)
# Likes:    1073
# Dislikes: 62
# Total Accepted:    83.4K
# Total Submissions: 201.5K
# Testcase Example:  '"9,3,4,#,#,1,#,#,2,#,6,#,#"'
#
# One way to serialize a binary tree is to use preorder traversal. When we
# encounter a non-null node, we record the node's value. If it is a null node,
# we record using a sentinel value such as '#'.
#
# For example, the above binary tree can be serialized to the string
# "9,3,4,#,#,1,#,#,2,#,6,#,#", where '#' represents a null node.
#
# Given a string of comma-separated values preorder, return true if it is a
# correct preorder traversal serialization of a binary tree.
#
# It is guaranteed that each comma-separated value in the string must be either
# an integer or a character '#' representing null pointer.
#
# You may assume that the input format is always valid.
#
#
# For example, it could never contain two consecutive commas, such as "1,,3".
#
#
# Note: You are not allowed to reconstruct the tree.
#
#
# Example 1:
# Input: preorder = "9,3,4,#,#,1,#,#,2,#,6,#,#"
# Output: true
# Example 2:
# Input: preorder = "1,#"
# Output: false
# Example 3:
# Input: preorder = "9,#,#,1"
# Output: false
#
#
# Constraints:
#
#
# 1 <= preorder.length <= 10^4
# preoder consist of integers in the range [0, 100] and '#' separated by commas
# ','.
#
#
#

# @lc tags=stack

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 给定一个先序遍历的二叉树序列，空节点用‘#’表示，判断其是否是一个二叉树。
# 直接记录还可以插入的节点位置，遇到‘#’表示消耗了一个，而其他值，说明有两个子节点，就相当于多了一个。遍历节点列表即可。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        buffer = preorder.split(',')
        n = 1
        for k in buffer:
            if n < 1:
                return False
            n -= 1
            if k != '#':
                n += 2

        return n == 0


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('preorder = "9,3,4,#,#,1,#,#,2,#,6,#,#"')
    print('Exception :')
    print('true')
    print('Output :')
    print(str(Solution().isValidSerialization("9,3,4,#,#,1,#,#,2,#,6,#,#")))
    print()

    print('Example 2:')
    print('Input : ')
    print('preorder = "1,#"')
    print('Exception :')
    print('false')
    print('Output :')
    print(str(Solution().isValidSerialization("1,#")))
    print()

    print('Example 3:')
    print('Input : ')
    print('preorder = "9,#,#,1"')
    print('Exception :')
    print('false')
    print('Output :')
    print(str(Solution().isValidSerialization("9,#,#,1")))
    print()

    pass
# @lc main=end