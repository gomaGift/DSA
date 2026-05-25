"""
Store Closing Time Penalty

Problem Description
We own a store that records, hour by hour, whether there were customers shopping. Each hour is marked with a single letter:
'Y' if there were customers during that hour
'N' if the store was empty during that hour

Example log for 4 hours:

hour: | 1 | 2 | 3 | 4 |
log:  | Y | Y | N | Y |
Here, there were customers for hours 1, 2, and 4, and no customers in hour 3.
We want to analyze when we should have closed the store to minimize wasted hours. The closing time is expressed as an integer from 0 to n:

0 → never open at all

n → open the entire day

Closing time is measured in hours from the start of the day:

hour:         | 1 | 2 | 3 | 4 |
closing_time: 0  1  2  3  4
Penalty Definition

For a given closing_time, define penalty as:
+1 for every hour we were open with no customers (unnecessary open time)
+1 for every hour we were closed with customers present (lost opportunity)

Part 1: Compute Penalty

Write a function:
def compute_penalty(log: str, closing_time: int) -> int:
    ...
where:

log is a space-separated string of 'Y' / 'N'

closing_time is an integer between 0 and len(log)

Return the total penalty.

Part 2: Find Best Closing Time

Write a function:

def find_best_closing_time(log: str) -> int:
    ...
that returns the closing time that yields the minimum penalty (using compute_penalty). If multiple closing times yield the same minimum penalty, return the smallest closing time.

Part 3: Aggregate Logs

Sometimes, employees record multiple days’ logs in one file. Valid logs are sequences that start with BEGIN, followed by zero or more 'Y' / 'N', and end with END.
 There can be extra garbage text or unfinished logs, which must be ignored.

Rules:

Valid logs cannot be nested (no BEGIN ... BEGIN ... END inside).

Valid logs can span multiple lines.

There may be multiple valid logs per line.

Write a function:

def get_best_closing_times(aggregate_log: str) -> list[int]:
    ...
that:

Parses the aggregate log string

Extracts all valid logs in order

Returns an array of best closing times (using Part 2 for each valid log)
"""
import re


def compute_penalty(log: str, closing_time: int) -> int:

    log = log.split()
    penalty = 0
    for i in range(closing_time):
         if log[i] == 'N':
             penalty += 1

    for i in range(closing_time, len(log)):
        if log[i] == 'Y':
            penalty += 1

    return penalty


def find_best_closing_time(log: str) -> int:
    log_list = log.split()
    n = len(log_list)

    best_time = 0
    min_penalty = float('inf')

    for closing_time in range(n + 1):
        penalty = compute_penalty(log, closing_time)
        if penalty < min_penalty:
            min_penalty = penalty
            best_time = closing_time

    return best_time


# print(find_best_closing_time("Y Y N Y N"))       # → 2
# print(find_best_closing_time("N N Y Y Y N"))     # → 2
# print(find_best_closing_time("N N N N"))         # → 0
# print(find_best_closing_time("Y Y Y Y"))         # → 4

log = "N N Y Y Y N"
closing_time = 4


# print(compute_penalty(log, closing_time))
def get_best_closing_times(aggregate_log: str) -> list[int]:
    pattern = r'BEGIN\b(.*?)\bEND'
    matches = re.findall(pattern, aggregate_log, flags=re.DOTALL)

    results = []

    for match in matches:
        # skip if nested BEGIN (invalid)
        if 'BEGIN' in match:
            continue


        # extract Y/N only (ignore junk)
        tokens = re.findall(r'\b[YN]\b', match)
        if not tokens:
            continue

        log = ' '.join(tokens)

        best = find_best_closing_time(log)
        results.append(best)

    return results

aggregate_log = """
BEGIN Y Y N Y END
garbage text
BEGIN N N Y Y
 Y N END
BEGIN Y BEGIN N END END  # nested → invalid
BEGIN Y END
"""

# print(get_best_closing_times(aggregate_log))

import re

def get_best_closing_times(aggregate_log: str) -> list[int]:
    """
    Extracts valid BEGIN...END logs and returns their best closing times.
    Skips:
      - Nested BEGINs
      - Unmatched BEGIN/END
      - Empty or garbage logs
    """
    results = []
    tokens = aggregate_log.split()

    i = 0
    n = len(tokens)

    while i < n:
        if tokens[i] == "BEGIN":
            j = i + 1
            nest = 0
            while j < n:
                if tokens[j] == "BEGIN":
                    # nested BEGIN → invalid block, skip
                    nest += 1
                elif tokens[j] == "END":
                    if nest == 0:
                        break
                    else:
                        nest -= 1
                j += 1

            # no matching END found → skip
            if j >= n or tokens[j] != "END":
                i += 1
                continue

            # extract Y/N within range
            block = tokens[i+1:j]
            ys_ns = [t for t in block if t in ("Y", "N")]

            if ys_ns:  # only process non-empty logs
                log = " ".join(ys_ns)
                best = find_best_closing_time(log)
                results.append(best)

            i = j + 1  # move pointer past END
        else:
            i += 1

    return results
aggregate_log = """
BEGIN Y Y N Y END
garbage text here
BEGIN N N Y Y Y N END
BEGIN Y BEGIN N END END   # nested → invalid
BEGIN Y                   # unclosed → invalid
END                       # stray END → ignored
"""

print(get_best_closing_times(aggregate_log))



