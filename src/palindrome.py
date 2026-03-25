def palindrome(text):
    isPalindrome = True
    for front in range(len(text)//2):
        if text[front].lower() != text[len(text)-front-1].lower():
            isPalindrome = False
            break

    return isPalindrome


input = input(f'Input String ')
print(f'palindrome >> {palindrome(input)}')
