# Things you should be able to do.

number_list = [-5, 6, 4, 8, 15, 16, 23, 42, 2, 7]
num_list = [ 6, 1, 4, 8, 15, 16, 23, 42, 2, 7]
word_list = [ "What", "about", "the", "Spam", "sausage", "spam", "spam", "bacon", "spam", "tomato", "and", "spam"]

# Write a function that takes a list of numbers and returns a new list with only the odd numbers.
def all_odd(number_list):
    odds = [number for number in number_list if number % 2 != 0]
    return odds

print all_odd(number_list)  

# Write a function that takes a list of numbers and returns a new list with only the even numbers.
def all_even(number_list):
    even = [number for number in number_list if number % 2 == 0]
    return even

print all_even(number_list)

# Write a function that takes a list of strings and return a new list with all strings of length 4 or greater.
def long_words(word_list):
    list_of_long_words = [lw for lw in word_list if len(lw) >= 4]
    return list_of_long_words

print long_words(word_list)


# Write a function that finds the smallest element in a list of integers and returns it.
def smallest(number_list):
    smallest_so_far = number_list[0]
    for number in number_list:
        if number < smallest_so_far:
            smallest_so_far = number
    return smallest_so_far

print smallest(number_list)
print smallest(num_list)

# Write a function that finds the largest element in a list of integers and returns it.
def largest(number_list):
    return None

# Write a function that takes a list of numbers and returns a new list of all those numbers divided by two.
def halvesies(number_list):
    return []

# Write a function that takes a list of words and returns a list of all the lengths of those words.
def word_lengths(word_list):
    return []

# Write a function (using iteration) that sums all the numbers in a list.
def sum_numbers(number_list):
    return 0

# Write a function that multiplies all the numbers in a list together.
def mult_numbers(number_list):
    return 0

# Write a function that joins all the strings in a list together (without using the join method) and returns a single string.
def join_strings(word_list):
    return ""

# Write a function that takes a list of integers and returns the average (without using the avg method)
def average(number_list):
    return 0

