'''
URL: https://leetcode.com/problems/di-string-match/

Difficulty: Easy

Description: DI String Match

Given a string S that only contains "I" (increase) or "D" (decrease), let N = S.length.

Return any permutation A of [0, 1, ..., N] such that for all i = 0, ..., N-1:

If S[i] == "I", then A[i] < A[i+1]
If S[i] == "D", then A[i] > A[i+1]
 

Example 1:

Input: "IDID"
Output: [0,4,1,3,2]
Example 2:

Input: "III"
Output: [0,1,2,3]
Example 3:

Input: "DDI"
Output: [3,2,0,1]
 

Note:

1 <= S.length <= 10000
S only contains characters "I" or "D".

'''


class Solution:
    def diStringMatch(self, S):
        output = []
        lower_limit = 0
        upper_limit = len(S)

        for ch in S:
            if ch == "I":
                output.append(lower_limit)
                lower_limit += 1
            elif ch == "D":
                output.append(upper_limit)
                upper_limit -= 1

        output.append(upper_limit)

        return output
