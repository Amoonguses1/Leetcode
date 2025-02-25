/*
This is an answer for
https://leetcode.com/problems/shopping-offers/

Time: O(N*(M^T))
Space: O(T)
T is the sum of needs
N is the length of price, needs
M is the length of special
*/

package main

// shoppingOffers calculates the minimum cost to buy all necessary items.
func shoppingOffers(price []int, special [][]int, needs []int) int {
	curMin := totalNormalPrice(price, needs)
	return minCostDFS(price, special, needs, curMin, 0)
}

// minCostDFS recursively calculates the minimum cost to purchase all required items.
// It explores the available special offers and returns the best price to cover the remaining needs.
func minCostDFS(price []int, special [][]int, needs []int, curMin, curVal int) int {
	if curVal >= curMin {
		return curMin
	}

	for i, items := range special {
		if availableOffer(items, needs) {
			decreaseNeeds(items, needs)
			curMin = minCostDFS(price, special[i:], needs, curMin, curVal+items[len(items)-1])
			increaseNeeds(items, needs)
		}
	}
	return min(curMin, curVal+totalNormalPrice(price, needs))
}

func totalNormalPrice(price, needs []int) int {
	total := 0
	for i, count := range needs {
		total += count * price[i]
	}
	return total
}

func availableOffer(items, needs []int) bool {
	for i, count := range needs {
		if count < items[i] {
			return false
		}
	}
	return true
}

func decreaseNeeds(items, needs []int) {
	for i := 0; i < len(needs); i++ {
		needs[i] -= items[i]
	}
}

func increaseNeeds(items, needs []int) {
	for i := 0; i < len(needs); i++ {
		needs[i] += items[i]
	}
}
