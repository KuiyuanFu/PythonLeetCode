# @lc app=leetcode id=653 lang=python3
#
# [653] Two Sum IV - Input is a BST
#
# https://leetcode.com/problems/two-sum-iv-input-is-a-bst/description/
#
# algorithms
# Easy (57.56%)
# Likes:    2752
# Dislikes: 175
# Total Accepted:    248.7K
# Total Submissions: 430.4K
# Testcase Example:  '[5,3,6,2,4,null,7]\n9'
#
# Given the root of a Binary Search Tree and a target number k, return true if
# there exist two elements in the BST such that their sum is equal to the given
# target.
#
#
# Example 1:
#
#
# Input: root = [5,3,6,2,4,null,7], k = 9
# Output: true
#
#
# Example 2:
#
#
# Input: root = [5,3,6,2,4,null,7], k = 28
# Output: false
#
#
# Example 3:
#
#
# Input: root = [2,1,3], k = 4
# Output: true
#
#
# Example 4:
#
#
# Input: root = [2,1,3], k = 1
# Output: false
#
#
# Example 5:
#
#
# Input: root = [2,1,3], k = 3
# Output: true
#
#
#
# Constraints:
#
#
# The number of nodes in the tree is in the range [1, 10^4].
# -10^4 <= Node.val <= 10^4
# root is guaranteed to be a valid binary search tree.
# -10^5 <= k <= 10^5
#
#
#

# @lc tags=tree

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 在二叉搜索树中，判断是否有两个数字和为指定值。
# 直接遍历。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        def search(p: Optional[TreeNode], t: int, origin: Optional[TreeNode]):
            while p:
                if p.val == t:
                    return p != origin
                elif p.val < t:
                    p = p.right
                else:
                    p = p.left
            return False

        def recur(p: Optional[TreeNode]):
            return search(root, k - p.val,p) \
                or (p.left is not None and recur(p.left)) \
                or (p.right is not None and recur(p.right))

        return recur(root)

        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':

    print('Example 1:')
    print('Input : ')
    print('root = [5,3,6,2,4,null,7], k = 9')
    print('Exception :')
    print('true')
    print('Output :')
    print(
        str(Solution().findTarget(listToTreeNode([5, 3, 6, 2, 4, None, 7]),
                                  9)))
    print()

    print('Example 2:')
    print('Input : ')
    print('root = [5,3,6,2,4,null,7], k = 28')
    print('Exception :')
    print('false')
    print('Output :')
    print(
        str(Solution().findTarget(listToTreeNode([5, 3, 6, 2, 4, None, 7]),
                                  28)))
    print()

    print('Example 3:')
    print('Input : ')
    print('root = [2,1,3], k = 4')
    print('Exception :')
    print('true')
    print('Output :')
    print(str(Solution().findTarget(listToTreeNode([2, 1, 3]), 4)))
    print()

    print('Example 4:')
    print('Input : ')
    print('root = [2,1,3], k = 1')
    print('Exception :')
    print('false')
    print('Output :')
    print(str(Solution().findTarget(listToTreeNode([2, 1, 3]), 1)))
    print()

    print('Example 5:')
    print('Input : ')
    print('root = [2,1,3], k = 3')
    print('Exception :')
    print('true')
    print('Output :')
    print(str(Solution().findTarget(listToTreeNode([2, 1, 3]), 3)))
    print()
    print(str(Solution().findTarget(listToTreeNode([1]), 2)))
    pass
# @lc main=end