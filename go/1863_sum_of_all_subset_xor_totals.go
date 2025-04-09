/*
This is an answer for
https://leetcode.com/problems/sum-of-all-subset-xor-totals/description/

Time: O(2^N)
Space: O(N)
N = len(nums)
*/
package main

// Returns the sum of XOR values for all subsets of the given slice nums.
// For each subset of nums, the elements are XOR-ed together, and this function sums up all such results.
func subsetXORSum(nums []int) int {
	return totalSubsetXOR(0, nums)
}

// Recursively computes the XOR sum of all subsets.
// cur keeps the XOR value built so far, and nums is the remaining list of elements to consider.
func totalSubsetXOR(cur int, nums []int) int {
	if len(nums) == 0 {
		return cur
	}

	return totalSubsetXOR(cur, nums[1:]) + totalSubsetXOR(cur^nums[0], nums[1:])
}
