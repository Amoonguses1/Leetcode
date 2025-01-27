/*
This code is an answer for https://leetcode.com/problems/sqrtx/ .

Time: O(logx)
Space: O(1)
*/
package main

func mySqrt(x int) int {
	left, right := -1, x+1

	// binary search
	for (right - left) > 1 {
		mid := (right + left) / 2
		if mid*mid > x {
			right = mid
		} else {
			left = mid
		}
	}
	return left
}
