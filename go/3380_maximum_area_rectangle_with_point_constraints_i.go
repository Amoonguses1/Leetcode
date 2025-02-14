/*
This is an answer for
https://leetcode.com/problems/maximum-area-rectangle-with-point-constraints-i/

Time: O(N^2)
Space: O(1)
N = len(points)
*/
package main

import "sort"

type Point struct {
	X int
	Y int
}

// maxRectangleArea returns the maximum area of a valid rectangle formed by four points.
// A valid rectangle satisfies the following conditions:
// 1. Can be formed using four of these points as its corners.
// 2. Does not contain any other point inside or on its border.
// 3. Has its edges parallel to the axes.
func maxRectangleArea(points [][]int) int {
	sort.Slice(points, func(i, j int) bool {
		if points[i][0] == points[j][0] {
			return points[i][1] < points[j][1]
		}
		return points[i][0] < points[j][0]
	})

	maxArea := -1

	// A valid rectangle should not contain any other points inside or on its border.
	// Therefore, the two smallest points' indices must be adjacent to form a valid rectangle.
	for i := 0; i < len(points)-2; i++ {
		if points[i][0] != points[i+1][0] {
			continue
		}

		point1 := Point{points[i][0], points[i][1]}
		point2 := Point{points[i+1][0], points[i+1][1]}
		for j := i + 2; j < len(points)-1; j++ {
			point3 := Point{points[j][0], points[j][1]}
			point4 := Point{points[j+1][0], points[j+1][1]}

			// Check if point3 is vertically within the bounds of the rectangle defined by point1 and point2,
			// ensuring that the new rectangle doesn't contain any other point inside or on its border.
			if point1.Y <= point3.Y && point3.Y <= point2.Y {
				if isRectangle(point1, point2, point3, point4) {
					maxArea = max(maxArea, (points[j][0]-points[i][0])*(points[j+1][1]-points[j][1]))
				}
				break
			}
		}
	}

	return maxArea
}

// isRectangle checks if the given four points can form a valid rectangle.
// It returns true if the points are the corners of a rectangle with edges parallel to the axes.
func isRectangle(point1, point2, point3, point4 Point) bool {
	return point3.X == point4.X && point1.Y == point3.Y && point2.Y == point4.Y
}
