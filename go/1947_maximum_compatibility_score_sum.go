/*
This is an answer for
https://leetcode.com/problems/maximum-compatibility-score-sum/

Time: O(NM^2)
Space: O(M^2)
M = len(students) = len(mentors)
N = len(students[i]) = len(mentors[j]), 0=<i<N,0<=j<N
*/
package main

// Returns the maximum compatibility score sum.
//
// The compatibility score of a student-mentor pair is the number of answers
// that are the same for both the student and the mentor.
func maxCompatibilitySum(students [][]int, mentors [][]int) int {
	scores := compatibilityScores(students, mentors)
	used := make([]bool, len(mentors))
	res := searchMaximumCompatibilityScore(scores, used, 0, 0)
	return res
}

// Returns all the pairs compatibility scores.
func compatibilityScores(students, mentors [][]int) [][]int {
	totalScores := [][]int{}
	for i := 0; i < len(students); i++ {
		scores := []int{}
		for j := 0; j < len(mentors); j++ {
			score := 0
			for k := 0; k < len(students[0]); k++ {
				score += 1 - (students[i][k] ^ mentors[j][k])
			}
			scores = append(scores, score)
		}
		totalScores = append(totalScores, scores)
	}
	return totalScores
}

// Recursively compute the maximum compatibility score.
func searchMaximumCompatibilityScore(scores [][]int, used []bool, pos, curScore int) int {
	if pos == len(used) {
		return curScore
	}

	res := 0
	for i := 0; i < len(scores); i++ {
		if !used[i] {
			used[i] = true
			res = max(res, searchMaximumCompatibilityScore(scores, used, pos+1, curScore+scores[pos][i]))
			used[i] = false
		}
	}
	return res
}
