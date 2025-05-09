/*
This is an answer for
https://leetcode.com/problems/delete-operation-for-two-strings/

Time: O(MN)
Space: O(MN)
M = len(source), N = len(target)
*/
package main

func minDistance(source string, target string) int {
	sourceToTarget := make([][]int, len(source)+1)
	for i := range sourceToTarget {
		sourceToTarget[i] = make([]int, len(target)+1)
	}

	for i := 0; i < len(source)+1; i++ {
		for j := 0; j < len(target)+1; j++ {
			if i == 0 || j == 0 {
				sourceToTarget[i][j] = i + j
			} else if source[i-1] == target[j-1] {
				sourceToTarget[i][j] = sourceToTarget[i-1][j-1]
			} else {
				sourceToTarget[i][j] = 1 + min(sourceToTarget[i-1][j], sourceToTarget[i][j-1])
			}
		}
	}
	return sourceToTarget[len(source)][len(target)]
}
