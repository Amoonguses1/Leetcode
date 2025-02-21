package main

import "testing"

// TestMostCommonWord tests the MostCommonWord function
// with some cases.
func TestMostCommonWord(t *testing.T) {
	// Define test cases
	tests := []struct {
		name      string
		paragraph string
		banned    []string
		expected  string
	}{
		{
			name:      "the most frequency word",
			paragraph: "Bob hit a ball, the hit BALL flew far after it was hit.",
			banned: []string{
				"bob",
			},
			expected: "hit",
		},
		{
			name:      "the most frequency word is banned",
			paragraph: "Bob hit a ball, the hit BALL flew far after it was hit.",
			banned: []string{
				"hit",
			},
			expected: "ball",
		},
		{
			name:      "paragraph consists only one word",
			paragraph: "Bob",
			banned:    []string{},
			expected:  "bob",
		},
	}

	// Run test cases
	for _, test := range tests {
		test := test
		t.Run(test.name, func(t *testing.T) {
			res := MostCommonWord(test.paragraph, test.banned)
			if res != test.expected {
				t.Errorf("%s: wrong answer returned. answer should be %s, but got %s", test.name, test.expected, res)
			}
		})
	}
}
