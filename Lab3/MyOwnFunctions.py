'''
@Author: Ben Howell-Burke
Date: 10/15/2025
Project: MyOwnFunctions.py
'''

# 3. Function to create a list of numbers from 1 to 13.
def create_number_list():
    """
    Creates and returns a list of consecutive numbers from 1 to 13.
    Parameters: None
    Return: A list of integers.
    """
    return list(range(1, 14))

# 4. Function to sum all elements in a list.
def calculate_sum(num_list):
    """
    Calculates the sum of all numbers in a given list.
    Parameters: A list of numbers.
    Return: The sum (integer or float).
    """
    total = 0
    for number in num_list:
        total += number
    return total

# 5. Function to multiply all elements in a list.
def calculate_product(num_list):
    """
    Calculates the product of all numbers in a given list.
    Parameters: A list of numbers.
    Return: The product (integer or float).
    """
    # Start with 1, because multiplying by 0 would result in 0.
    product = 1
    for number in num_list:
        product *= number
    return product

# 6. Function to print all even numbers from a list.
def print_even_numbers(num_list):
    """
    Prints all the even numbers from a list on a single line.
    This function does not return any value.
    Parameters: A list of numbers.
    Return: None
    """
    for number in num_list:
        # Check if the number is perfectly divisible by 2
        if number % 2 == 0:
            print(number, end=" ")
    print() # Adds a final newline for clean formatting in the console

# 7. Main part of the script where functions are called.
if __name__ == "__main__":
    
    # Create the list by calling the function from step 3
    numbers = create_number_list()
    
    # Get the sum by calling the function from step 4
    list_sum = calculate_sum(numbers)
    
    # Get the product by calling the function from step 5
    list_product = calculate_product(numbers)
    
    # Print the generated list and the final results
    print(f"The generated list is: {numbers}")
    print(f"The sum of all elements is: {list_sum}")
    print(f"The product of all elements is: {list_product}")
    print() # Adding a blank line for better readability
    
    # Call the function from step 6 to print even numbers
    print("The even numbers in the list are:")
    print_even_numbers(numbers)