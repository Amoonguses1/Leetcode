/*
This is an answer for
https://leetcode.com/problems/binary-tree-preorder-traversal/

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

// Returns the preorder traversal of its nodes' values.
func preorderTraversal(root *TreeNode) []int {
	if root == nil {
		return []int{}
	}

	res := []int{root.Val}
	res = append(res, preorderTraversal(root.Left)...)
	res = append(res, preorderTraversal(root.Right)...)
	return res
}
