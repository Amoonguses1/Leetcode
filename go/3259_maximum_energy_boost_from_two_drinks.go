/*
This is an answer for
https://leetcode.com/problems/maximum-energy-boost-from-two-drinks/description/

Time: O(N)
Space: O(N)
N = len(energyDrinkA) = len(energyDrinkB)
*/
package main

func maxEnergyBoost(energyDrinkA []int, energyDrinkB []int) int64 {
	drinks := [][]int{energyDrinkA, energyDrinkB}
	length := len(energyDrinkA)
	total := make([][]int, len(drinks))
	for i := range total {
		total[i] = make([]int, length)
	}

	for i := 0; i < length; i++ {
		for kind := 0; kind < len(drinks); kind++ {
			if i == 0 {
				total[kind][i] = drinks[kind][i]
			} else {
				total[kind][i] = total[kind][i-1] + drinks[kind][i]
				if i > 1 {
					otherKind := otherDrinkKind(kind)
					total[kind][i] = max(total[otherKind][i-2]+drinks[kind][i], total[kind][i])
				}
			}
		}
	}
	return int64(max(total[0][length-1], total[1][length-1]))
}

func otherDrinkKind(current int) int {
	switch current {
	case 0:
		return 1
	case 1:
		return 0
	default:
		panic("invalid drink kind index")
	}
}
