# @lc app=leetcode id=729 lang=python3
#
# [729] My Calendar I
#
# https://leetcode.com/problems/my-calendar-i/description/
#
# algorithms
# Medium (54.39%)
# Likes:    1642
# Dislikes: 54
# Total Accepted:    130.7K
# Total Submissions: 239.1K
# Testcase Example:  '["MyCalendar","book","book","book"]\n[[],[10,20],[15,25],[20,30]]'
#
# You are implementing a program to use as your calendar. We can add a new
# event if adding the event will not cause a double booking.
#
# A double booking happens when two events have some non-empty intersection
# (i.e., some moment is common to both events.).
#
# The event can be represented as a pair of integers start and end that
# represents a booking on the half-open interval [start, end), the range of
# real numbers x such that start <= x < end.
#
# Implement the MyCalendar class:
#
#
# MyCalendar() Initializes the calendar object.
# boolean book(int start, int end) Returns true if the event can be added to
# the calendar successfully without causing a double booking. Otherwise, return
# false and do not add the event to the calendar.
#
#
#
# Example 1:
#
#
# Input
# ["MyCalendar", "book", "book", "book"]
# [[], [10, 20], [15, 25], [20, 30]]
# Output
# [null, true, false, true]
#
# Explanation
# MyCalendar myCalendar = new MyCalendar();
# myCalendar.book(10, 20); // return True
# myCalendar.book(15, 25); // return False, It can not be booked because time
# 15 is already booked by another event.
# myCalendar.book(20, 30); // return True, The event can be booked, as the
# first event takes every time less than 20, but not including 20.
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

# @lc tags=array

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 日历，插入时间。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class MyCalendar:
    def __init__(self):
        self.b = [[0, 0]]

    def book(self, start: int, end: int) -> bool:

        idx = bisect_right(self.b, [start + 1, 0]) - 1

        if self.b[idx][1] > start or \
             (idx + 1 < len(self.b) and self.b[idx + 1][0] < end):
            return False
        self.b.insert(idx + 1, [start, end])
        return True


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('')
    print('Exception :')
    print('')
    print('Output :')
    print(str(Solution().__init__()))
    print()

    pass
# @lc main=end