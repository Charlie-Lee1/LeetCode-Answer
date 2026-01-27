"""
    题目描述：给定一个长度为 n 的整数数组 height 。有 n 条垂线，第 i 条线的两个端点是 (i, 0) 和 (i, height[i]) 。
找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。
返回容器可以储存的最大水量。  说明：你不能倾斜容器。

我的理解：就是寻找最大面积，想象柱状图,运用双指针的方式
"""
class Solution(object):
    def maxArea(self,height):
        length=len(height)
        if length==1:
            return 0
        pointer1=0
        pointer2=length-1  #初始化双指针
        max_volumn=0
        while pointer1<=pointer2:
            height1=height[pointer1]
            height2=height[pointer2]
            h=min(height1,height2)
            volumn=h**(pointer2-pointer1)
            if volumn>max_volumn:
                max_volumn=volumn
            if height1<=height2:
                pointer1+=1
            else:
                pointer2-=1
        return max_volumn
