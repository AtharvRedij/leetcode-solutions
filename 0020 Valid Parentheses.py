'''
URL: https://leetcode.com/problems/valid-parentheses/

Difficulty: Easy

Description: Valid Parentheses

Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:

Input: "()"
Output: true
Example 2:

Input: "()[]{}"
Output: true
Example 3:

Input: "(]"
Output: false
Example 4:

Input: "([)]"
Output: false
Example 5:

Input: "{[]}"
Output: true

'''


class Solution:
    def isValid(self, s):
        stack = []
        top = -1
        bracket_key = {")": "(", "}": "{", "]": "["}

        for br in s:
            if (br == "(" or br == "{" or br == "["):
                stack.append(br)
                top += 1
            else:
                if top == -1:
                    return False
                elif(stack[len(stack)-1] == bracket_key[br]):
                    stack.pop()
                    top -= 1
                else:
                    return False

        return top == -1
