/*
This is an answer for
https://leetcode.com/problems/longest-strictly-increasing-or-strictly-decreasing-subarray/description/

Time: O(N)
Space: O(1)
N = len(nums)
*/
package main

// longestMonotonicSubarray returns the length of the longest continuous subarray
// in which elements are either strictly increasing or strictly decreasing.
//
// The input nums must contain at least one element.
func longestMonotonicSubarray(nums []int) int {
	// Edge case: nums contains only one element.
	if len(nums) == 1 {
		return 1
	}

	// Initialize tracking variables.
	maxLength := 1
	curStreak := 1
	diff := nums[1] - nums[0]

	for i := 1; i < len(nums); i++ {
		curDiff := nums[i] - nums[i-1]
		if curDiff == 0 {
			// Reset the current streak if consecutive elements are equal.
			curStreak = 1
		} else if curDiff*diff < 0 {
			// Reset streak to 2 if the direction changes.
			// (since the new streak starts with the previous and current element.)
			curStreak = 2
		} else {
			// Extend current streak.
			curStreak++
		}

		// Update direction and maximum length.
		diff = curDiff
		maxLength = max(maxLength, curStreak)
	}

	return maxLength
}
