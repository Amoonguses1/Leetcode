/*
This is an answer for
https://leetcode.com/problems/binary-tree-tilt/ .

Time: O(N)
Space: O(H)
N is the number of the TreeNodes
H is the depth of the TreeNodes
*/
package main

// Definition for a binary tree node.
// type TreeNode struct {
// 	Val   int
// 	Left  *TreeNode
// 	Right *TreeNode
// }

// FindTilt calculates the total tilt of a binary tree.
// The tilt of a node is defined as the absolute difference
// between the sum of all left subtree node values
// and all right subtree node values.
func FindTilt(root *TreeNode) int {
	_, tilt := computeSubtreeStats(root)
	return tilt
}

// intAbs returns the absolute value of the given integer.
func intAbs(n int) int {
	if n < 0 {
		return -n
	}

	return n
}

// computeSubtreeStats recursively calculates the sum of node values in a subtree
// and the total tilt for that subtree.
// It returns two values.
// 1. The sum of node values in a subtree.
// 2. the total tilt for that subtree.
func computeSubtreeStats(root *TreeNode) (int, int) {
	// Base case: if root is nil, return 0, 0
	if root == nil {
		return 0, 0
	}

	// Recursively compute the sum and tilt for the left nad right subtrees
	leftSum, leftTilt := computeSubtreeStats(root.Left)
	rightSum, rightTilt := computeSubtreeStats(root.Right)

	// Calculate the tilt of the current node.
	tilt := intAbs(leftSum - rightSum)

	return root.Val + leftSum + rightSum, tilt + leftTilt + rightTilt
}
