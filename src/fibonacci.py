def fibonacci(number):
    # base case
    if number < 0:
        return 0
    if number == 1 or number == 2:
        return 1
    # otherwise recursive
    return fibonacci(number-1) + fibonacci(number-2)


name = int(input(f'Enter a number : '))
print(f'Fibonacci >> {fibonacci(name)}')
