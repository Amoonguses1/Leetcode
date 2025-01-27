/*
This code is an answer for
https://leetcode.com/problems/minimum-number-of-operations-to-make-elements-in-array-distinct/ .

Time: O(N)
Space: O(N)
N = len(nums)
*/
package main

func minimumOperations(nums []int) int {
	usedNum := make(map[int]bool)
	removeIdx := -1

	for i := len(nums) - 1; i > -1; i-- {
		isUsed := usedNum[nums[i]]
		if isUsed {
			removeIdx = i
			break
		} else {
			usedNum[nums[i]] = true
		}
	}

	return (removeIdx + 3) / 3
}
