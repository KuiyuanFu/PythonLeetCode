# @lc app=leetcode id=199 lang=python3
#
# [199] Binary Tree Right Side View
#
# https://leetcode.com/problems/binary-tree-right-side-view/description/
#
# algorithms
# Medium (56.89%)
# Likes:    4122
# Dislikes: 225
# Total Accepted:    463.2K
# Total Submissions: 812.5K
# Testcase Example:  '[1,2,3,null,5,null,4]'
#
# Given the root of a binary tree, imagine yourself standing on the right side
# of it, return the values of the nodes you can see ordered from top to
# bottom.
#
#
# Example 1:
#
#
# Input: root = [1,2,3,null,5,null,4]
# Output: [1,3,4]
#
#
# Example 2:
#
#
# Input: root = [1,null,3]
# Output: [1,3]
#
#
# Example 3:
#
#
# Input: root = []
# Output: []
#
#
#
# Constraints:
#
#
# The number of nodes in the tree is in the range [0, 100].
# -100 <= Node.val <= 100
#
#
#

# @lc tags=tree;depth-first-search;breadth-first-search

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 给定一个二叉树，计算从右侧能看到的结点。
# 广度优先遍历，得到每一层的最右侧结点。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        result = []
        next = [root]
        while next:
            now, next = next, []
            result.append(now[-1].val)
            for p in now:
                if p.left:
                    next.append(p.left)
                if p.right:
                    next.append(p.right)
        return result
        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('root = [1,2,3,null,5,null,4]')
    print('Exception :')
    print('[1,3,4]')
    print('Output :')
    print(
        str(Solution().rightSideView(
            listToTreeNode([1, 2, 3, None, 5, None, 4]))))
    print()

    print('Example 2:')
    print('Input : ')
    print('root = [1,null,3]')
    print('Exception :')
    print('[1,3]')
    print('Output :')
    print(str(Solution().rightSideView(listToTreeNode([1, None, 3]))))
    print()

    print('Example 3:')
    print('Input : ')
    print('root = []')
    print('Exception :')
    print('[]')
    print('Output :')
    print(str(Solution().rightSideView(listToTreeNode([]))))
    print()

    pass
# @lc main=end