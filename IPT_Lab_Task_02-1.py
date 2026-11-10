# Task 1: Accept two numbers and display their sum, difference,
# product, and division.

# %%
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("Sum:", num1 + num2)
print("Difference:", num1 - num2)
print("Product:", num1 * num2)

if num2 != 0:
    print("Division:", num1 / num2)
else:
    print("Division: Cannot divide by zero")

# Output:
# Enter first number: 20
# Enter second number: 10
# Sum: 30.0
# Difference: 10.0
# Product: 200.0
# Division: 2.0


# %% [markdown]
# Task 2: Accept an image's width and height and calculate
# its total number of pixels.

# %%
width = int(input("Enter image width in pixels: "))
height = int(input("Enter image height in pixels: "))

total_pixels = width * height

print("Total Pixels:", total_pixels)

# Output:
# Enter image width in pixels: 100
# Enter image height in pixels: 100
# Total Pixels: 10000


# %% [markdown]
# Task 3: Accept an image's width and height and calculate
# its uncompressed grayscale size in kilobytes.
# A grayscale image with 8 bits per pixel uses approximately
# one byte per pixel. 1 KB = 1024 bytes.

# %%
width = int(input("Enter image width in pixels: "))
height = int(input("Enter image height in pixels: "))

total_pixels = width * height
size_bytes = total_pixels
size_kb = size_bytes / 1024

print("Total Pixels:", total_pixels)
print("Approximate Grayscale Image Size:", round(size_kb, 2), "KB")

# Output:
# Enter image width in pixels: 100
# Enter image height in pixels: 100
# Total Pixels: 10000
# Approximate Grayscale Image Size: 9.77 KB


# %% [markdown]
# Task 4: Accept a student's name, roll number, and marks in
# three subjects. Calculate and display the total and average marks.

# %%
name = input("Enter student name: ")
roll_number = input("Enter roll number: ")

subject1 = float(input("Enter marks in subject 1: "))
subject2 = float(input("Enter marks in subject 2: "))
subject3 = float(input("Enter marks in subject 3: "))

total_marks = subject1 + subject2 + subject3
average_marks = total_marks / 3

print("\n--- Student Result ---")
print("Name:", name)
print("Roll Number:", roll_number)
print("Total Marks:", total_marks)
print("Average Marks:", round(average_marks, 2))

# Output:
# Enter student name: Ali
# Enter roll number: 2024-CET-07
# Enter marks in subject 1: 80
# Enter marks in subject 2: 75
# Enter marks in subject 3: 85
#
# --- Student Result ---
# Name: Ali
# Roll Number: 2024-CET-07
# Total Marks: 240.0
# Average Marks: 80.0
