# @lc app=leetcode id=872 lang=python3
#
# [872] Leaf-Similar Trees
#
# https://leetcode.com/problems/leaf-similar-trees/description/
#
# algorithms
# Easy (64.94%)
# Likes:    1625
# Dislikes: 55
# Total Accepted:    160.8K
# Total Submissions: 247.6K
# Testcase Example:  '[3,5,1,6,2,9,8,null,null,7,4]\n' +
# '[3,5,1,6,7,4,2,null,null,null,null,null,null,9,8]'
#
# Consider all the leaves of a binary tree, from left to right order, the
# values of those leaves form a leaf value sequence.
#
#
#
# For example, in the given tree above, the leaf value sequence is (6, 7, 4, 9,
# 8).
#
# Two binary trees are considered leaf-similar if their leaf value sequence is
# the same.
#
# Return true if and only if the two given trees with head nodes root1 and
# root2 are leaf-similar.
#
#
# Example 1:
#
#
# Input: root1 = [3,5,1,6,2,9,8,null,null,7,4], root2 =
# [3,5,1,6,7,4,2,null,null,null,null,null,null,9,8]
# Output: true
#
#
# Example 2:
#
#
# Input: root1 = [1,2,3], root2 = [1,3,2]
# Output: false
#
#
#
# Constraints:
#
#
# The number of nodes in each tree will be in the range [1, 200].
# Both of the given trees will have values in the range [0, 200].
#
#
#

# @lc tags=string;backtracking;greedy

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 叶子是否相同。
# 迭代
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
    def leafSimilar(self, root1: Optional[TreeNode],
                    root2: Optional[TreeNode]) -> bool:
        def getLeaf(p: Optional[TreeNode], ):
            buf = []

            while p:
                if p.left and p.right:
                    buf.append(p.right)
                    p = p.left
                elif p.left:
                    p = p.left
                elif p.right:
                    p = p.right
                else:
                    yield p.val
                    if not buf:
                        return
                    else:
                        p = buf.pop()
            return

        leaf1 = getLeaf(root1)
        leaf2 = getLeaf(root2)

        n1, n2 = False, False
        while True:
            try:
                l1 = next(leaf1)
            except StopIteration:
                n1 = True
            try:
                l2 = next(leaf2)
            except StopIteration:
                n2 = True

            if n1 and n2:
                return True
            if n1 or n2:
                return False
            if l1 != l2:
                return False

        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print(
        'root1 = [3,5,1,6,2,9,8,null,null,7,4], root2 =[3,5,1,6,7,4,2,null,null,null,null,null,null,9,8]'
    )
    print('Exception :')
    print('true')
    print('Output :')
    print(
        str(Solution().leafSimilar(
            listToTreeNode([3, 5, 1, 6, 2, 9, 8, None, None, 7, 4]),
            listToTreeNode([
                3, 5, 1, 6, 7, 4, 2, None, None, None, None, None, None, 9, 8
            ]))))
    print()

    print('Example 2:')
    print('Input : ')
    print('root1 = [1,2,3], root2 = [1,3,2]')
    print('Exception :')
    print('false')
    print('Output :')
    print(
        str(Solution().leafSimilar(listToTreeNode([1, 2, 3]),
                                   listToTreeNode([1, 3, 2]))))
    print()

    pass
# @lc main=end