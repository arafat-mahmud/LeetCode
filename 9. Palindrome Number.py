class Solution:
    def isPalindrome(self, x):

        if x < 0:
            return False

        number = x
        reverse = 0

        for _ in range(len(str(number))):
            reverse = reverse * 10 + number % 10
            number //= 10
            
        return x == reverse

