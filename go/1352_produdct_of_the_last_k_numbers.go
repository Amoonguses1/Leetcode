/*
This is an answer for
https://leetcode.com/problems/product-of-the-last-k-numbers/description/
*/

package main

// this is a struct for accepting a stream of integers and
// retrieving the product of the last k integers of the stream.
type ProductOfNumbers struct {
	arr []int
}

// Constructor function returns the ProductOfNumbers structure.
func Constructor() ProductOfNumbers {
	return ProductOfNumbers{
		arr: []int{1},
	}
}

// Add appends a new integer to the list and updates the product history.
func (this *ProductOfNumbers) Add(num int) {
	// If the new integer is 0, any previous product calculations become invalid
	// because multiplying by 0 results in 0. In this case, we reset the list to [1],
	// effectively discarding previous values since they are no longer useful.
	if num == 0 {
		this.arr = []int{1}
		return
	}

	prev := 1
	if len(this.arr) > 0 {
		prev = this.arr[len(this.arr)-1]
	}
	this.arr = append(this.arr, prev*num)
}

// GetProduct returns the product of the last k integers in the stream.
func (this *ProductOfNumbers) GetProduct(k int) int {
	// If k exceeds the number of stored products (i.e., since the last reset),
	// it means a 0 was encountered, and any product involving it is 0.
	if len(this.arr) <= k {
		return 0
	}
	return this.arr[len(this.arr)-1] / this.arr[len(this.arr)-1-k]
}
