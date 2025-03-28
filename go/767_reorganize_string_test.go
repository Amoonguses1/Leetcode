package main

import (
	"testing"
)

// TestReorganizeString tests the CountArrangement function
// with multiple binary tree structures.
func TestReorganizeString(t *testing.T) {
	// Define test cases
	tests := []struct {
		name     string
		input    string
		expected string
		hasError bool
	}{
		{
			name:     "normal case",
			input:    "asdfg",
			expected: "agfds",
			hasError: false,
		},
		{
			name:     "no valid rearrangement case",
			input:    "aaa",
			expected: "",
			hasError: false,
		},
		{
			name:     "invalid input case",
			input:    "1sdf",
			expected: "",
			hasError: true,
		},
	}

	// Run test cases
	for _, test := range tests {
		test := test
		t.Run(test.name, func(t *testing.T) {
			res, err := RearrangeDistinctAdjacent(test.input)

			// check if the err is the same as the expected.
			if (err != nil) != test.hasError {
				if test.hasError {
					t.Errorf("%s: expected an error but got none", test.name)
				} else {
					t.Errorf("%s: unexpected error: %v", test.name, err)
				}
			}

			// check if the result is the same as the expected.
			if res != test.expected {
				t.Errorf("%s: wrong answer returned. answer should be %s, but got %s", test.name, test.expected, res)
			}
		})
	}
}
