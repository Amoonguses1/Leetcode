package main

import "testing"

// TestIsIsomorphic tests the CountArrangement function
// with multiple binary tree structures.
func TestIsIsomorphic(t *testing.T) {
	// Define test cases
	tests := []struct {
		name     string
		source   string
		target   string
		expected bool
	}{
		{
			name:     "isomorphic case",
			source:   "abc",
			target:   "cba",
			expected: true,
		},
		{
			name:     "length are not equal",
			source:   "a",
			target:   "aa",
			expected: false,
		},
		{
			name:     "source can not mapping one character",
			source:   "foo",
			target:   "bar",
			expected: false,
		},
		{
			name:     "target can not mapping one character",
			source:   "bar",
			target:   "foo",
			expected: false,
		},
	}

	// Run test cases
	for _, test := range tests {
		test := test
		t.Run(test.name, func(t *testing.T) {
			res := isIsomorphic(test.source, test.target)
			if res != test.expected {
				t.Errorf("%s: wrong answer returned. answer should be %v, but got %v", test.name, test.expected, res)
			}
		})
	}
}
