import re 

def validate_email(email):
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    if re.match(pattern, email):
        return True
    else:
        return False

def process_emails(email_list):
    valid_emails = []
    invalid_emails = []
    for email in email_list:
        try:
            if validate_email(email):
                valid_emails.append(email)
            else:
                invalid_emails.append(email)
        except Exception as e:
            print(f"Error processing email {email}: {e}")
    return valid_emails, invalid_emails

email_list = ["user@example.com", "invalid-email.com", "contact@company.org", "name@domain", "info@example.net"]

valid, invalid = process_emails(email_list)
print("Valid Emails:", valid)
print("Invalid Emails:", invalid)