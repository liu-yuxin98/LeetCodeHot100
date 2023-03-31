class Solution:
    def cutRope(self, number: int) -> int:
        # write code here
        product = 1
        while number > 0:
            if number == 2:
                product *= 2
                return product
            elif number == 3:
                product *= 3
                return product
            elif number == 4:
                product *= 2
                number -= 2
            else:
                product *= 3
                number -= 3
