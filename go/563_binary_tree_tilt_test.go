package main

import "testing"

// TestFindTilt tests the FindTilt function
// with multiple binary tree structures.
func TestFindTilt(t *testing.T) {
	// Initialize large binary tree
	naturalNumbersTree := &TreeNode{
		1,
		&TreeNode{2, nil, nil},
		&TreeNode{5, nil, nil},
	}
	normalBinaryTree := &TreeNode{
		1,
		&TreeNode{-7, &TreeNode{5, nil, nil}, nil},
		&TreeNode{5, naturalNumbersTree, nil},
	}

	// Define test cases
	tests := []struct {
		name     string
		input    *TreeNode
		expected int
	}{
		{
			name:     "given no nodes",
			input:    nil,
			expected: 0,
		},
		{
			name:     "given only one node",
			input:    &TreeNode{1, nil, nil},
			expected: 0,
		},
		{
			name:     "only natural numbers",
			input:    naturalNumbersTree,
			expected: 3,
		},
		{
			name:     "normal binary trees",
			input:    normalBinaryTree,
			expected: 31,
		},
	}

	// Run test cases
	for _, test := range tests {
		test := test
		t.Run(test.name, func(t *testing.T) {
			res := FindTilt(test.input)
			if res != test.expected {
				t.Errorf("%s: wrong answer returned. answer should be %d, but got %d", test.name, test.expected, res)
			}
		})
	}
}
