# Exercise 1: (score : 1) Write a Python program to read a file and display its contents
# from random import sample
file1=open("C:\\Users\\user\\PycharmProjects\\entri_d41_python_project\\assignment.txt",'r')
print(file1.read())

# Exercise 2: (score : 1) Write a Python program to copy the contents of one file to another file
source_filename = input("Enter the source file name:")
destination_filename = input("Enter the destination file name:")
try:
    source_file = open(source_filename, 'r')
    destination_file = open(destination_filename, 'w')
    contents = source_file.read()
    destination_file.write(contents)
    source_file.close()
    destination_file.close()
    print(f"Contents of '{source_filename}' have been successfully copied to '{destination_filename}'.")
except FileNotFoundError:
    print(f"Error: The file '{source_filename}' does not exist.")
except Exception as e:
    print(f"An error occurred: {e}")

# Exercise 3: (score : 2) Write a Python program to read the content of a file and count the total
# number of words in that file.
file2=open("sample.txt",'r')
content=file2.read()
words=content.split()
word_count=len(words)
print('Content of the file: ',content)
print('Total words= ',len(content))


# Exercise 4: (score : 1) Write a Python program that prompts the user to input a string and
# converts it to an integer. Use try-except blocks to handle any exceptions that might occur
a=input("the string which is to be converted to int")
try:
    b=int(a)
    print(b,"the string converted to integer")
except ValueError:
    print("This string cannot be converted to integer")
except Exception as e:
    print("This string cannot be converted to integer:",e)


# Exercise 5: (score : 1) Write a Python program that prompts the user to input a list of
# integers and raises an exception if any of the integers in the list are negative.
try:
    numbers = input("Enter a list of integers separated by spaces: ").split()
    integers = [int(num) for num in numbers]
    for num in integers:
        if num < 0:
            raise ValueError(f"Negative number detected: {num}")
    print("All numbers are positive. The entered list is:", integers)
except ValueError as e:
    print("Error:", e)

# Exercise 6: (score : 2) Write a Python program that prompts the user to input a list ofintegers and computes
# the average of those integers. Use try-except blocks to handle any exceptions that might occur.
# use the finally clause to print a message indicating that the program has finished running.
user_input=input("Enter a list of integers:")
numbers = list(map(int, user_input.split()))
try:
    Number_of_words=len(numbers)
    print(Number_of_words)
    if len(numbers) == 0:
        raise ValueError("The list cannot be empty.")
    average = sum(numbers) / len(numbers)
    print(f"The average of the integers is: {average}")
except ValueError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

finally:
    print("The program has finished running.")

# Exercise 7 : (score : 2) Write a Python program that prompts the user to input a filename
# and writes a string to that file. Use try-except blocks to handle any exceptions that might
# occur and print a welcome message if there is no exception occurred.
file_name=input("Enter the file name:")
new_string=input("enter a string to the file:")
try:
    with open(file_name, "w") as file_name:
        file_name.write(new_string)

    print("File written successfully!","welcome to the world of programming")
except Exception as e:
    # Handle any exceptions and print an error message
    print("An error occurred:", e)