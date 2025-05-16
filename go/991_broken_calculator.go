/*
This is an answer for
https://leetcode.com/problems/broken-calculator/description/

Time: O(log(target))
Space: O(1)
*/
package main

func brokenCalc(startValue int, target int) int {
	res := 0
	for target > startValue {
		res++
		if target%2 == 0 {
			target = target / 2
		} else {
			target += 1
		}
	}
	return res + startValue - target
}
