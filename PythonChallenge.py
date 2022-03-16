#Palindrome method: check that a word is the same foward

# Is Palindrome

# A palindrome is a word that is spelled the same forwards
# and backwards.

# Write a method is_palindrome(word) that takes in a string word and 
# returns the true if the word is a palindrome, false otherwise.

def is_palindrome(word):
    # reversing a string using slice notation
    if word == word[::-1]:
        # print output using string formatting
        print("The word %s is a palindrome" % word)
    else:
        print("The word %s is not a palindrome" % word)


is_palindrome("mother")
is_palindrome("dad")


# method 2
def is_palindrome():

    pal_word = input("Enter the word and see if it is palindrome: ")

    if pal_word == pal_word[::-1]:
     print("This word is palindrome")
    else:
        print("This word is not palindrome")


is_palindrome()


# Goodbye
# Write a method goodbye(name) 
# that takes in a string name
# and returns a string saying bye to that name. See the example calls.

def goodbye(name):
   print("Bye " + name)


goodbye("precious")
goodbye("mpho")
goodbye("lovie")

# Doubler
# Write a method doubler(numbers) that 
# takes an array of numbers and returns a new array
# where every element of the original array 
# is multiplied by 2.

def doubler():
   numbers = [1, 2, 3, 4, 5]
   doubled_numbers = []

   for n in numbers:
    new_number = n * 2
    doubled_numbers.append(new_number)

   print(doubled_numbers)


doubler()

# Write a method average_of_three(num1, num2, num3) 
# that returns the average of three numbers

def average_of_three(num1, num2, num3):

    sum_total = int(num1) + int(num2) + int(num3)
    average = sum_total / 3
    # print output using string formatting
    print("The average of %d, %d, %d is %d " % (num1, num2, num3, average))
    return average


average_of_three(58, 2, 8)

# Fizz Buzz
# Write a method fizz_buzz(max)
# that takes in a number max and returns an array
# containing all numbers greater than 0 and less than max
# that are divisible by either 4 or 6, but not both.


def fizz_buzz(max):
    result = []

    for n in range(1, max):
       if (n % 4 == 0 or n % 6 == 0) and not(n % 4 == 0 and n % 6 == 0):
           result.append(n)
    return result


print(fizz_buzz(25))
