# @lc app=leetcode id=732 lang=python3
#
# [732] My Calendar III
#
# https://leetcode.com/problems/my-calendar-iii/description/
#
# algorithms
# Hard (64.61%)
# Likes:    621
# Dislikes: 136
# Total Accepted:    36K
# Total Submissions: 55K
# Testcase Example:  '["MyCalendarThree","book","book","book","book","book","book"]\n' +
# '[[],[10,20],[50,60],[10,40],[5,15],[5,10],[25,55]]'
#
# A k-booking happens when k events have some non-empty intersection (i.e.,
# there is some time that is common to all k events.)
#
# You are given some events [start, end), after each given event, return an
# integer k representing the maximum k-booking between all the previous
# events.
#
# Implement the MyCalendarThree class:
#
#
# MyCalendarThree() Initializes the object.
# int book(int start, int end) Returns an integer k representing the largest
# integer such that there exists a k-booking in the calendar.
#
#
#
# Example 1:
#
#
# Input
# ["MyCalendarThree", "book", "book", "book", "book", "book", "book"]
# [[], [10, 20], [50, 60], [10, 40], [5, 15], [5, 10], [25, 55]]
# Output
# [null, 1, 1, 2, 3, 3, 3]
#
# Explanation
# MyCalendarThree myCalendarThree = new MyCalendarThree();
# myCalendarThree.book(10, 20); // return 1, The first event can be booked and
# is disjoint, so the maximum k-booking is a 1-booking.
# myCalendarThree.book(50, 60); // return 1, The second event can be booked and
# is disjoint, so the maximum k-booking is a 1-booking.
# myCalendarThree.book(10, 40); // return 2, The third event [10, 40)
# intersects the first event, and the maximum k-booking is a 2-booking.
# myCalendarThree.book(5, 15); // return 3, The remaining events cause the
# maximum K-booking to be only a 3-booking.
# myCalendarThree.book(5, 10); // return 3
# myCalendarThree.book(25, 55); // return 3
#
#
#
# Constraints:
#
#
# 0 <= start < end <= 10^9
# At most 400 calls will be made to book.
#
#
#

# @lc tags=segment-tree;ordered-map

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 每个时间段最多使用次数。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class MyCalendarThree:
    def __init__(self):
        self.b = [[-1, -1, 0]]
        self.res = 1

    def book(self, start: int, end: int) -> bool:
        idxL = bisect_right(self.b, [start + 1, 0, 0]) - 1
        idxR = bisect_right(self.b, [end, 0, 0])

        def add():
            startC, endC = start, end
            res = self.b[:idxL]
            for idx in range(idxL, idxR):
                l, r, t = self.b[idx]
                if r <= startC:
                    res.append(self.b[idx])
                else:

                    n1, n2, n3, n4 = min(l, startC), max(l, startC), min(
                        r, endC), max(r, endC)
                    if n1 != n2:
                        res.append([n1, n2, t if l == n1 else 1])
                    if n2 != n3:
                        res.append([n2, n3, t + 1])
                        self.res = max(self.res, t + 1)
                    if endC == n3:
                        res.append([n3, n4, t])
                        startC = endC
                    else:
                        startC, endC = n3, n4

            if startC != endC:
                res.append([startC, endC, 1])

            res += self.b[idxR:]
            return res

        self.b = add()
        return self.res


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    o = MyCalendarThree()
    print(o.book(10, 20))
    print(o.book(50, 60))
    print(o.book(10, 40))
    print(o.book(5, 15))
    print(o.book(5, 10))
    print(o.book(25, 55))
    print()

    o = MyCalendarThree()
    print(o.book(26, 35))
    print(o.book(26, 32))
    print(o.book(25, 32))
    print(o.book(18, 26))
    print(o.book(40, 45))
    print(o.book(19, 26))
    print(o.book(48, 50))
    print(o.book(1, 6))
    print(o.book(45, 50))
    print(o.book(11, 18))

    pass
# @lc main=end