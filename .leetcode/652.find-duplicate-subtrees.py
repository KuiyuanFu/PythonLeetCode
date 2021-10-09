# @lc app=leetcode id=652 lang=python3
#
# [652] Find Duplicate Subtrees
#
# https://leetcode.com/problems/find-duplicate-subtrees/description/
#
# algorithms
# Medium (54.24%)
# Likes:    2529
# Dislikes: 265
# Total Accepted:    115.7K
# Total Submissions: 212.3K
# Testcase Example:  '[1,2,3,4,null,2,4,null,null,4]'
#
# Given the root of a binary tree, return all duplicate subtrees.
#
# For each kind of duplicate subtrees, you only need to return the root node of
# any one of them.
#
# Two trees are duplicate if they have the same structure with the same node
# values.
#
#
# Example 1:
#
#
# Input: root = [1,2,3,4,null,2,4,null,null,4]
# Output: [[2,4],[4]]
#
#
# Example 2:
#
#
# Input: root = [2,1,1]
# Output: [[1]]
#
#
# Example 3:
#
#
# Input: root = [2,2,2,3,null,3,null]
# Output: [[2,3],[3]]
#
#
#
# Constraints:
#
#
# The number of the nodes in the tree will be in the range [1, 10^4]
# -200 <= Node.val <= 200
#
#
#

# @lc tags=tree

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 返回相同的子树。
# 用字典保存每个节点的特征，特征为左右子树的特征加上此节点的值。
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
    def findDuplicateSubtrees(
            self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        dic = {}
        res = {}

        def recur(p: Optional[TreeNode]):
            l = recur(p.left) if p.left else None
            r = recur(p.right) if p.right else None
            m = p.val
            k = (l, m, r)
            if k in dic:
                res[k] = p
            else:
                dic[k] = len(dic)
            return dic[k]

        recur(root)
        return list(res.values())

        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('root = [1,2,3,4,null,2,4,null,null,4]')
    print('Exception :')
    print('[[2,4],[4]]')
    print('Output :')
    print(
        str(Solution().findDuplicateSubtrees(
            listToTreeNode([1, 2, 3, 4, None, 2, 4, None, None, 4]))))
    print()

    print('Example 2:')
    print('Input : ')
    print('root = [2,1,1]')
    print('Exception :')
    print('[[1]]')
    print('Output :')
    print(str(Solution().findDuplicateSubtrees(listToTreeNode([2, 1, 1]))))
    print()

    print('Example 3:')
    print('Input : ')
    print('root = [2,2,2,3,null,3,null]')
    print('Exception :')
    print('[[2,3],[3]]')
    print('Output :')
    print(
        str(Solution().findDuplicateSubtrees(
            listToTreeNode([2, 2, 2, 3, None, 3, None]))))
    print()

    pass
# @lc main=end