# @lc app=leetcode id=230 lang=python3
#
# [230] Kth Smallest Element in a BST
#
# https://leetcode.com/problems/kth-smallest-element-in-a-bst/description/
#
# algorithms
# Medium (63.45%)
# Likes:    4133
# Dislikes: 90
# Total Accepted:    558.7K
# Total Submissions: 876.8K
# Testcase Example:  '[3,1,4,null,2]\n1'
#
# Given the root of a binary search tree, and an integer k, return the k^th
# (1-indexed) smallest element in the tree.
#
#
# Example 1:
#
#
# Input: root = [3,1,4,null,2], k = 1
# Output: 1
#
#
# Example 2:
#
#
# Input: root = [5,3,6,2,4,null,null,1], k = 3
# Output: 3
#
#
#
# Constraints:
#
#
# The number of nodes in the tree is n.
# 1 <= k <= n <= 10^4
# 0 <= Node.val <= 10^4
#
#
#
# Follow up: If the BST is modified often (i.e., we can do insert and delete
# operations) and you need to find the kth smallest frequently, how would you
# optimize?
#

# @lc tags=binary-search;tree

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 找二叉搜索树的第k小的元素。
# 直接深度优先，递归。
#
# @lc idea=end

# @lc group=

# @lc rank=

# @lc code=start


class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        def rkthSmallest(root: TreeNode, k: int):
            if not root:
                return None, 0

            retL, countL = rkthSmallest(root.left, k)
            if retL is not None:
                return retL, 0
            k -= countL
            if k == 1:
                return root.val, 0
            retR, countR = rkthSmallest(root.right, k - 1)
            if retR is not None:
                return retR, 0
            return None, countL + countR + 1

        return rkthSmallest(root, k)[0]


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print(
        str(Solution().kthSmallest(
            listToTreeNode([
                31, 30, 48, 3, None, 38, 49, 0, 16, 35, 47, None, None, None,
                2, 15, 27, 33, 37, 39, None, 1, None, 5, None, 22, 28, 32, 34,
                36, None, None, 43, None, None, 4, 11, 19, 23, None, 29, None,
                None, None, None, None, None, 40, 46, None, None, 7, 14, 17,
                21, None, 26, None, None, None, 41, 44, None, 6, 10, 13, None,
                None, 18, 20, None, 25, None, None, 42, None, 45, None, None,
                8, None, 12, None, None, None, None, None, 24, None, None,
                None, None, None, None, 9
            ]), 1)))
    print('Example 1:')
    print('Input : ')
    print('root = [3,1,4,null,2], k = 1')
    print('Exception :')
    print('1')
    print('Output :')
    print(str(Solution().kthSmallest(listToTreeNode([3, 1, 4, None, 2]), 1)))

    print()

    print('Example 2:')
    print('Input : ')
    print('root = [5,3,6,2,4,null,null,1], k = 3')
    print('Exception :')
    print('3')
    print('Output :')
    print(
        str(Solution().kthSmallest(
            listToTreeNode([5, 3, 6, 2, 4, None, None, 1]), 3)))
    print()

    pass
# @lc main=end