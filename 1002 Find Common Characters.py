'''
URL: https://leetcode.com/problems/find-common-characters/

Difficulty: Easy

Description: Find Common Characters

Given an array A of strings made only from lowercase letters, return a list of all characters that show up in all strings within the list (including duplicates).  For example, if a character occurs 3 times in all strings but not 4 times, you need to include that character three times in the final answer.

You may return the answer in any order.

 

Example 1:

Input: ["bella","label","roller"]
Output: ["e","l","l"]
Example 2:

Input: ["cool","lock","cook"]
Output: ["c","o"]
 

Note:

1 <= A.length <= 100
1 <= A[i].length <= 100
A[i][j] is a lowercase letter

'''


class Solution:
    def commonChars(self, A):
        # array stores count of each char in each string at respective index
        counts = []

        for i, string in enumerate(A):
            # holds occurrence count of each char
            cts = {}
            for ch in set(string):
                cts[ch] = string.count(ch)

            counts.append(cts)

        # we will check against set of all chars in first string in A
        first_string_chars = set(A[0])
        result = []

        for ch in first_string_chars:
            ch_counts = []
            flag = 0

            for cts in counts:
                # if char not in in any of the subsequent char count dict break and set flag
                if ch not in cts:
                    flag = 1
                    break

                ch_counts.append(cts[ch])

            if flag == 0:
                result += [ch] * min(ch_counts)

        return result
