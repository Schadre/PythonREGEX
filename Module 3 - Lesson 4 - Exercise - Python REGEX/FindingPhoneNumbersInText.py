import re 

text = "Contact us at 123-456-7890"
match = re.search(r"\d{3}-\d{3}-\d{4}", text)
if match:
    print("Phone number found:", match.group())