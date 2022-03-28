# @lc app=leetcode id=863 lang=python3
#
# [863] All Nodes Distance K in Binary Tree
#
# https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/description/
#
# algorithms
# Medium (60.74%)
# Likes:    5921
# Dislikes: 122
# Total Accepted:    220.5K
# Total Submissions: 362.1K
# Testcase Example:  '[3,5,1,6,2,0,8,null,null,7,4]\n5\n2'
#
# Given the root of a binary tree, the value of a target node target, and an
# integer k, return an array of the values of all nodes that have a distance k
# from the target node.
#
# You can return the answer in any order.
#
#
# Example 1:
#
#
# Input: root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, k = 2
# Output: [7,4,1]
# Explanation: The nodes that are a distance 2 from the target node (with value
# 5) have values 7, 4, and 1.
#
#
# Example 2:
#
#
# Input: root = [1], target = 1, k = 3
# Output: []
#
#
#
# Constraints:
#
#
# The number of nodes in the tree is in the range [1, 500].
# 0 <= Node.val <= 500
# All the values Node.val are unique.
# target is the value of one of the nodes in the tree.
# 0 <= k <= 1000
#
#
#

# @lc tags=tree;depth-first-search

# @lc imports=start
from logging import RootLogger
from imports import *
# @lc imports=end

# @lc idea=start
#
# 树上距离指定结点指定距离的所有结点。
# dfs
#
# @lc idea=end

# @lc group=

# @lc rank=

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        # dfs
        p = root

        buffer = []
        res = []
        while True:
            if p is not None:
                if p.val == target.val:
                    l = 0
                    dp = [(p, 0)]
                    while buffer:
                        l += 1
                        p, f = buffer.pop()
                        if l == k:
                            res.append(p.val)
                            break
                        if f:
                            dp.append((p.right, l + 1))
                        else:
                            dp.append((p.left, l + 1))

                    while dp:
                        p, l = dp.pop()
                        if p == None:
                            continue
                        if l == k:
                            res.append(p.val)
                        else:
                            dp.append((p.left, l + 1))
                            dp.append((p.right, l + 1))
                    break

                else:
                    buffer.append((p, True))
                    p = p.left

            elif len(buffer) > 0:
                p, goLeft = buffer.pop()
                if goLeft:
                    buffer.append((p, False))
                    p = p.right
                else:
                    p = None
            else:
                break

        return res
        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print(
        str(Solution().distanceK(listToTreeNode([0, 1, None, 3, 2]),
                                 listToTreeNode([2]), 1)))
    print('Example 1:')
    print('Input : ')
    print('root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, k = 2')
    print('Exception :')
    print('[7,4,1]')
    print('Output :')
    print(
        str(Solution().distanceK(
            listToTreeNode([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]),
            listToTreeNode([5]), 2)))
    print()

    print('Example 2:')
    print('Input : ')
    print('root = [1], target = 1, k = 3')
    print('Exception :')
    print('[]')
    print('Output :')
    print(
        str(Solution().distanceK(listToTreeNode([1]), listToTreeNode([1]), 3)))
    print()

    pass
# @lc main=end