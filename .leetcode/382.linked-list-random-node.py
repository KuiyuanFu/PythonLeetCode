# @lc app=leetcode id=382 lang=python3
#
# [382] Linked List Random Node
#
# https://leetcode.com/problems/linked-list-random-node/description/
#
# algorithms
# Medium (54.76%)
# Likes:    978
# Dislikes: 251
# Total Accepted:    109.5K
# Total Submissions: 199.6K
# Testcase Example:  '["Solution","getRandom","getRandom","getRandom","getRandom","getRandom"]\n' +
#   '[[[1,2,3]],[],[],[],[],[]]'
#
# Given a singly linked list, return a random node's value from the linked
# list. Each node must have the same probability of being chosen.
#
# Implement the Solution class:
#
#
# Solution(ListNode head) Initializes the object with the integer array
# nums.
# int getRandom() Chooses a node randomly from the list and returns its value.
# All the nodes of the list should be equally likely to be choosen.
#
#
#
# Example 1:
#
#
# Input
# ["Solution", "getRandom", "getRandom", "getRandom", "getRandom", "getRandom"]
# [[[1, 2, 3]], [], [], [], [], []]
# Output
# [null, 1, 3, 2, 2, 3]
#
# Explanation
# Solution solution = new Solution([1, 2, 3]);
# solution.getRandom(); // return 1
# solution.getRandom(); // return 3
# solution.getRandom(); // return 2
# solution.getRandom(); // return 2
# solution.getRandom(); // return 3
# // getRandom() should return either 1, 2, or 3 randomly. Each element should
# have equal probability of returning.
#
#
#
# Constraints:
#
#
# The number of nodes in the linked list will be in the range [1, 10^4].
# -10^4 <= Node.val <= 10^4
# At most 10^4 calls will be made to getRandom.
#
#
#
# Follow up:
#
#
# What if the linked list is extremely large and its length is unknown to
# you?
# Could you solve this efficiently without using extra space?
#
#
#

# @lc tags=reservoir-sampling

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 给定链表，返回随机元素。
# 在n个元素中，选择k个，那么可以直接先取前k个放在蓄水池中，之后每个元素取到的概率为k/i。
#
# @lc idea=end

# @lc group=reservoir-sampling

# @lc rank=10


# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def __init__(self, head: Optional[ListNode]):
        self.head = head
        p = head
        n = 0
        while p:
            p = p.next
        self.n = n

    def getRandom(self) -> int:
        r = self.head.val
        i = 2
        p = self.head.next
        while p:
            if random.random() < (1 / i):
                r = p.val
            p = p.next
            i += 1
        return r


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('')
    print('Exception :')
    print('')
    print('Output :')
    print(str(Solution().__init__(error)))
    print()

    pass
# @lc main=end