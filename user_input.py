# user_input.py

# Ask the user for their name
name = input("What is your name? ")

# Ask the user for their age
age = input("How old are you? ")

# Ask the user for their location
location = input("Where do you live? ")

# Create a personalized message
message = f"Hello {name}, you are {age} years old and live in {location}."

# Print out the personalized message
print(message)

# Create another Python file with the personalized message
with open('generated_message.py', 'w') as file:
    file.write("# generated_message.py\n\n")
    file.write(f'print("{message}")\n')

print("A new file 'generated_message.py' has been created with the personalized message.")
