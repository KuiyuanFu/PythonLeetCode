# @lc app=leetcode id=841 lang=python3
#
# [841] Keys and Rooms
#
# https://leetcode.com/problems/keys-and-rooms/description/
#
# algorithms
# Medium (68.47%)
# Likes:    2823
# Dislikes: 165
# Total Accepted:    181.4K
# Total Submissions: 264.5K
# Testcase Example:  '[[1],[2],[3],[]]'
#
# There are n rooms labeled from 0 to n - 1 and all the rooms are locked except
# for room 0. Your goal is to visit all the rooms. However, you cannot enter a
# locked room without having its key.
#
# When you visit a room, you may find a set of distinct keys in it. Each key
# has a number on it, denoting which room it unlocks, and you can take all of
# them with you to unlock the other rooms.
#
# Given an array rooms where rooms[i] is the set of keys that you can obtain if
# you visited room i, return true if you can visit all the rooms, or false
# otherwise.
#
#
# Example 1:
#
#
# Input: rooms = [[1],[2],[3],[]]
# Output: true
# Explanation:
# We visit room 0 and pick up key 1.
# We then visit room 1 and pick up key 2.
# We then visit room 2 and pick up key 3.
# We then visit room 3.
# Since we were able to visit every room, we return true.
#
#
# Example 2:
#
#
# Input: rooms = [[1,3],[3,0,1],[2],[0]]
# Output: false
# Explanation: We can not enter room number 2 since the only key that unlocks
# it is in that room.
#
#
#
# Constraints:
#
#
# n == rooms.length
# 2 <= n <= 1000
# 0 <= rooms[i].length <= 1000
# 1 <= sum(rooms[i].length) <= 3000
# 0 <= rooms[i][j] < n
# All the values of rooms[i] are unique.
#
#
#

# @lc tags=Unknown

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 拿钥匙。
# 遍历。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:

        visited = set()
        keys = [0]
        while keys:
            k = keys.pop()
            if k in visited:
                continue
            visited.add(k)
            for k in rooms[k]:
                keys.append(k)
        return len(visited) == len(rooms)
        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('rooms = [[1],[2],[3],[]]')
    print('Exception :')
    print('true')
    print('Output :')
    print(str(Solution().canVisitAllRooms([[1], [2], [3], []])))
    print()

    print('Example 2:')
    print('Input : ')
    print('rooms = [[1,3],[3,0,1],[2],[0]]')
    print('Exception :')
    print('false')
    print('Output :')
    print(str(Solution().canVisitAllRooms([[1, 3], [3, 0, 1], [2], [0]])))
    print()

    pass
# @lc main=end