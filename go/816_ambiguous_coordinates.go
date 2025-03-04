/*
This is an answer for
https://leetcode.com/problems/ambiguous-coordinates/description/

Time: O(N^3)
Space: O(N^3)
*/

package main

import (
	"fmt"
	"strings"
)

// Returns a list of all possible valid coordinate pairs.
// All valid combinations of coordinates in the form of "(x, y)".
func ambiguousCoordinates(s string) []string {
	s = s[1 : len(s)-1]
	coordinates := []string{}

	for i := 1; i < len(s); i++ {
		pairs := generatePairs(generateCandidates(s[:i]), generateCandidates(s[i:]))
		coordinates = append(coordinates, pairs...)
	}
	return coordinates
}

// Generates all possible valid numeric representations from the given string.
func generateCandidates(s string) []string {
	if len(s) == 1 {
		return []string{s}
	}

	res := []string{}
	if isValidNumber(s) {
		res = append(res, s)
	}
	for i := 1; i < len(s); i++ {
		newString := s[:i] + "." + s[i:]
		if isValidNumber(newString) {
			res = append(res, newString)
		}
	}
	return res
}

// Checks whether the given string represents a valid numeric value.
func isValidNumber(s string) bool {
	// Check for leading zeros (only valid for "0" or "0.x")
	if s[0] == '0' && !(len(s) == 1 || s[1] == '.') {
		return false
	}

	// Check for trailing zeros after the decimal point
	if s[len(s)-1] == '0' && strings.Contains(s, ".") {
		return false
	}

	return true
}

// Combines two slices of coordinate candidates
func generatePairs(candi1, candi2 []string) []string {
	res := make([]string, len(candi1)*len(candi2))
	for i, s1 := range candi1 {
		for j, s2 := range candi2 {
			res[i*len(candi2)+j] = fmt.Sprintf("(%s, %s)", s1, s2)
		}
	}
	return res
}
