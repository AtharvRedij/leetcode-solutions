'''
URL: https://leetcode.com/problems/to-lower-case/

Difficulty: Easy

Description: To Lower Case

Implement function ToLowerCase() that has a string parameter str, and returns the same string in lowercase.

Example 1:

Input: "Hello"
Output: "hello"
Example 2:

Input: "here"
Output: "here"
Example 3:

Input: "LOVELY"
Output: "lovely"

'''


class Solution:
    def toLowerCase(self, str):
        output = ""

        for ch in str:
            ascii_val = ord(ch)
            if 65 <= ascii_val <= 90:
                output += chr(ascii_val + 32)
            else:
                output += ch

        return output
