/*
This is an answer for
https://leetcode.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters/

Time: O(2^N)
Space: O(2^N)
*/
package main

import "math/bits"

// Returns the maximum possible length of s,
// which is formed by the concatenation of a subsequence of arr that has unique characters
func maxLength(arr []string) int {
	masks := []int{}
	for _, word := range arr {
		mask := convertUniqueCharactersToBit(word)
		if mask != 0 {
			masks = append(masks, mask)
		}
	}

	return backTrack(masks, 0, 0, 0)
}

// Returns the binary expression of word.
// if there is duplicated characters, return 0.
func convertUniqueCharactersToBit(word string) int {
	bit := 0
	for _, ch := range word {
		bit ^= 1 << (ch - 'a')
		if (bit & (1 << (ch - 'a'))) == 0 {
			return 0
		}
	}
	return bit
}

// Finds the maximum length of a concatenated string with unique characters
// using a backtracking approach.
//
// The function iterates through the masks slice, checking if adding a new mask results in
// duplicate characters (using bitwise AND). If not, it recursively explores the next
// possibilities, tracking the maximum length found.
func backTrack(masks []int, pos, mask, length int) int {
	if pos >= len(masks) {
		return length
	}

	res := 0
	for i := pos; i < len(masks); i++ {
		if masks[i]&mask == 0 {
			newMask := masks[i] | mask
			res = max(res, bits.OnesCount(uint(newMask)))
			res = max(res, backTrack(masks, i+1, newMask, bits.OnesCount(uint(newMask))))
		}
	}
	return res
}
