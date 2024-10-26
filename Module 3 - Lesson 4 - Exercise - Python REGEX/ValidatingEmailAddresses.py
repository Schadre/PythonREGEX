import re

email = "user@example.com"
if re.search(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}", email):
    print("Valid email address")
else:
    print("Invalid email address")