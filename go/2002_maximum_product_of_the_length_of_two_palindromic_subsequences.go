/*
This is an answer for
https://leetcode.com/problems/maximum-product-of-the-length-of-two-palindromic-subsequences/

Time: O(2^N)
Space: O(2^N)
N = len(s)
*/
package main

import (
	"math/bits"
	"strings"
)

// Return the maximum possible product of the lengths of the two palindromic subsequences.
func maxProduct(s string) int {
	candidates := generatePalindromicSubsequenceMask(s)
	res := 0
	for i := 0; i < len(candidates); i++ {
		for j := i + 1; j < len(candidates); j++ {
			if candidates[i]&candidates[j] == 0 {
				res = max(res, bits.OnesCount(candidates[i])*bits.OnesCount(candidates[j]))
			}
		}
	}
	return res
}

// Returns a list of bitmasks, where each bitmask represents a subsequence of the input string `s`
// that is a palindrome.
//
// Each bit in the mask corresponds to a character index in `s`.
// A bit set to 1 means the character at that index is included in the subsequence.
func generatePalindromicSubsequenceMask(s string) []uint {
	length := len(s)
	candidates := []uint{}
	for mask := 1; mask < (1 << length); mask++ {
		var sb strings.Builder
		for i := 0; i < length; i++ {
			if (mask & (1 << i)) != 0 {
				sb.WriteByte(s[i])
			}
		}

		if isPalindrome(sb.String()) {
			candidates = append(candidates, uint(mask))
		}
	}

	return candidates
}

// Returns if the given string is a palindrome string.
func isPalindrome(s string) bool {
	for i := 0; i < len(s)/2; i++ {
		if s[i] != s[len(s)-i-1] {
			return false
		}
	}
	return true
}
