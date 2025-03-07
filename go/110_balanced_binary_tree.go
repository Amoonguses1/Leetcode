/*
This is an answer for
https://leetcode.com/problems/balanced-binary-tree/description/

Time: O(N)
Space: O(N)
N is the number of nodes
*/
package main

/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

// Difinition for a binary tree status for determining
// if the tree is balanced.
type treeStats struct {
	depth      int
	isBalanced bool
}

// Returns if the given binary tree is height-balanced.
// A height-balanced binary tree is a binary tree
// in which the depth of the two subtrees of every node
// never differs by more than one.
func IsBalanced(root *TreeNode) bool {
	rootStats := calcTreeStats(root)
	return rootStats.isBalanced
}

// calcTreeStats returns both the height of the tree
// and whether it is balanced.
func calcTreeStats(root *TreeNode) treeStats {
	if root == nil {
		return treeStats{0, true}
	}

	leftStats := calcTreeStats(root.Left)
	rightStats := calcTreeStats(root.Right)

	if !leftStats.isBalanced || !rightStats.isBalanced {
		return treeStats{-1, false}
	}

	if abs(leftStats.depth-rightStats.depth) > 1 {
		return treeStats{-1, false}
	}

	return treeStats{max(leftStats.depth, rightStats.depth) + 1, true}
}

// Returns absolute value of type int.
func abs(x int) int {
	if x < 0 {
		return -x
	}
	return x
}
