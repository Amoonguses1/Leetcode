/*
This is an answer for
https://leetcode.com/problems/single-number-ii/description/

Time: O(N)
Space: O(N)
*/
package main

// Returns the single element.
// the input slice nums must be following the rule
//
// every elements appears three times except for one,
// which appears only once.
func singleNumber(nums []int) int {
	once, twice := 0, 0
	for _, num := range nums {
		// Update `once` to store bits that have appeared exactly once.
		// If a bit is in `twice`, we remove it from `once` (to prevent counting three times).
		once ^= (num & ^twice)
		// Update `twice` to store bits that have appeared exactly twice.
		// If a bit is in `once`, we remove it from `twice` (to prevent counting once).
		twice ^= (num & ^once)
	}

	return once
}
