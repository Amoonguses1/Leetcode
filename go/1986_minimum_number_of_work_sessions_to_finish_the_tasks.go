/*
This is an answer for
https://leetcode.com/problems/minimum-number-of-work-sessions-to-finish-the-tasks/description/

Time: O(N*2^N)
Space: O(N*2^N)
N = len(tasks)
*/
package main

type State struct {
	mask   int
	remain int
}

func minSessions(tasks []int, sessionTime int) int {
	stateMap := make(map[State]int)
	n := len(tasks)
	dp(tasks, 1<<n-1, sessionTime, 0, stateMap)
	return stateMap[State{mask: 1<<n - 1, remain: 0}]
}

func dp(tasks []int, mask, sessionTime, remain int, stateMap map[State]int) int {
	if mask == 0 {
		return 0
	}

	if val, ok := stateMap[State{mask: mask, remain: remain}]; ok {
		return val
	}
	n := len(tasks)
	res := n
	for i := 0; i < n; i++ {
		if ((mask >> i) & 1) != 0 {
			newMask := ^(1 << i) & mask
			if tasks[i] <= remain {
				res = min(res, dp(tasks, newMask, sessionTime, remain-tasks[i], stateMap))
			} else {
				res = min(res, dp(tasks, newMask, sessionTime, sessionTime-tasks[i], stateMap)+1)
			}
		}
	}
	stateMap[State{mask: mask, remain: remain}] = res
	return res
}
