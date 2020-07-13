'''
URL: https://leetcode.com/problems/reverse-words-in-a-string-iii/

Difficulty: Easy

Description: Reverse Words in a String III

Given a string, you need to reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

Example 1:
Input: "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"
Note: In the string, each word is separated by single space and there will not be any extra space in the string.

'''


class Solution:
    def reverseWords(self, s):
        output = ""

        for word in s.split(" "):
            output += word[::-1] + " "

        return output[:-1]
