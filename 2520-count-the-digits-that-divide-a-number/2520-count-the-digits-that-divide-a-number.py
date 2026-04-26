class Solution:
    def countDigits(self, num: int) -> int:
        sum=0
        num1=num
        while num>0:
            n=num%10
            if num1% n==0:
                sum+=1
            num=num//10
        return sum
        