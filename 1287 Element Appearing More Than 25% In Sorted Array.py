'''
URL: https://leetcode.com/problems/element-appearing-more-than-25-in-sorted-array/

Difficulty: Easy

Description: Element Appearing More Than 25% In Sorted Array

Given an integer array sorted in non-decreasing order, there is exactly one integer in the array that occurs more than 25% of the time.

Return that integer.

 

Example 1:

Input: arr = [1,2,2,6,6,6,6,7,10]
Output: 6
 

Constraints:

1 <= arr.length <= 10^4
0 <= arr[i] <= 10^5

'''


class Solution:
    def findSpecialInteger(self, arr):
        expected_occurrence_count = int(len(arr) * 0.25)

        counts = {}

        for n in arr:
            if n in counts:
                if counts[n] > expected_occurrence_count:
                    return n
                else:
                    counts[n] += 1
            else:
                counts[n] = 1

        return max(counts, key=lambda x: counts[x])
