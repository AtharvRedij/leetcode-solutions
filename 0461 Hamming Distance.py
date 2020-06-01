'''
URL: https://leetcode.com/problems/hamming-distance/

Difficulty: Easy

Description: Hamming Distance

The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

Given two integers x and y, calculate the Hamming distance.

Note:
0 ≤ x, y < 231.

Example:

Input: x = 1, y = 4

Output: 2

Explanation:
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑

The above arrows point to positions where the corresponding bits are different.

'''


class Solution:
    def decimal_to_binary(self, n):
        output = ""

        while n > 0:
            output += str(n % 2)
            n = n // 2

        return output[::-1]

    def hammingDistance(self, x, y):
        x_binary = self.decimal_to_binary(x)
        y_binary = self.decimal_to_binary(y)

        max_len = max(len(x_binary), len(y_binary))
        x_binary = "0" * (max_len - len(x_binary)) + x_binary
        y_binary = "0" * (max_len - len(y_binary)) + y_binary

        count = 0

        for i in range(max_len):
            if x_binary[i] != y_binary[i]:
                count += 1

        return count
