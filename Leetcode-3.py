"""
    题目描述：给定一个字符串 s ，请你找出其中不含有重复字符的 最长 子串 的长度。
我的理解：可以运用窗口思想，当子字符串不存在相应元素时，添加并移动右指针，存在则删除并移动左指针，直到没有重复
"""
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        start=0
        end=0   #初始化头指针和尾指针
        substring=set()  #初始化子串
        max_len=0  #初始化最大长度
        len=0 #记录子串随时的长度变化
        while end<=len(s):
            if s[end] not in substring:
                substring.add(s[end])
                end+=1 #移动右指针
                len+=1
                if len>max_len:
                    max_len=len
                
            else:
                while s[end] in substring:
                    substring.remove(s[start])
                    start+=1  #移动左指针
                    len-=1

        return max_len