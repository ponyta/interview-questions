#!/usr/bin/python3

# Given an array of integers, return the largest range, inclusive, of integers that are all included in the array.
# For example, given the array [9, 6, 1, 3, 8, 10, 12, 11], return (8, 12) since 8, 9, 10, 11, and 12 are all in the array.

# I assume the "largest range" means the range where M-N is maximized, and all numbers N, N+1, N+2, ..., M-1, M are included in the array.

# First, the easiest way to do this is to simply sort the array. Then we can go through the sorted array in linear time and count the
# lengths of continuous ranges. This would give us O(nlogn + n) time which is overall O(nlogn).

# So we are probably looking for a O(n) time solution. I assume we can't limit the range of numbers we get (i.e. we can be given any possible integers).
# - If the array is size N the largest possible range is also of size N.

# Given the example: say we start with 9. Then I know if I find a 8 or 10 the max possible range is 2.
# let found = {9}
# let looking_for = {8: 2, 10: 2}

# next iter: we find 7.
# found = {9, 6}
# looking_for = {6:2, 8:3, 10:2 }

def largest_range(arr: list[int]) -> tuple(int, int):
    found = {}
    looking_for = {}
    # O(n) time
    for i in arr:
        found[i] = True
        if looking_for[i-1]:
            looking_for[i-1] += 1
        else:
            looking_for[i-1] = 2


