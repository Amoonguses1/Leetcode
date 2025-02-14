/*
This is an answer for
https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/

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

// distanceK returns the array of the values of all nodes
// that have a distance k from the target node.
func distanceK(root *TreeNode, target *TreeNode, k int) []int {
	parentMap := map[*TreeNode]*TreeNode{}
	constructParentsMap(root, nil, parentMap)
	return getKDistVal(target, k, map[*TreeNode]bool{}, parentMap)
}

// constructParentsMap creates a map which tells parent node.
func constructParentsMap(node, parent *TreeNode, parentMap map[*TreeNode]*TreeNode) {
	if node == nil {
		return
	}

	parentMap[node] = parent
	constructParentsMap(node.Left, node, parentMap)
	constructParentsMap(node.Right, node, parentMap)
}

// getKDistVal recursively finds all nodes at distance k from the given node.
func getKDistVal(node *TreeNode, k int, visited map[*TreeNode]bool, parentMap map[*TreeNode]*TreeNode) []int {
	if node == nil || visited[node] {
		return []int{}
	}

	visited[node] = true
	if k == 0 {
		return []int{node.Val}
	}

	res := []int{}
	res = append(res, getKDistVal(node.Left, k-1, visited, parentMap)...)
	res = append(res, getKDistVal(node.Right, k-1, visited, parentMap)...)
	res = append(res, getKDistVal(parentMap[node], k-1, visited, parentMap)...)

	return res
}
