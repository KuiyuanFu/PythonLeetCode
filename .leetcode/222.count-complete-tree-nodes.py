# @lc app=leetcode id=222 lang=python3
#
# [222] Count Complete Tree Nodes
#
# https://leetcode.com/problems/count-complete-tree-nodes/description/
#
# algorithms
# Medium (50.30%)
# Likes:    3083
# Dislikes: 262
# Total Accepted:    304K
# Total Submissions: 601K
# Testcase Example:  '[1,2,3,4,5,6]'
#
# Given the root of a complete binary tree, return the number of the nodes in
# the tree.
#
# According to Wikipedia, every level, except possibly the last, is completely
# filled in a complete binary tree, and all nodes in the last level are as far
# left as possible. It can have between 1 and 2^h nodes inclusive at the last
# level h.
#
# Design an algorithm that runs in less than O(n) time complexity.
#
#
# Example 1:
#
#
# Input: root = [1,2,3,4,5,6]
# Output: 6
#
#
# Example 2:
#
#
# Input: root = []
# Output: 0
#
#
# Example 3:
#
#
# Input: root = [1]
# Output: 1
#
#
#
# Constraints:
#
#
# The number of nodes in the tree is in the range [0, 5 * 10^4].
# 0 <= Node.val <= 5 * 10^4
# The tree is guaranteed to be complete.
#
#
#

# @lc tags=binary-search;tree

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 计算一棵完全二叉树的结点个数。
# 二分法，找最后一层的节点个数。
#
# @lc idea=end

# @lc group=

# @lc rank=

# @lc code=start


class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0

        # calc n
        p = root
        n = 0
        while p:
            n += 1
            p = p.left
        # calc skip number
        n = n - 1
        l, r = 0, 2**n - 1
        length = [2**i for i in reversed(range(n))]
        # test exist
        while l < r:
            m = (l + r + 1) // 2
            t = m
            p = root
            for i in range(n):
                if t >= length[i]:
                    p = p.right
                    t -= length[i]
                else:
                    p = p.left
            if p:
                l = m
            else:
                r = m - 1
        return (2**(n)) - 1 + l + 1
        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print(str(Solution().countNodes(listToTreeNode([1, 2, 3, 4, 5, 6, 7, 8]))))
    print(str(Solution().countNodes(listToTreeNode([1, 2, 3, 4, 5, 6, 7]))))
    print('Example 1:')
    print('Input : ')
    print('root = [1,2,3,4,5,6]')
    print('Exception :')
    print('6')
    print('Output :')
    print(str(Solution().countNodes(listToTreeNode([1, 2, 3, 4, 5, 6]))))
    print()

    print('Example 2:')
    print('Input : ')
    print('root = []')
    print('Exception :')
    print('0')
    print('Output :')
    print(str(Solution().countNodes(listToTreeNode([]))))
    print()

    print('Example 3:')
    print('Input : ')
    print('root = [1]')
    print('Exception :')
    print('1')
    print('Output :')
    print(str(Solution().countNodes(listToTreeNode([1]))))
    print()

    pass
# @lc main=end