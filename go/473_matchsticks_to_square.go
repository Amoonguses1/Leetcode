/*
This is an answer for
https://leetcode.com/problems/matchsticks-to-square/description/

Time: O(4^^N)
Space: O(N)
*/

package main

import "sort"

// makesquare returns true if you can make this square
func makesquare(matchsticks []int) bool {
	target := 0
	for _, length := range matchsticks {
		target += length
	}
	if target%4 != 0 {
		return false
	}

	target /= 4
	// sort in reverse
	sort.Slice(matchsticks, func(i, j int) bool { return matchsticks[i] > matchsticks[j] })
	sides := []int{matchsticks[0], 0, 0, 0}
	return canMakeSquare(matchsticks, sides, target, 1)
}

// canMakeSquare searches recursively
// to find valid distribution of matchsticks to 4 sides
func canMakeSquare(matchsticks, sides []int, target, index int) bool {
	// base case: the length of one side over target
	for i := 0; i < len(sides); i++ {
		if sides[i] > target {
			return false
		}
	}

	// base case: successfully divided matchsticks
	if len(matchsticks) == index {
		return true
	}

	for i := 0; i < len(sides); i++ {
		sides[i] += matchsticks[index]
		if canMakeSquare(matchsticks, sides, target, index+1) {
			return true
		}
		sides[i] -= matchsticks[index]
		if sides[i] == 0 {
			return false
		}
	}
	return false
}
