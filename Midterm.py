#Q1
a = 16
a = a // 2
print(a**2)
a = a + 11
print(a+1)
a = a - 3
#q2
print((3+10**2/2) or 70.0)
#q3
import datetime

a = 7
b = 2
today = datetime.datetime.today()
day_of_week = today.weekday()
month_of_year = today.month
a = a + day_of_week
b += month_of_year

print(a)
print(b)
c = a + b
print(c)
d = "xyz" * (c // 3)
print(d)
#Q5
import re

def find_pattern(text):
    # This regex pattern looks for any word that starts with 'b' and ends with 'Bob'
    pattern = r'\bb[a-zA-Z]*Bob\b'
    # Find all matches in the text
    matches = re.findall(pattern, text)
    # Return the number of matches
    return len(matches)

# Example usage:
text_to_search = "bBob beagleBob notBob bobcatBob"
print(find_pattern(text_to_search))  # Output will be the count of matches
#Q6

# Create a list
my_list = [1, 2, 3]

# Add an element
my_list.append(4)
print(my_list)  # Output: [1, 2, 3, 4]

# Change an element
my_list[0] = 'a'
print(my_list)  # Output: ['a', 2, 3, 4]

# Remove an element
my_list.pop(1)
print(my_list)  # Output: ['a', 3, 4]

#q7
import random

random_numbers = []
for i in range(10):
    random_numbers.append(random.randint(1, 100))

# Using list comprehension to remove odd numbers and double the even numbers
random_numbers = [x * 2 for x in random_numbers if x % 2 == 0]

# Print the resulting list
print(random_numbers)
#q8

def is_valid_url(url):
    if not isinstance(url, str):
        return False  # Not a string

    # Check for the presence of scheme and domain
    if '://' in url:
        scheme, rest = url.split('://', 1)
        if '.' in rest:
            return True  # Simplistic check for a domain
    return False


# Examples of usage:
print(is_valid_url("https://www.example.com"))  # Should return True
print(is_valid_url("not-a-url"))  # Should return False
#q9
def calculate_full_days_since_birthday(birthday):
    # Split the birthday string into components
    day, month, year = map(int, birthday.split('.'))

    # Define the number of days in each month
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    # Calculate the number of full years since the birthday
    current_year = 2024
    full_years_since_birthday = current_year - year - 1

    # Calculate the total days from full years
    total_full_days = full_years_since_birthday * 365

    # Add extra days for leap years
    leap_years = (year + 1) // 4 - year // 100 + year // 400
    leap_years -= (current_year - 1) // 4 - (current_year - 1) // 100 + (current_year - 1) // 400
    total_full_days += leap_years

    return total_full_days


# Example usage
print(calculate_full_days_since_birthday("21.01.2003"))

#q5
def count_pattern(text):
    """
    This function counts the occurrences of a pattern that starts with 'b' and ends with 'Bob' in a given text.

    :param text: The text in which to search for the pattern.
    :return: The count of occurrences of the pattern.
    """
    count = 0
    # Splitting the text by spaces to get individual words
    words = text.split()

    # Iterating over each word in the text
    for word in words:
        # Checking if the word starts with 'b' and ends with 'Bob'
        if word.startswith('b') and word.endswith('Bob'):
            count += 1

    return count


# Example usage:
example_text = "b123Bob is talking to bAliceBob and b123456Bob"
print(count_pattern(example_text))  # Output should be the count of occurrences
#q4
def palindrome(word):
    return word == word[::-1]

numbers = [
    "659303660135934337466473349531066303956",
    "6593036601359343374664733439531066303956",
    "8025833559061079503003059701609553385208",
    "5485839837501070045005400701057389385845",
    "748961779749244646336564429497177169847",
    "7489617719749244646336564429479177169847"
]

# Use the function for each number
for number in numbers:
    if not palindrome(number):
        print(f"The number {number} is NOT a palindrome.")
