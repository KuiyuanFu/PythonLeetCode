# @lc app=leetcode id=508 lang=python3
#
# [508] Most Frequent Subtree Sum
#
# https://leetcode.com/problems/most-frequent-subtree-sum/description/
#
# algorithms
# Medium (60.71%)
# Likes:    1104
# Dislikes: 178
# Total Accepted:    93.9K
# Total Submissions: 154.2K
# Testcase Example:  '[5,2,-3]'
#
# Given the root of a binary tree, return the most frequent subtree sum. If
# there is a tie, return all the values with the highest frequency in any
# order.
#
# The subtree sum of a node is defined as the sum of all the node values formed
# by the subtree rooted at that node (including the node itself).
#
#
# Example 1:
#
#
# Input: root = [5,2,-3]
# Output: [2,-3,4]
#
#
# Example 2:
#
#
# Input: root = [5,2,-5]
# Output: [2]
#
#
#
# Constraints:
#
#
# The number of nodes in the tree is in the range [1, 10^4].
# -10^5 <= Node.val <= 10^5
#
#
#

# @lc tags=hash-table;tree

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 频数最高的子树和。
# 递归，字典。
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
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:

        d = defaultdict(int)

        def recur(p: TreeNode):
            if not p:
                return 0
            pl, pr = recur(p.left), recur(p.right)
            s = p.val + pl + pr
            d[s] += 1
            return s

        recur(root)

        res = []
        m = 0
        for k in d.keys():
            t = d[k]
            if t > m:
                m = t
                res.clear()
                res.append(k)
            elif t == m:
                res.append(k)
        return res


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('root = [5,2,-3]')
    print('Exception :')
    print('[2,-3,4]')
    print('Output :')
    print(str(Solution().findFrequentTreeSum(listToTreeNode([5, 2, -3]))))
    print()

    print('Example 2:')
    print('Input : ')
    print('root = [5,2,-5]')
    print('Exception :')
    print('[2]')
    print('Output :')
    print(str(Solution().findFrequentTreeSum(listToTreeNode([5, 2, -5]))))
    print()

    pass
# @lc main=end