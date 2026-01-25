"""
    题目描述：给你两个 非空 的链表，表示两个非负的整数。它们每位数字都是按照 逆序 的方式存储的，并且每个节点只能存储 一位 数字。请你将两个数相加，并以相同形式返回一个表示和的链表。
    你可以假设除了数字 0 之外，这两个数都不会以 0 开头。
我的理解：单个数位置相加，一定注意进位
"""
class ListNode(object):
    def __init__(self, val=0, next=None):
         self.val = val
class Solution:
     def addTwoNumbers(self, l1=ListNode, l2=ListNode):
        head=ListNode(0)    #创建新链表，记录答案
        current=head    #初始化指针
        carry=0  #初始化进位
        while l1 or l2 or carry:
            val1=l1.val if l1 else 0
            val2=l2.val if l2 else 0
            val_sum=val1+val2+carry
            carry=val_sum%10 #获取进位
            digit=val_sum//10
            current.next=ListNode(digit)
            current=current.next #移动指针到下一位
            if l1:
                l1=l1.next #移动l1的指针
            if l2:
                l2=l2.next
        return head.next

