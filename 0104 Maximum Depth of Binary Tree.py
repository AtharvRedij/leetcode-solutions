'''
URL: https://leetcode.com/problems/maximum-depth-of-binary-tree/

Difficulty: Easy

Description: Maximum Depth of Binary Tree

Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its depth = 3.

'''

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root, depth=1):

        r1 = r2 = 0

        if root:
            if root.left == None and root.right == None:
                return depth

            if root.left:
                r1 = self.maxDepth(root.left, depth + 1)

            if root.right:
                r2 = self.maxDepth(root.right, depth + 1)

        return max(r1, r2)
