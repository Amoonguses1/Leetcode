/*
This is an answer for
https://leetcode.com/problems/split-a-string-into-the-max-number-of-unique-substrings/description/

Time: O(N*2^N)
Space: O(N)
*/
package main

// Returns the maximum number of unique substrings
// that the given string can be split into.
func maxUniqueSplit(s string) int {
	return backTrackUniqueSplit(s, make(map[string]struct{}))
}

// Finds the maximum number of unique substrings
// that the given string can be split into using a backtracking approach.
func backTrackUniqueSplit(s string, seen map[string]struct{}) int {
	if len(s) == 0 {
		return len(seen)
	}

	maxSplit := 0

	for i := 1; i <= len(s); i++ {
		// check if maxSplit can be updated
		if len(seen)+len(s)-i+1 <= maxSplit {
			break
		}

		_, found := seen[s[:i]]
		if !found {
			seen[s[:i]] = struct{}{}
			maxSplit = max(maxSplit, backTrackUniqueSplit(s[i:], seen))
			delete(seen, s[:i])
		}
	}

	return maxSplit
}
