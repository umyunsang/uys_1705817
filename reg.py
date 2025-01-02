import re

pattern = r"\b\d{2,3}-\d{3,4}-\d{4}\b"
str_list = ["hello", "010-1234-5678", "02-123-4567", "010-hellow", "123-456"]

for s in str_list:
    if re.fullmatch(pattern, s):
        print(f"'{s}' is a valid phone number.")
    else:
        print(f"'{s}' is not a phone number.")

