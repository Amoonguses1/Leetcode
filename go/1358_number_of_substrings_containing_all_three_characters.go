/*
This is an answer for
https://leetcode.com/problems/number-of-substrings-containing-all-three-characters/description/

Time: O(N)
Space: O(1)
*/
package main

const (
	numChars     = 3
	startingByte = 'a'
)

// Returns the number of substrings containing at least one occurrence a, b and c.
func numberOfSubstrings(s string) int {
	slow := 0
	res := 0
	occurrence := [numChars]int{}
	for i := 0; i < len(s); i++ {
		occurrence[s[i]-startingByte]++
		for allRequiredCharsPresent(occurrence) {
			res += len(s) - i
			occurrence[s[slow]-startingByte]--
			slow++
		}
	}
	return res
}

// Returns true if all character counts are non-zero.
func allRequiredCharsPresent(occurrence [numChars]int) bool {
	for _, frequency := range occurrence {
		if frequency == 0 {
			return false
		}
	}
	return true
}
