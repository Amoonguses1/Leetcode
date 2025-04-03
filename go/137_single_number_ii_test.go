package main

import "testing"

// TestsingleNumber tests the singleNumber function
// with some cases.
func TestSingleNumber(t *testing.T) {
	// Define test cases
	tests := []struct {
		name     string
		input    []int
		expected int
	}{
		{
			name:     "base case",
			input:    []int{0, 0, 0, 1},
			expected: 1,
		},
		{
			name:     "given only one element slice",
			input:    []int{1},
			expected: 1,
		},
		{
			name:     "the expected answer is negative",
			input:    []int{-1, 1, 1, 1},
			expected: -1,
		},
	}

	// Run test cases
	for _, test := range tests {
		test := test
		t.Run(test.name, func(t *testing.T) {
			res := singleNumber(test.input)
			if res != test.expected {
				t.Errorf("%s: wrong answer returned. answer should be %d, but got %d", test.name, test.expected, res)
			}
		})
	}
}
