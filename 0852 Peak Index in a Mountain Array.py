'''
URL: https://leetcode.com/problems/peak-index-in-a-mountain-array/

Difficulty: Easy

Description: Peak Index in a Mountain Array

Let's call an array A a mountain if the following properties hold:

A.length >= 3
There exists some 0 < i < A.length - 1 such that A[0] < A[1] < ... A[i-1] < A[i] > A[i+1] > ... > A[A.length - 1]
Given an array that is definitely a mountain, return any i such that A[0] < A[1] < ... A[i-1] < A[i] > A[i+1] > ... > A[A.length - 1].

Example 1:

Input: [0,1,0]
Output: 1
Example 2:

Input: [0,2,1,0]
Output: 1
Note:

3 <= A.length <= 10000
0 <= A[i] <= 10^6
A is a mountain, as defined above.

'''


class Solution:
    def peakIndexInMountainArray(self, A):
        start, end = 0, len(A)-1

        while start < end:
            mid = (start+end)//2
            if A[mid] > A[mid-1] and A[mid] > A[mid+1]:
                return mid
            elif A[mid] < A[mid-1]:
                end = mid-1
            elif A[mid] < A[mid+1]:
                start = mid+1
        return start

        '''
        Other Solution 1
        return A.index(max(A))
    
        Other Solution 2
        for i in range(len(A)-1):
            if A[i] > A[i+1]:
                return i
        '''
