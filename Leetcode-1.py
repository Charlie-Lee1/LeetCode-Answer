"""题目描述：给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 target  的那 两个 整数，并返回它们的数组下标。

    你可以假设每种输入只会对应一个答案，并且你不能使用两次相同的元素。

    你可以按任意顺序返回答案。
我的理解：利用字典(哈希表)，看差值，要是遍历到差值，return对应值
"""
class Solution(object):
    def twoSum(self, nums:list, target):
        dic={}
        for i, num in enumerate(nums):
            gap=target-num
            if gap in dic:
                return [dic[gap],i]
            dic[num]=i
