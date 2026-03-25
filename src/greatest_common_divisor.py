# greatest_common_divisor
class GreatestCommonDivisor:
    # recursive
    # def gcd(self, a, b):
    #     a = abs(a)
    #     b = abs(b)

    #     if a == 0 and b == 0:
    #         raise Exception(f'GCD undefined for (0,0)')
    #     if a == 0:
    #         return b
    #     if b == 0:
    #         return a

    #     return self.gcd(b, a % b)

    # nomal option
    def gcd(seft, a, b):
        # Using abs() handles negative numbers.
        a = abs(a)
        b = abs(b)
        # Using abs() handles negative numbers.
        # Using ValueError for invalid input is perfect.
        if a == 0 and b == 0:
            raise Exception(f'GCD undefined for (0,0)')
        while b != 0:
            a, b = b, a % b
        return a


gcd = GreatestCommonDivisor()
print(f'gcd.gcd(48, 18)>>> {gcd.gcd(48, 18)}')
