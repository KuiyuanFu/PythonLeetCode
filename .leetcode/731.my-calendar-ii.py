# @lc app=leetcode id=731 lang=python3
#
# [731] My Calendar II
#
# https://leetcode.com/problems/my-calendar-ii/description/
#
# algorithms
# Medium (52.05%)
# Likes:    991
# Dislikes: 114
# Total Accepted:    64.8K
# Total Submissions: 123.6K
# Testcase Example:  '["MyCalendarTwo","book","book","book","book","book","book"]\n' +
# '[[],[10,20],[50,60],[10,40],[5,15],[5,10],[25,55]]'
#
# You are implementing a program to use as your calendar. We can add a new
# event if adding the event will not cause a triple booking.
#
# A triple booking happens when three events have some non-empty intersection
# (i.e., some moment is common to all the three events.).
#
# The event can be represented as a pair of integers start and end that
# represents a booking on the half-open interval [start, end), the range of
# real numbers x such that start <= x < end.
#
# Implement the MyCalendarTwo class:
#
#
# MyCalendarTwo() Initializes the calendar object.
# boolean book(int start, int end) Returns true if the event can be added to
# the calendar successfully without causing a triple booking. Otherwise, return
# false and do not add the event to the calendar.
#
#
#
# Example 1:
#
#
# Input
# ["MyCalendarTwo", "book", "book", "book", "book", "book", "book"]
# [[], [10, 20], [50, 60], [10, 40], [5, 15], [5, 10], [25, 55]]
# Output
# [null, true, true, true, false, true, true]
#
# Explanation
# MyCalendarTwo myCalendarTwo = new MyCalendarTwo();
# myCalendarTwo.book(10, 20); // return True, The event can be booked.
# myCalendarTwo.book(50, 60); // return True, The event can be booked.
# myCalendarTwo.book(10, 40); // return True, The event can be double booked.
# myCalendarTwo.book(5, 15);  // return False, The event ca not be booked,
# because it would result in a triple booking.
# myCalendarTwo.book(5, 10); // return True, The event can be booked, as it
# does not use time 10 which is already double booked.
# myCalendarTwo.book(25, 55); // return True, The event can be booked, as the
# time in [25, 40) will be double booked with the third event, the time [40,
# 50) will be single booked, and the time [50, 55) will be double booked with
# the second event.
#
#
#
# Constraints:
#
#
# 0 <= start < end <= 10^9
# At most 1000 calls will be made to book.
#
#
#

# @lc tags=ordered-map

# @lc imports=start
from os import stat
from imports import *
# @lc imports=end

# @lc idea=start
#
# 每个时间段最多使用两次。
#
# @lc idea=end

# @lc group=

# @lc rank=

# @lc code=start


class MyCalendarTwo:
    def __init__(self):
        self.b = [[-1, -1, 0]]

    def book(self, start: int, end: int) -> bool:
        idxL = bisect_right(self.b, [start + 1, 0, 0]) - 1
        idxR = bisect_right(self.b, [end, 0, 0])

        def check():
            for idx in range(idxL, idxR):
                l, r, t = self.b[idx]
                if t == 2 and not (l >= end or r <= start):
                    return False

            return True

        if not check():
            return False

        def add():
            startC, endC = start, end
            res = self.b[:idxL]
            for idx in range(idxL, idxR):
                l, r, _ = self.b[idx]
                if r <= startC:
                    res.append(self.b[idx])
                elif l >= endC:
                    res.append([startC, endC, 1])
                    startC = endC
                    res.append(self.b[idx])
                    break
                else:
                    n1, n2, startC, endC = min(l, startC), max(l, startC), min(
                        r, endC), max(r, endC)
                    if n1 != n2:
                        res.append([n1, n2, 1])
                    if n2 != startC:
                        res.append([n2, startC, 2])

            if startC != endC:
                res.append([startC, endC, 1])

            res += self.b[idxR:]
            return res

        self.b = add()
        return True


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    o = MyCalendarTwo()
    print(o.book(10, 20))
    print(o.book(50, 60))
    print(o.book(10, 40))
    print(o.book(5, 15))
    print(o.book(5, 10))
    print(o.book(25, 55))

    pass
# @lc main=end