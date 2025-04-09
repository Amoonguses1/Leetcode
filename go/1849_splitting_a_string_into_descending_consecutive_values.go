/*
This is an answer for
https://leetcode.com/problems/splitting-a-string-into-descending-consecutive-values/

Time: O(N!)
Space: O(N!)
N = len(s)
*/
package main

import (
	"math"
	"strconv"
)

// invalidPrev is a sentinel value indicating that no previous number exists yet.
const invalidPrev = -1

// intMax is an upper bound to prevent overflow when constructing integers from the substring.
var intMax = int(math.Pow10(9))

// Checks if we can split s into two or more non-empty substrings
// such that the numerical values of the substrings are in descending order
// and the difference between numerical values of every two adjacent substrings is equal to 1.
func splitString(s string) bool {
	return searchValidSubstrings(0, invalidPrev, s, false)
}

// Attempts to recursively split the string s starting from position pos.
// prev represents the previous numeric value used for comparison (or invalidPrev if unset).
// divided is true if at least one valid split has been made so far.
// It returns true if a valid decreasing sequence with a difference of 1 is found.
func searchValidSubstrings(pos, prev int, s string, divided bool) bool {
	if pos == len(s) && divided {
		return true
	}

	cur := 0
	for i := pos; i < len(s); i++ {
		if cur > intMax {
			return false
		}
		num, _ := strconv.Atoi(string(s[i]))
		cur = cur*10 + num
		if prev == invalidPrev {
			if searchValidSubstrings(i+1, cur, s, false) {
				return true
			}
		}
		if cur == prev-1 {
			if searchValidSubstrings(i+1, cur, s, true) {
				return true
			}
		}
	}
	return false
}
