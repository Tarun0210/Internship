#!/usr/bin/env python
# coding: utf-8

# # Problem 11

# In[13]:


def factorial(n):
   # Initialize the result to 1
   factorial_result = 1
   
   # Iterate from 1 to n and multiply each number to factorial_result
   for i in range(1, n+1):
       factorial_result *= i
       
   return factorial_result

# Example usage:
number = 5

print(f"The factorial of {number} is:", factorial (number))
   


# # Problem 12

# In[16]:


def is_prime(number):
    # Check if number is less than or equal to 1
    if number <=1:
        return false
    
    # check for factors from 2 to sqrt(number)
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
        
    return True

# Example usage:
num = 19

if is_prime(num):
    print(f"{num} is a prime number.")
else:
    print(f"{num} is a composite number.")
        


# # Problem 13

# In[19]:


def find_hypotenuse(side1, side2):
    # Calculate the hypotenuse using pythagoras theoram
    hypotenuse = (side1**2 + side2**2)**0.5
    return hypotenuse

# Example usage:
side1 = 3
side2 = 4

hypotenuse = find_hypotenuse(side1, side2)
print(f"The hypotenuse of the right_angled triangle with sides {side1} and {side2} is: {hypotenuse}")


# In[ ]:


# def is_palindrome(s):
    # Remove spaces and convert to lowecase
    s = s.replace(" ", "").lower()
    
    # Check if the string is equal to its reverse
    return s == s[::-1]

# Example usage:
input_string = "A man a plan a canal Panama"

if is_palindrome(input_string):
    print(f"The string '{input_string}' is a palindrome.")
else:
    print(f"The string '{input_string}' is not a palindrome.")


# In[20]:


def character_frequency(input_string):
    # Initialize an empty dictionary to store frequency of each character
    frequency = {}
    
    # Iterate through each character in the string
    for char in input_string:
        # Increment frequency count for each character
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    return frequency

# Example usage:
input_str = "Hello, World!"

# Calculate frequency of characters in the string
freq = character_frequency(input_str)

# Print the frequency of each character
print("character frequencies:")
for char, count in freq.items():
    if char.isprintable(): # Ensure to print only printable characters
        print(f" '{char}' -> {count}")


