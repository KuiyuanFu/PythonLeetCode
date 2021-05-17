# @lc app=leetcode id=108 lang=python3
#
# [108] Convert Sorted Array to Binary Search Tree
#
# https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/description/
#
# algorithms
# Easy (61.10%)
# Likes:    3901
# Dislikes: 282
# Total Accepted:    534.3K
# Total Submissions: 870.8K
# Testcase Example:  '[-10,-3,0,5,9]'
#
# Given an integer array nums where the elements are sorted in ascending order,
# convert it to a height-balanced binary search tree.
#
# A height-balanced binary tree is a binary tree in which the depth of the two
# subtrees of every node never differs by more than one.
#
#
# Example 1:
#
#
# Input: nums = [-10,-3,0,5,9]
# Output: [0,-3,9,-10,null,5]
# Explanation: [0,-10,5,null,-3,null,9] is also accepted:
#
#
#
# Example 2:
#
#
# Input: nums = [1,3]
# Output: [3,1]
# Explanation: [1,3] and [3,1] are both a height-balanced BSTs.
#
#
#
# Constraints:
#
#
# 1 <= nums.length <= 10^4
# -10^4 <= nums[i] <= 10^4
# nums is sorted in a strictly increasing order.
#
#
#

# @lc tags=tree;depth-first-search

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 给定一个升序数组，得到平衡二叉搜索树。
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
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        def recur(l, r):
            if r - l == 0:
                return None
            m = (r + l) // 2
            val = nums[m]
            root = TreeNode(val)
            root.left = recur(l, m)
            root.right = recur(m + 1, r)
            return root

        return recur(0, len(nums))
        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('nums = [-10,-3,0,5,9]')
    print('Output :')
    print(str(Solution().sortedArrayToBST([-10, -3, 0, 5, 9])))
    print('Exception :')
    print('[0,-3,9,-10,null,5]')
    print()

    print('Example 2:')
    print('Input : ')
    print('nums = [1,3]')
    print('Output :')
    print(str(Solution().sortedArrayToBST([1, 3])))
    print('Exception :')
    print('[3,1]')
    print()

    pass
# @lc main=end