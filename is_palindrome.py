import unittest
   


   
def is_palindrome(value):
    print(value[::1])
    if value == value[::-1]:
        return True
    else:
        return False






class TestIsPalindrome(unittest.TestCase):

    def test_with_a(self):

        input = "a"

        result = is_palindrome(input)

        self.assertTrue(result)

    def test_with_pepe(self):

        input = "pepe"

        result = is_palindrome(input)

        self.assertTrue(result)

    def test_with_ala(self):

        input = "ala"

        result = is_palindrome(input)

        self.assertTrue(result)



    def test_with_neuquen(self):

        input = "neuquen"

        result = is_palindrome(input)

        self.assertTrue(result)


unittest.main()