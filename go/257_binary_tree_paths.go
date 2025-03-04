/*
This is an answer for
https://leetcode.com/problems/binary-tree-paths/

Time: O(NlogN)
Space: O(NlogN)
N is the number of nodes
*/
package main

import (
	"bytes"
	"strconv"
)

/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

func binaryTreePaths(root *TreeNode) []string {
	var buf bytes.Buffer
	var res []string
	getPaths(root, &buf, true, &res)
	return res
}

func getPaths(node *TreeNode, buf *bytes.Buffer, isRoot bool, res *[]string) {
	if node == nil {
		return
	}

	curLen := buf.Len()

	if !isRoot {
		buf.WriteString("->")
	}
	buf.WriteString(strconv.Itoa(node.Val))

	if node.Left == nil && node.Right == nil {
		*res = append(*res, buf.String())
	} else {
		getPaths(node.Left, buf, false, res)
		getPaths(node.Right, buf, false, res)
	}

	buf.Truncate(curLen)
}
