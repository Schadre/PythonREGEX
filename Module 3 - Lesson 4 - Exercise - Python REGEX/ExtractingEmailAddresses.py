import re
text = "Contact us at support@example.com or sales@example.com."
emails = re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}",text)
print(emails)