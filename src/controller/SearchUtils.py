import re

def contains_text(string, pattern, case_sensitive=True):
    if case_sensitive:
        return pattern in string
    else:
        return pattern.lower() in string.lower()

def contains_regex(string, regex, case_sensitive=True):
    if case_sensitive:
        return re.search(regex, string)
    else:
        return re.search(regex, string, re.IGNORECASE)
