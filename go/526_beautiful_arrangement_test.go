package main

import "testing"

// TestCountArrangement tests the CountArrangement function
// with multiple binary tree structures.
func TestCountArrangement(t *testing.T) {
	// Define test cases
	tests := []struct {
		name     string
		input    int
		expected int
	}{
		{
			name:     "base case",
			input:    1,
			expected: 1,
		},
		{
			name:     "large input number",
			input:    15,
			expected: 24679,
		},
	}

	// Run test cases
	for _, test := range tests {
		test := test
		t.Run(test.name, func(t *testing.T) {
			res := CountArrangement(test.input)
			if res != test.expected {
				t.Errorf("%s: wrong answer returned. answer should be %d, but got %d", test.name, test.expected, res)
			}
		})
	}
}
