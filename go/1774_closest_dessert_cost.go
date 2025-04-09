/*
This is an answer for
https://leetcode.com/problems/closest-dessert-cost/description/

Time: O(N3^M)
Space: O(M)
N = len(baseCosts) M = len(toppingCosts)
*/
package main

// maxToppingCount is maximum number of toppings that can be placed on one ice
const maxToppingCount = 2

// maxPrice is the largest int to initialize the return value in the chooseToppings function.
const maxPrice = int(^uint(0) >> 1)

// Returns the closest possible cost of the dessert to target.
// If there are multiple, return the lower one.
//
// Rules for making your dessert
// There must be exactly one ice cream base.
// You can add one or more types of topping or have no toppings at all.
// There are at most two of each type of topping.
func closestCost(baseCosts []int, toppingCosts []int, target int) int {
	res := maxPrice
	for _, cost := range baseCosts {
		candidate := chooseToppings(toppingCosts, target-cost, 0)
		if isClosestToZero(candidate, res) {
			res = candidate
		}
	}
	return target - res
}

// Returns the minimum difference between target and the made ice price.
func chooseToppings(toppingCosts []int, target, pos int) int {
	if pos == len(toppingCosts) {
		return target
	}

	res := maxPrice
	for i := 0; i <= maxToppingCount; i++ {
		candidates := chooseToppings(toppingCosts, target, pos+1)
		if isClosestToZero(candidates, res) {
			res = candidates
		}
		target -= toppingCosts[pos]
	}
	return res
}

// Checks if a is closer to zero than b.
// If the absolute value is equal, checks if a is smaller than b.
func isClosestToZero(a, b int) bool {
	absA := intAbs(a)
	absB := intAbs(b)
	if absA < absB {
		return true
	}

	if absA == absB && a > b {
		return true
	}

	return false
}

// Returns the absolute value.
func intAbs(a int) int {
	if a > 0 {
		return a
	}

	return -a
}
