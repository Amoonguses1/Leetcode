package main

import "testing"

// TestShortestCompletingWord tests the ShortestCompletingWord function
// with some cases.
func TestShortestCompletingWord(t *testing.T) {
	// Define test cases
	tests := []struct {
		name         string
		licensePlate string
		words        []string
		expected     string
	}{
		{
			name:         "only one completing word",
			licensePlate: "1s3 PSt",
			words: []string{
				"step",
				"steps",
				"stripe",
				"stepple",
			},
			expected: "steps",
		},
		{
			name:         "return the shortest length completing word",
			licensePlate: "1s3 456",
			words: []string{
				"looks",
				"pest",
			},
			expected: "pest",
		},
		{
			name:         "return the shortest length and first completing word",
			licensePlate: "1s3 456",
			words: []string{
				"looks",
				"pest",
				"stew",
				"show",
			},
			expected: "pest",
		},
	}

	// Run test cases
	for _, test := range tests {
		test := test
		t.Run(test.name, func(t *testing.T) {
			res := ShortestCompletingWord(test.licensePlate, test.words)
			if res != test.expected {
				t.Errorf("%s: wrong answer returned. answer should be %s, but got %s", test.name, test.expected, res)
			}
		})
	}
}
