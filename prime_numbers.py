import math


def isPrimeNumber(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def listPrimeNumbers(n):
    numbers = []
    for i in range(2, n+1):
        if isPrimeNumber(i):
            numbers.append(i)
    return numbers


num = int(input(f"Input a number : "))
print(f"Is {num} prime number ? {isPrimeNumber(num)}")
print(f"List prime number of {num} are {listPrimeNumbers(num)}")


# # รับ input จากผู้ใช้
# num = int(input("Input a number: "))

# # แสดงผล
# print(f"Is {num} prime number? {isPrimeNumber(num)}")
# print(f"List prime numbers of {num} are: {listPrimeNumbers(num)}")
