class Solution:
    def canMeasureWater(self, x: int, y: int, z: int) -> bool:

        def gcd(a, b):
            while b:
                #if b > a: a,b = b,a (swap)
                a, b = b, a % b
            return a

        if y == 0:  # deal with ZeroDivisionError
            return z == 0 or z == x

        return (z <= x+y) and z % (gcd(x, y)) == 0
