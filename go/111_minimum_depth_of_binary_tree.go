/*
This is an answer for
https://leetcode.com/problems/minimum-depth-of-binary-tree/

Time: O(N)
Space: O(N)
N is the number of nodes
*/
package main

// Returns minimum depth.
// The minimum depth is the number of nodes
// along the shortest path from the root node down to the nearest leaf node.
func minDepth(root *TreeNode) int {
	if root == nil {
		return 0
	}

	if root.Left == nil {
		return minDepth(root.Right) + 1
	}

	if root.Right == nil {
		return minDepth(root.Left) + 1
	}

	return min(minDepth(root.Left), minDepth(root.Right)) + 1
}
