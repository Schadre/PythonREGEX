import re

username = "@user123"
if re.match(r"@\w+", username):
    print("Valid username format")
else:
    print("Invalid username format")