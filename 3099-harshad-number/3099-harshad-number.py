class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        sum=0
        num=x
        while x>0:
            n=x%10
            sum+=n
            x=x//10
        if num%sum==0:
            return sum
        return -1

        