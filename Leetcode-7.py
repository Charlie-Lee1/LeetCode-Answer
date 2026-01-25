"""
    题目描述：给你一个 32 位的有符号整数 x ，返回将 x 中的数字部分反转后的结果。如果反转后整数超过 32 位的有符号整数的范围 [−231,  231 − 1] ，就返回 0。
    假设环境不允许存储 64 位整数（有符号或无符号）。
我的理解：分正负讨论，暴力反转字符串，在判断临界条件。
"""
class Solution(object):
    def reverse(self, x):
        if x==0:
            return 0
        while x%10==0:
            x=x//10
        else:
            if x<0:
                x1=-x
                string=str(x1)
            else:
                string=str(x)
            new_string=string[::-1]
            if int(new_string)>=2**31 or int(new_string)<-2**31:
                return 0
            else:
                if x<0:
                    result=int(new_string)
                    return -result
                else:
                    result=int(new_string)
                    return result