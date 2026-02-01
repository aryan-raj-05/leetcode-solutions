class Solution:
    def squareSum(self, n):
        if n < 10:
            return n ** 2
        sum = 0
        while n > 0:
            i = n % 10
            sum += i ** 2
            n = n // 10
        return sum
    

    def isHappy_slowFastPointer(self, n):
        slow = self.squareSum(n)
        fast = self.squareSum(n)

        while True:
            slow = self.squareSum(slow)
            fast = self.squareSum(self.squareSum(fast))
            
            if slow == 1:
                return True

            if slow == fast:
                return False


    def isHappy(self, n: int) -> bool:
        mySet = set()
        while True:
            sq = self.squareSum(n)
            if sq == 1:
                return True
            elif sq in mySet:
                return False
            else:
                mySet.add(sq)
                n = sq
