package main

import "testing"

// TestIsBalanced tests the IsBalanced function
// with some cases.
func TestIsBalanced(t *testing.T) {
	smallTree1 := TreeNode{Val: 0, Left: &TreeNode{Val: 1}, Right: &TreeNode{Val: 2}}
	smallTree2 := TreeNode{Val: 3, Left: &TreeNode{Val: 4}, Right: &TreeNode{Val: 5}}
	balancedTree := TreeNode{Val: 0, Left: &smallTree1, Right: &smallTree2}
	unbalancedTree := TreeNode{Val: 0, Left: &smallTree1}
	// Define test cases
	tests := []struct {
		name     string
		treeNode *TreeNode
		expected bool
	}{
		{
			name:     "given no nodes",
			treeNode: nil,
			expected: true,
		},
		{
			name:     "given balanced binary tree",
			treeNode: &balancedTree,
			expected: true,
		},
		{
			name:     "given unbalanced binary tree",
			treeNode: &unbalancedTree,
			expected: false,
		},
	}

	// Run test cases
	for _, test := range tests {
		test := test
		t.Run(test.name, func(t *testing.T) {
			res := IsBalanced(test.treeNode)
			if res != test.expected {
				t.Errorf("%s: wrong answer returned. answer should be %v, but got %v", test.name, test.expected, res)
			}
		})
	}
}
