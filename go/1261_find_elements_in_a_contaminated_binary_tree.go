/*
This is an answer for
*/
package main

/**
* Definition for a binary tree node.
* type TreeNode struct {
*     Val int
*     Left *TreeNode
*     Right *TreeNode
* }
 */

type FindElements struct {
	valMap map[int]struct{}
}

// Initializes the object with a contaminated binary tree and recovers it.
// FintElements struct has a Find method
// that tells the given target value is in the given binary tree.
// Time: O(N)
// Space: O(N)
// N is the number of nodes in the given binary tree.
func Constructor(root *TreeNode) FindElements {
	valMap := make(map[int]struct{})
	nodeStack := []*TreeNode{root}
	valStack := []int{0}
	for len(nodeStack) > 0 {
		node := nodeStack[len(nodeStack)-1]
		nodeStack = nodeStack[:len(nodeStack)-1]
		val := valStack[len(valStack)-1]
		valStack = valStack[:len(valStack)-1]
		valMap[val] = struct{}{}
		if node.Left != nil {
			nodeStack = append(nodeStack, node.Left)
			valStack = append(valStack, val*2+1)
		}
		if node.Right != nil {
			nodeStack = append(nodeStack, node.Right)
			valStack = append(valStack, val*2+2)
		}
	}
	return FindElements{valMap: valMap}
}

// Returns true if the target value exists in the recovered binary tree.
// Time: O(1)
// Space: O(1)
func (this *FindElements) Find(target int) bool {
	_, found := this.valMap[target]
	return found
}

/**
 * Your FindElements object will be instantiated and called as such:
 * obj := Constructor(root);
 * param_1 := obj.Find(target);
 */
