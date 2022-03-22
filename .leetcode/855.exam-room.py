# @lc app=leetcode id=855 lang=python3
#
# [855] Exam Room
#
# https://leetcode.com/problems/exam-room/description/
#
# algorithms
# Medium (43.55%)
# Likes:    950
# Dislikes: 371
# Total Accepted:    46K
# Total Submissions: 105.5K
# Testcase Example:  '["ExamRoom","seat","seat","seat","seat","leave","seat"]\n' +
# '[[10],[],[],[],[],[4],[]]'
#
# There is an exam room with n seats in a single row labeled from 0 to n - 1.
#
# When a student enters the room, they must sit in the seat that maximizes the
# distance to the closest person. If there are multiple such seats, they sit in
# the seat with the lowest number. If no one is in the room, then the student
# sits at seat number 0.
#
# Design a class that simulates the mentioned exam room.
#
# Implement the ExamRoom class:
#
#
# ExamRoom(int n) Initializes the object of the exam room with the number of
# the seats n.
# int seat() Returns the label of the seat at which the next student will
# set.
# void leave(int p) Indicates that the student sitting at seat p will leave the
# room. It is guaranteed that there will be a student sitting at seat p.
#
#
#
# Example 1:
#
#
# Input
# ["ExamRoom", "seat", "seat", "seat", "seat", "leave", "seat"]
# [[10], [], [], [], [], [4], []]
# Output
# [null, 0, 9, 4, 2, null, 5]
#
# Explanation
# ExamRoom examRoom = new ExamRoom(10);
# examRoom.seat(); // return 0, no one is in the room, then the student sits at
# seat number 0.
# examRoom.seat(); // return 9, the student sits at the last seat number 9.
# examRoom.seat(); // return 4, the student sits at the last seat number 4.
# examRoom.seat(); // return 2, the student sits at the last seat number 2.
# examRoom.leave(4);
# examRoom.seat(); // return 5, the student sits at the last seat number
# 5.
#
#
#
#
# Constraints:
#
#
# 1 <= n <= 10^9
# It is guaranteed that there is a student sitting at seat p.
# At most 10^4 calls will be made to seat and leave.
#
#
#

# @lc tags=two-pointers

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 座位，每次都距离最远。
#
# @lc idea=end

# @lc group=

# @lc rank=

# @lc code=start
from bisect import *


class ExamRoom:
    def __init__(self, n: int):

        self.n = n
        self.list = []

    def seat(self) -> int:

        if len(self.list) == 0:
            self.list.append(0)
            return 0

        res = max((self.list[0] - 0 - 1, 0),
                  ((self.n - 1) - self.list[-1] - 1, -(self.n - 1)))
        for i in range(len(self.list) - 1):
            l, r = self.list[i], self.list[i + 1]
            dist = r - l - 1
            if dist > 0:
                ld = (dist - 1) // 2
                res = max(res, (ld, -(l + ld + 1)))
        res, idx = res[0], -res[1]
        idxInsert = bisect_left(self.list, idx)
        if idxInsert == len(self.list) or self.list[idxInsert] != idx:
            self.list.insert(idxInsert, idx)
        return idx

    def leave(self, p: int) -> None:
        idx = bisect_left(self.list, p)
        self.list.pop(idx)
        pass


# Your ExamRoom object will be instantiated and called as such:
# obj = ExamRoom(n)
# param_1 = obj.seat()
# obj.leave(p)
# pass
# @lc code=end

# @lc main=start
if __name__ == '__main__':
    e = ExamRoom(10)
    print(e.seat())
    print(e.seat())
    print(e.seat())
    print(e.seat())
    print(e.leave(4))
    print(e.seat())
    print()
    e = ExamRoom(10)
    print(e.seat())
    print(e.seat())
    print(e.seat())
    print(e.seat())
    print(e.leave(0))
    print(e.leave(4))
    print(e.seat())
    print(e.seat())
    print(e.seat())
    print(e.seat())
    print(e.seat())
    print(e.seat())
    print(e.seat())
    print(e.seat())
    print(e.seat())
    pass
# @lc main=end