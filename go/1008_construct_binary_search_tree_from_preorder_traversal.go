/*
This is an answer for
https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal/description/

Time: O(N^2)
Space: O(N^2)
N = len(preorder)
*/
package main

// Definition for a binary tree node.
type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

// bisect finds the first index 'idx' where preorder[idx] >= target.
func bisect(preorder []int, target int) int {
	left, right := 0, len(preorder)

	for (right - left) > 1 {
		mid := (right + left) / 2
		if preorder[mid] < target {
			left = mid
		} else {
			right = mid
		}
	}

	return right
}

// bstFromPreorder constructs Binary Search Tree (BST) from the given preorder array.
// The input 'preorder' represents the preorder traversal of a BST.
// It returns the root of the constructed BST.
func bstFromPreorder(preorder []int) *TreeNode {
	// Base case: Return nil if there are no elements in the preorder.
	if len(preorder) == 0 {
		return nil
	}

	// Create the root node with the first element.
	root := &TreeNode{preorder[0], nil, nil}

	// Find the index where right subtree starts.
	idx := bisect(preorder, preorder[0])

	// Recursively construct left and right subtrees.
	if idx != 0 {
		root.Left = bstFromPreorder(preorder[1:idx])
	}
	root.Right = bstFromPreorder(preorder[idx:])

	return root
}
