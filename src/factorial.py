def factorial(number):
    if number < 0:
        raise Exception('please input a number >= 0!')
    if number <= 1:
        return 1
    return number * factorial(number-1)


input = int(input(f'Input a number '))
print(f'Factorial >> {factorial(input)}')
