/*
This is an answer for
https://leetcode.com/problems/remove-duplicates-from-sorted-list/description/

Time: O(N)
Space: O(N)
N is the number of ListNodes
*/
package main

// Definition for singly-linked list.
type ListNode struct {
	Val  int
	Next *ListNode
}

func deleteDuplicates(head *ListNode) *ListNode {
	if head == nil {
		return nil
	}
	dummy := &ListNode{Val: head.Val - 1, Next: nil}
	prev := dummy
	for head != nil {
		if prev.Val != head.Val {
			prev.Next = &ListNode{Val: head.Val, Next: nil}
			prev = prev.Next
		}
		head = head.Next
	}
	return dummy.Next
}
