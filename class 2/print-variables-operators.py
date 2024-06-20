# get input from user
email= input ("mostafa.qasimi28@gmail.com: ").strip()

# Test 1: It has a "." at the third-to-last index
dot_index= len (email) -3
has_dot=email[dot_index]=="."

# Test 2: It has exactly one "@" symbol, at the fifth-to-last index or earlier
at_index = len(email) - 5
has_at = email[at_index] == "@" and email.count("@") == 1

# Test 3: There is at least one character before the "@" symbol
before_at = email[:at_index].strip()

# Test 4: It doesn't have any spaces
no_spaces = " " not in email

# Final test with AND keyword
is_valid_email = has_dot and has_at and before_at and no_spaces

print(is_valid_email)
