'''
URL: https://leetcode.com/problems/shortest-distance-to-a-character/

Difficulty: Easy

Description: Shortest Distance to a Character

Given a string S and a character C, return an array of integers representing the shortest distance from the character C in the string.

Example 1:

Input: S = "loveleetcode", C = 'e'
Output: [3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0]
 

Note:

S string length is in [1, 10000].
C is a single character, and guaranteed to be in string S.
All letters in S and C are lowercase.

'''


class Solution:
    def shortestToChar(self, S, C):
        result = []

        # find all indexes of target char
        C_indexes = [i for i, ch in enumerate(S) if ch == C]

        for i in range(len(S)):

            # check which index of target char from C_indexes is nearest to current char index
            nearest = min(
                C_indexes, key=lambda list_value: abs(list_value - i))

            result.append(abs(nearest - i))

        return result

        '''
        OTHER APPROCH: keep two pointers from current index move left and right
        if any of those to index hold target char then append nearest of two
        
        
        result = []
        
        for starting_index, ch in enumerate(S):
            left = right = starting_index
            
            while left > -1 and right < len(S):
                if S[left] == C or S[right] == C:
                    result.append(max(abs(starting_index - left), abs(starting_index - right)))
                    break
                else:
                    if left > 0:
                        left -= 1
                    if right < len(S) - 1:
                        right += 1
        
        return result
        '''
