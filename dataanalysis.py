import re

# Function to extract all email addresses (URLs) from the text
def extract_emails(text):
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    emails = re.findall(email_pattern, text)
    return emails

# Function to extract all phone numbers in the format (xxx) xxx-xxxx
def extract_phone_numbers(text):
    # Regular expression pattern for phone numbers in the format (xxx) xxx-xxxx
    phone_pattern = r'\(\d{3}\)\s\d{3}-\d{4}'
    phone_numbers = re.findall(phone_pattern, text)
    return phone_numbers

# Function to replace all occurrences of a word with another word
def replace_word(text, old_word, new_word):
    # Replacing the word using the re.sub function
    modified_text = re.sub(r'\b' + re.escape(old_word) + r'\b', new_word, text)
    return modified_text

# Test the functions
text_data = """
Here are some emails: python123@gmail.com.com, test.email@domain.org.
Contact me at (123) 456-7890 or (987) 654-3210.
The word 'bad' should be replaced by 'good' in the text.
"""

# Extract emails
emails = extract_emails(text_data)
print("Emails found:", emails)

# Extract phone numbers
phone_numbers = extract_phone_numbers(text_data)
print("Phone numbers found:", phone_numbers)

# Replace word 'bad' with 'good'
modified_text = replace_word(text_data, 'bad', 'good')
print("Modified text:", modified_text)
