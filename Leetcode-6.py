"""题目描述：将一个给定字符串 s 根据给定的行数 numRows ，以从上往下、从左到右进行 Z 字形排列。

    比如输入字符串为 "PAYPALISHIRING" 行数为 3 时，排列如下：

    P   A   H   N
    A P L S I I G
    Y   I   R
    之后，你的输出需要从左往右逐行读取，产生出一个新的字符串


我的理解：与其说是Z形变换，不如说是N形变换。
    找规律：1.一个字符串可以写成12341234这样的循环顺序
           2.需要做的就是找到每个字符对应的行在哪"""
    
class Solution(object):
        def convert(self,s,numRows):
            if numRows==1:
                return s             #当要求行数为1，直接输出
            else:
                group=(numRows-1)*2  #找到循环周期
                rows=[""]*numRows    #根据行数创建列表
                for i,char in enumerate(s):
                    x=i%group
                    rows[min(x,group-x)] +=char #将字符加入对应的行中
                return "".join(rows)