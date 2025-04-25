/*
This is an answer for
https://leetcode.com/problems/subarray-sum-equals-k/description/

Time: O(N)
Space: O(N)
*/
package main

func subarraySum(nums []int, k int) int {
	hashMap := make(map[int]int, len(nums))

	prefixSum := 0
	ans := 0
	for i := 0; i < len(nums); i++ {
		prefixSum += nums[i]
		if prefixSum == k {
			ans++
		}

		if val, ok := hashMap[prefixSum-k]; ok {
			ans += val
		}

		hashMap[prefixSum]++
	}
	return ans
}
