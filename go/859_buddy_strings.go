/*
This is an answer for
https://leetcode.com/problems/buddy-strings/description/

Time: O(N)
Space: O(N)
N is the length of the given string
*/
package main

// buddyStrings return true
// if you can swap two letters in s so the result is equal to goal.
func BuddyStrings(s string, goal string) bool {
	if len(s) != len(goal) {
		return false
	}

	// If two strings are the same,
	// then the same characters in the string can be exchanged.
	if s == goal && len(s) != computeNumberOfString(s) {
		return true
	}

	swapCandidates := []int{}
	for i := 0; i < len(s); i++ {
		if s[i] != goal[i] {
			swapCandidates = append(swapCandidates, i)
		}
	}

	return isSameAfterSwap(s, goal, swapCandidates)
}

// isSameAfterSwap returns true
// if the given string s can be formed the given string goal by swapping
// two candidate position.
func isSameAfterSwap(s, goal string, swapCandidates []int) bool {
	if len(swapCandidates) != 2 {
		return false
	}
	i, j := swapCandidates[0], swapCandidates[1]

	return s[i] == goal[j] && s[j] == goal[i]
}

// computeNumberOfString returns
// the number of the character types in the given string.
func computeNumberOfString(s string) int {
	counter := make(map[byte]struct{})
	for i := 0; i < len(s); i++ {
		counter[s[i]] = struct{}{}
	}

	return len(counter)
}
