'''
URL: https://leetcode.com/problems/squares-of-a-sorted-array/

Difficulty: Easy

Description: Squares of a Sorted Array

Given an array of integers A sorted in non-decreasing order, return an array of the squares of each number, also in sorted non-decreasing order.

 

Example 1:

Input: [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Example 2:

Input: [-7,-3,2,3,11]
Output: [4,9,9,49,121]
 

Note:

1 <= A.length <= 10000
-10000 <= A[i] <= 10000
A is sorted in non-decreasing order.

'''


class Solution:
    def sortedSquares(self, A):
        if len(A) == 1:
            return [A[0]**2]

        sq_arr = []
        neg_index = 0
        pos_index = 0

        for i, n in enumerate(A):
            if n >= 0:
                pos_index = i
                neg_index = i-1
                break

        while neg_index >= 0 and pos_index < len(A):
            if abs(A[neg_index]) < A[pos_index]:
                sq_arr.append(A[neg_index]**2)
                neg_index -= 1
            else:
                sq_arr.append(A[pos_index]**2)
                pos_index += 1

        for i in range(neg_index, -1, -1):
            sq_arr.append(A[i]**2)

        for i in range(pos_index, len(A)):
            sq_arr.append(A[i]**2)

        return sq_arr
