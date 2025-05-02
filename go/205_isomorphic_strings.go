/*
This is an answer for
https://leetcode.com/problems/isomorphic-strings/description/

Time: O(N)
Space: O(N)
N = len(source) = len(target)
*/
package main

// Checks if the two given strings are isomorphic.
// Two strings source and target are isomorphic
// if the characters in source can be replaced to get target,
// with a one-to-one mapping and vice versa.
func isIsomorphic(source string, target string) bool {
	// Check if the lengths of the strings are equal
	if len(source) != len(target) {
		return false
	}

	// Maps to record the mapping from source to target and target to source
	sourceToTarget := make(map[byte]byte)
	targetToSource := make(map[byte]byte)

	for i := 0; i < len(source); i++ {
		charS := source[i]
		charT := target[i]

		// Check mapping from source to target
		if mappedCharT, exists := sourceToTarget[charS]; !exists {
			sourceToTarget[charS] = charT
		} else if mappedCharT != charT {
			return false
		}

		// Check mapping from target to source
		if mappedCharS, exists := targetToSource[charT]; !exists {
			targetToSource[charT] = charS
		} else if mappedCharS != charS {
			return false
		}
	}

	return true
}
