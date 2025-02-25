/*
This is an answer for
https://leetcode.com/problems/partition-to-k-equal-sum-subsets/?envType=problem-list-v2&envId=backtracking

Time: O(N^k)
Space: O(k)
N is the length of nums
*/
package main

import "sort"

func canPartitionKSubsets(nums []int, k int) bool {
	sum := calcSum(nums)
	if sum%k != 0 {
		return false
	}

	res := make([]int, k)
	sort.Slice(nums, func(i, j int) bool {
		return nums[i] > nums[j]
	})

	return dfs(res, nums, sum/k)
}

func calcSum(nums []int) int {
	res := 0
	for _, num := range nums {
		res += num
	}
	return res
}

func dfs(res, nums []int, target int) bool {
	if len(nums) == 0 {
		return true
	}

	for i := 0; i < len(res); i++ {
		if res[i]+nums[0] <= target {
			res[i] += nums[0]
			if dfs(res, nums[1:], target) {
				return true
			}
			res[i] -= nums[0]
		}

		if res[i] == 0 {
			return false
		}
	}

	return false
}
