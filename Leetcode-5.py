"""
    题目描述：给你一个字符串 s，找到 s 中最长的 回文 子串。
我的理解：回文子串分为奇数串和偶数串，需要用到双指针向左右移动，遇到不同的停止
"""
class Solution(object):
    def longestPalindrome(self, s):
        n = len(s)
        if n < 2:
            return s
    
        start, max_len = 0, 1  # 初始化为第一个字符
    
        for i in range(n):
            # 奇数长度回文
            left = right = i
            while left >= 0 and right < n and s[left] == s[right]:
                cur_len = right - left + 1
                if cur_len > max_len:
                    max_len = cur_len
                    start = left
                left -= 1
                right += 1
        
            # 偶数长度回文
            left, right = i, i + 1
            while left >= 0 and right < n and s[left] == s[right]:
                cur_len = right - left + 1
                if cur_len > max_len:
                    max_len = cur_len
                    start = left
                left -= 1
                right += 1
    

        return s[start:start + max_len]
