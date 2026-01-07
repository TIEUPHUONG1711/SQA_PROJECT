   # check NULL, duplicateimport pandas as pd
import re

def check_null(df, columns):
    for col in columns:
        if df[col].isnull().any():
            return False, f"NULL found in column: {col}"
    return True, "No NULL values"

def check_duplicate(df, column):
    if df[column].duplicated().any():
        return False, f"Duplicate found in column: {column}"
    return True, "No duplicates"

def check_email_format(df, column):
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    for email in df[column].dropna():
        if not re.match(pattern, email):
            return False, f"Invalid email format: {email}"
    return True, "Email format valid"
