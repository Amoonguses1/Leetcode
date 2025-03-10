/*
This is an answer for
https://leetcode.com/problems/smallest-string-starting-from-leaf/description/

Time: O(N)
Space: O(logN)
N is the number of nodes
*/
package main

// Returns the lexicographically smallest string
// that starts at a leaf of this tree and ends at the root.
//
// TreeNode value is in the range[0, 25] representing the letters 'a' to 'z'
func smallestFromLeaf(root *TreeNode) string {
	var result string
	var currentPath []byte

	searchSmallestString(root, &currentPath, &result)

	return result
}

// performs a backtracking search to find the smallest string.
func searchSmallestString(node *TreeNode, currentPath *[]byte, result *string) {
	if node == nil {
		return
	}

	*currentPath = append(*currentPath, byte('a'+node.Val))

	if isLeaf(node) {
		pathStr := string(reverse(*currentPath))
		if isLessThan(pathStr, *result) {
			*result = pathStr
		}
	}

	searchSmallestString(node.Left, currentPath, result)
	searchSmallestString(node.Right, currentPath, result)

	*currentPath = (*currentPath)[:len(*currentPath)-1]
}

// checks if the lhs is less than the rhs or not.
func isLessThan(lhs, rhs string) bool {
	return lhs < rhs || rhs == ""
}

// checks if the given node is a leaf node.
func isLeaf(node *TreeNode) bool {
	return node.Left == nil && node.Right == nil
}

// reverses the given slice.
func reverse(bytesSlice []byte) []byte {
	reversed := make([]byte, len(bytesSlice))
	for i, j := 0, len(bytesSlice)-1; i <= j; i, j = i+1, j-1 {
		reversed[i], reversed[j] = bytesSlice[j], bytesSlice[i]
	}
	return reversed
}
