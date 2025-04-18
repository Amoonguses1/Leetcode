/*
This is an answer for
https://leetcode.com/problems/binary-tree-postorder-traversal/description/

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

// Returns the postorder traversal of its nodes' values.
func postorderTraversal(root *TreeNode) []int {
	if root == nil {
		return []int{}
	}

	res := postorderTraversal(root.Left)
	res = append(res, postorderTraversal(root.Right)...)
	res = append(res, root.Val)
	return res
}
