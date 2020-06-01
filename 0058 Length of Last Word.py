'''
URL: https://leetcode.com/problems/length-of-last-word/

Difficulty: Easy

Description: Length of Last Word

Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word (last word means the last appearing word if we loop from left to right) in the string.

If the last word does not exist, return 0.

Note: A word is defined as a maximal substring consisting of non-space characters only.

Example:

Input: "Hello World"
Output: 5

'''


class Solution:
    def lengthOfLastWord(self, s):
        s = s.strip()
        if len(s) > 0:
            return len(s.split(" ")[-1])
        else:
            return 0
