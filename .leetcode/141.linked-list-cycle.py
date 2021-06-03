# @lc app=leetcode id=141 lang=python3
#
# [141] Linked List Cycle
#
# https://leetcode.com/problems/linked-list-cycle/description/
#
# algorithms
# Easy (43.35%)
# Likes:    4640
# Dislikes: 624
# Total Accepted:    934K
# Total Submissions: 2.2M
# Testcase Example:  '[3,2,0,-4]\n1'
#
# Given head, the head of a linked list, determine if the linked list has a
# cycle in it.
#
# There is a cycle in a linked list if there is some node in the list that can
# be reached again by continuously following the next pointer. Internally, pos
# is used to denote the index of the node that tail's next pointer is connected
# to. Note that pos is not passed as a parameter.
#
# Return true if there is a cycle in the linked list. Otherwise, return
# false.
#
#
# Example 1:
#
#
# Input: head = [3,2,0,-4], pos = 1
# Output: true
# Explanation: There is a cycle in the linked list, where the tail connects to
# the 1st node (0-indexed).
#
#
# Example 2:
#
#
# Input: head = [1,2], pos = 0
# Output: true
# Explanation: There is a cycle in the linked list, where the tail connects to
# the 0th node.
#
#
# Example 3:
#
#
# Input: head = [1], pos = -1
# Output: false
# Explanation: There is no cycle in the linked list.
#
#
#
# Constraints:
#
#
# The number of the nodes in the list is in the range [0, 10^4].
# -10^5 <= Node.val <= 10^5
# pos is -1 or a valid index in the linked-list.
#
#
#
# Follow up: Can you solve it using O(1) (i.e. constant) memory?
#
#

# @lc tags=linked-list;two-pointers

# @lc imports=start
from imports import *
# @lc imports=end

# @lc idea=start
#
# 给定一个链表，判断这个链表是否有环。
# 使用快慢指针，如果快指针能追上慢指针，就说明有环。
# 之后确定位置，当相遇时，p为环的第一个结点，设c为环的结点个数，当slow进入到环中，fast一定已经在环中了，设此时fast在环中的位置为t，那么在环中相遇的位置为c-t，因为fast比slow快1，所以此时fast比slow慢c-t，经过c-t次移动，就会相遇。
# slow：s=p+ c-t
# fast：2s = p + c-t + c * n1
# 那么怎么找到p呢。
# 将1式乘2得 2s=2p + 2c-2t
# 减2式得 p = -(c-t) + c * n1
# 可见，当fast从相遇位置移动p次时，会恰移动到环中第一个结点。
# 设slow为0，之后同步移动，相遇结点为目标结点。
#
# @lc idea=end

# @lc group=linked-list;two-pointers

# @lc rank=10

# @lc code=start


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        slow = head
        fast = head
        while True:
            if fast and fast.next:
                fast = fast.next.next
            else:
                return None
            slow = slow.next
            if slow == fast:
                break
        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next
        return slow
        return False


# @lc code=end

# @lc main=start
if __name__ == '__main__':

    pass
# @lc main=end