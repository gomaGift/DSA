"""
🧠 Problem Summary
You need to check if a company name is available or not available based on previous requests.
Names are considered the same if they match under these normalization rules:

Case-insensitive
Ignore suffixes: Inc., Corp., LLC, L.L.C.
Replace & and , with spaces
Ignore multiple spaces (treat as one)
Ignore leading The, An, A
Ignore and unless it’s at the beginning
Ignore punctuation and trim spaces
If the name becomes empty, it’s Not Available

"""
import re
from cgitb import reset

seen = set()
SUFFIXES = [" Inc.", "Corp.", "LLC", "L.L.C."]

def normalize(company_name: str):
    # case insensitive
    company_name = company_name.lower().strip()

    # Replace & and , with spaces
    company_name = company_name.replace("&", " ").replace(",", "")

    # ignore suffixes and remove trailing space
    for suffix in SUFFIXES:
        if company_name.endswith(suffix):
            company_name = company_name[:-len(suffix)].strip()

    # Ignore multiple spaces (treat as one)
    company_name = re.sub(r'\s+', ' ', company_name)

    # Ignore leading The, An, A
    company_name = re.sub(r'^(the|an|a)\s+', '', company_name)

    # Ignore and unless it’s at the beginning
    name_parts = company_name.split()
    filtered_parts = [p for i, p in enumerate(name_parts) if (p != "and" and i != 0)]
    company_name = " ".join(filtered_parts)

    # Ignore punctuation and trim spaces
    company_name = re.sub(r'[^a-z0-9 ]', "", company_name)

    return company_name




def check_availability(requests: list[str]):
     results = []
     for req in requests:
         # split by one to prevent multiple splits if name accidentally contains multiple pipes
         acc_id, proposed_name = req.split("|", 1)
         normalized = normalize(proposed_name)
         if normalized in seen:
             results.append(f'{acc_id}|Name Not Available')
         elif not normalized:
             results.append(f'{acc_id}|Name Not Available')
         else:
             results.append(f'{acc_id}|Name Available')
             seen.add(normalized)
