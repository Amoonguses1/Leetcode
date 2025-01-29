/*
This code is an answer for https://leetcode.com/problems/redundant-connection/description/ .

Time: O(N^2)
Space: O(N)
N = len(edges)
*/
package main

func findRedundantConnection(edges [][]int) []int {
	var parent = make([]int, len(edges)+1)
	for i := 1; i <= len(edges); i++ {
		parent[i] = i
	}

	var result []int
	for i := 0; i < len(edges); i++ {
		doUnion(edges[i][0], edges[i][1], parent, &result)
	}

	return result
}

func doUnion(i, j int, parents []int, result *[]int) {
	u1, u2 := findParent(i, parents), findParent(j, parents)
	if u1 != u2 {
		parents[u2] = u1
	} else {
		*result = append(*result, i)
		*result = append(*result, j)
	}
}

func findParent(i int, parent []int) int {
	if parent[i] == i {
		return i
	}

	return findParent(parent[i], parent)
}
