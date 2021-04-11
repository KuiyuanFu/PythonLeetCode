#
# @lc app=leetcode id=23 lang=python3
#
# [23] Merge k Sorted Lists
#
# https://leetcode.com/problems/merge-k-sorted-lists/description/
#
# algorithms
# Hard (43.00%)
# Likes:    6917
# Dislikes: 349
# Total Accepted:    858.7K
# Total Submissions: 2M
# Testcase Example:  '[[1,4,5],[1,3,4],[2,6]]'
#
# You are given an array of k linked-lists lists, each linked-list is sorted in
# ascending order.
# 
# Merge all the linked-lists into one sorted linked-list and return it.
# 
# 
# Example 1:
# 
# 
# Input: lists = [[1,4,5],[1,3,4],[2,6]]
# Output: [1,1,2,3,4,4,5,6]
# Explanation: The linked-lists are:
# [
# ⁠ 1->4->5,
# ⁠ 1->3->4,
# ⁠ 2->6
# ]
# merging them into one sorted list:
# 1->1->2->3->4->4->5->6
# 
# 
# Example 2:
# 
# 
# Input: lists = []
# Output: []
# 
# 
# Example 3:
# 
# 
# Input: lists = [[]]
# Output: []
# 
# 
# 
# Constraints:
# 
# 
# k == lists.length
# 0 <= k <= 10^4
# 0 <= lists[i].length <= 500
# -10^4 <= lists[i][j] <= 10^4
# lists[i] is sorted in ascending order.
# The sum of lists[i].length won't exceed 10^4.
# 
# 
#
# @lc idea=start
#
# 合并多个有序链表。
# 使用堆，对这n个有序链表的首节点进行排序。
# 小trick ，使用元组来应对不能修改类比较函数时，的比较问题。
#
# @lc idea=end

from typing import *
from collections import *


# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        # 判断空
        if len(lists) == 0:
            return None
        ls = []
        for i,l in enumerate(lists) :
            if l :
                ls.append((l.val,i,l) )
    
        pseudo = ListNode()
        p = pseudo
        # 堆
        import heapq
        heapq.heapify(ls)
        while len(ls) != 0 :
            _,i,p.next = ls[0]
            p = p.next 
            if p.next :
                heapq.heapreplace(ls, (p.next.val,i,p.next))
            else:
                heapq.heappop(ls)
                
        return pseudo.next
        
        
# @lc code=end

