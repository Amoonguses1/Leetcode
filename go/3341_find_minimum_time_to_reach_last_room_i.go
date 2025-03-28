/*
This is an answer for
https://leetcode.com/problems/find-minimum-time-to-reach-last-room-i/

Time: O(MN)
Space: O(MN)
M = len(moveTime), N = len(moveTime[0])
*/
package main

import "container/heap"

type timeToReachRoom struct {
	time int
	x    int
	y    int
}

type timeToReachRoomHeap []timeToReachRoom

func (h timeToReachRoomHeap) Len() int           { return len(h) }
func (h timeToReachRoomHeap) Less(i, j int) bool { return h[i].time < h[j].time }
func (h timeToReachRoomHeap) Swap(i, j int)      { h[i], h[j] = h[j], h[i] }

func (h *timeToReachRoomHeap) Push(x any) {
	*h = append(*h, x.(timeToReachRoom))
}

func (h *timeToReachRoomHeap) Pop() any {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[:n-1]
	return x
}

func minTimeToReach(moveTime [][]int) int {
	reachTimeHeap := &timeToReachRoomHeap{}
	heap.Push(reachTimeHeap, timeToReachRoom{time: 0, x: 0, y: 0})
	directions := [4][2]int{{1, 0}, {-1, 0}, {0, 1}, {0, -1}}
	moveTime[0][0] = -1

	for reachTimeHeap.Len() > 0 {
		popped := heap.Pop(reachTimeHeap)
		reach, _ := popped.(timeToReachRoom)
		for _, direction := range directions {
			nextX, nextY := reach.x+direction[0], reach.y+direction[1]
			if !isValidPos(nextX, nextY, moveTime) || moveTime[nextX][nextY] < 0 {
				continue
			}
			nextTime := max(reach.time+1, moveTime[nextX][nextY]+1)
			moveTime[nextX][nextY] = -1
			if hasReached(nextX, nextY, moveTime) {
				return nextTime
			}
			heap.Push(reachTimeHeap, timeToReachRoom{time: nextTime, x: nextX, y: nextY})
		}
	}
	return -1
}

func isValidPos(x, y int, grid [][]int) bool {
	return 0 <= x && x < len(grid) && 0 <= y && y < len(grid[0])
}

func hasReached(x, y int, grid [][]int) bool {
	return x == len(grid)-1 && y == len(grid[0])-1
}
