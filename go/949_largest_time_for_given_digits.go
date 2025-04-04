/*
This is an answer for
https://leetcode.com/problems/largest-time-for-given-digits/description/

Time: O(N!)
Space: O(N!)
N = len(arr)
*/
package main

import "fmt"

// Finds the latest 24-hour time that can be made using each digit exactly once.
func largestTimeFromDigits(arr []int) string {
	largestIntTime := FindLargestValidTime(arr, [4]int{0, 0, 0, 0}, 0)
	if largestIntTime < 0 {
		return ""
	}
	return fmt.Sprintf("%02d:%02d", largestIntTime/60, largestIntTime%60)
}

// Finds the largest 24-hour time can be made using each digit exactly once with back tracking.
func FindLargestValidTime(arr []int, cur [4]int, pos int) int {
	if pos == len(arr) {
		return convertToIntTime(cur)
	}

	res := -1
	for i, num := range arr {
		if num != -1 {
			cur[pos] = num
			arr[i] = -1
			if isValidTime(cur) {
				validTime := FindLargestValidTime(arr, cur, pos+1)
				res = max(res, validTime)
			}
			cur[pos] = 0
			arr[i] = num
		}
	}
	return res
}

// Converts arr [4]int to int.
func convertToIntTime(timeArr [4]int) int {
	hours := timeArr[0]*10 + timeArr[1]
	minutes := timeArr[2]*10 + timeArr[3]
	return hours*60 + minutes
}

// Checks if the given time represents the valid 24-hour time.
func isValidTime(timeArr [4]int) bool {
	hours := timeArr[0]*10 + timeArr[1]
	minutes := timeArr[2]*10 + timeArr[3]
	if hours > 23 || minutes > 59 {
		return false
	}
	return true
}
