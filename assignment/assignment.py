''' Print statement outlining rules for your application'''
system_username = "admin"  # System username for authentication
system_password = "password"  # System password for authentication
print(system_username)
print(system_password)

''' Initialize your variables 

We will need 2 variables to capture the username and password. Another 2 variables to use as the system username and password to authenticate against when we register
'''
while True:
    # Get user input for username and password
    user_username = input("Enter your username: ")
    user_password = input("Enter your password: ")
    # Check if the user input matches the system username and password
    

''' A List to handle error messages '''

error_messages = [""]

''' Start your while loop '''
try:
        number = float(user_input)
        print(f"Square of {number} is {number ** 2}")
except ValueError:
        print("Invalid input. Please enter a valid number or 'exit'.")

''' Get your username and password'''
try:
        number = float(user_input)
        print(f"Square of {number} is {number ** 2}")
except ValueError:
        print("Invalid input. Please enter a valid number or 'exit'.")

''' Test your username and enforce logic'''


''' Test your password and enforce logic'''



''' If we pass, congratulate the user and immediately ask them to register'''
if valid_credentials(user_username, user_password):
        print("Congratulations! You're registered.")
        
else:
        print("Invalid credentials. Please try again.")



''' If they input the correct matching info, program complete. If incorrect, send the user all the way back to the beginning of the loop to start from scratch. '''

def valid_credentials(username, password):
    # Implement your validation rules here
    # Return True if valid, otherwise return False
    # You can also add error messages to the list if needed
    return len(username) >= 6 and any(c.isupper() for c in password) and any(c.isdigit() for c in password)


import getpass

# Prompt for username (non-sensitive input)
username = input("Enter your username: ")

# Prompt for password (sensitive input)
password = getpass.getpass("Enter your password: ")
