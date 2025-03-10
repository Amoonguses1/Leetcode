/*
This is an answer for
https://leetcode.com/problems/beautiful-arrangement/description/

Time: O(N!)
Space: O(N)
*/
package main

// baseCasePos represents the base case for the recursion in searchArrangement.
//
// When pos reaches this value, it means all positions in the arrangement
// have been successfully assigned, so a valid arrangement is found.
const baseCasePos = 1

// Returns the number of the beautiful arrangements.
//
// A beautiful arrangement is defined as a permutation of numbers from 1 to inputArraySize
// where, for each index i (1-based), either of the following conditions hold:
// - The number at index i is divisible by i.
// - i is divisible by the number at index i.
func CountArrangement(inputArraySize int) int {
	return searchArrangement(inputArraySize, inputArraySize, 0)
}

// performs a backtracking search to count beautiful arrangements.
//
// The function uses bitmasking to track which numbers have already been used.
// The `mask` variable represents used numbers,
// where the ith bit is set if the number i is used.
//
// Parameters:
// - inputArraySize: The original size of the array (N).
// - pos: The current position being filled in the arrangement (starts from N and decrements).
// - mask: A bitmask where each bit represents whether a number has been used.
//
// Returns:
// - The number of valid arrangements that can be formed from the current state.
func searchArrangement(inputArraySize, pos, mask int) int {
	if pos == baseCasePos {
		return 1
	}

	cnt := 0
	for digit := inputArraySize; digit > 0; digit-- {
		if isUnused(mask, digit) && isValidPlacement(pos, digit) {
			cnt += searchArrangement(inputArraySize, pos-1, mask|1<<digit)
		}
	}
	return cnt
}

// isUnused checks whether the number `bitShift` is not yet used in the bitmask.
func isUnused(mask, bitShift int) bool {
	return mask&1<<bitShift == 0
}

// checks if `value` can be placed at `pos` in a beautiful arrangement.
func isValidPlacement(pos, value int) bool {
	return pos%value == 0 || value%pos == 0
}
