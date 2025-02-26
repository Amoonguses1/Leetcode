package main

import "testing"

// TestBuddyStrings tests the ShortestCompletingWord function
// with some cases.
func TestBuddyStrings(t *testing.T) {
	// Define test cases
	tests := []struct {
		name     string
		s        string
		goal     string
		expected bool
	}{
		{
			name:     "two strings are buddy strings",
			s:        "ab",
			goal:     "ba",
			expected: true,
		},
		{
			name:     "two strings are not buddy strings",
			s:        "abd",
			goal:     "abc",
			expected: false,
		},
		{
			name:     "the given s is equal to goal and return false",
			s:        "ab",
			goal:     "ab",
			expected: false,
		},
		{
			name:     "the given s is equal to goal and return true",
			s:        "aa",
			goal:     "aa",
			expected: true,
		},
	}

	// Run test cases
	for _, test := range tests {
		test := test
		t.Run(test.name, func(t *testing.T) {
			res := BuddyStrings(test.s, test.goal)
			if res != test.expected {
				t.Errorf("%s: wrong answer returned. answer should be %t, but got %t", test.name, test.expected, res)
			}
		})
	}
}
