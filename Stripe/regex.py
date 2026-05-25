"""
🟢 Beginner Level

🟠 Intermediate Level

6️⃣ Match all Zambian phone numbers:
"0977-123456, 0955 987654, +260977111222"
👉 Pattern: (?:\+260|0)\d{3}[- ]?\d{6}

7️⃣ Extract all years between 1900–2099:
"Founded in 1964, reformed in 2002, vision 2100"
👉 Pattern: 19\d{2}|20\d{2}

8️⃣ Validate a simple username (letters, numbers, underscore, 3–15 chars):
👉 Pattern: ^[A-Za-z0-9_]{3,15}$

9️⃣ Remove all punctuation from:
"Hello, world! How's it going?"
👉 Pattern: [^A-Za-z0-9 ]

10️⃣ Find duplicate words (like “the the”):
"This is is a test test line"
👉 Pattern: \b(\w+)\s+\1\b
"""
import re


def regex_practice(string):
    """
      Find all digits in: My ID is 2025 and phone is 0977123456
👉   Pattern: \\d+
     """

    digits = re.findall(r'\d+', string)
    # print(digits)

    """
    2️⃣ Find all words in:
        "Hello, world! This is Python_3"
👉       Pattern: \\w+
    """
    words = re.findall(r'\w+', string)
    # print(words)

    """
        3️⃣ Match all email addresses in:
        "Contact us at info@unza.zm or support@zamtel.co.zm"
        # 👉 Pattern: [\w\.-]+@[\w\.-]+   
    """
    emails_matches = re.findall(r'[\w\.-]+@[\w\.-]+\.\w+', string)
    # print(emails_matches)


    """
    4️⃣ Replace all digits with #:
    "My number is 0977 123 456"
👉 Pattern: \d
    """
    replace_digits = re.sub(r'\d', '#', string)
    # print(replace_digits)

    """5️⃣ Match only words starting with a capital letter:
    "Python is fun, but Regex is Power!"
👉   Pattern: \b[A-Z][a-z]+\b"""

    capital_case = re.findall(r'\b[A-Z][a-z]+\b', string)
    print(capital_case)


# regex_practice("My ID is 2025 and phone is 0977123456")
# regex_practice("Hello, world! This is Python_3")
# regex_practice("Contact us at info@unza.zm or support@zamtel.co.zm")
regex_practice("Python is fun, but Regex is Power!")