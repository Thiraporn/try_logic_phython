from greatest_common_divisor import gcd
# least_common_multiple

# Today, I want to implement a class for Least Common Multiple.


class LeastCommonMultiple:
    # Let’s start by defining the class and the lcm method.
    # LCM should handle negative numbers and return 0 if either number is 0
    def lcm(self, a, b):
        # Using abs() handles negative numbers.
        # Returning 0 if either number is 0 is correct.
        # a = abs(a)
        # b = abs(b)
        a, b = abs(a), abs(b)
        if a == 0 or b == 0:
            return 0
        # Now, how will you calculate the LCM using GCD?
        # I will use the formula LCM(a, b) = abs(a * b) // GCD(a, b) and call the existing gcd function or class.
        # Using integer division // is correct to get an integer result.

        return (a*b) // gcd.gcd(a, b)


# Creating  an instance and calling gcd works if it’s a method.
lcm = LeastCommonMultiple()
print(f'lcm.lcm(12, 18)>>> {lcm.lcm(12, 18)}')
# remak : It's easy way, i could also make gcd a static method so lcm() doesn’t need to create an instance every time. That would make our LCM class simpler to use.
