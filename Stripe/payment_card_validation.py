"""
Stripe Payment Card Validation System
Background

Stripe processes billions of dollars through various payment methods. To ensure payment security, card numbers must be validated before processing.

This system requires:
Network detection (VISA, MASTERCARD, AMEX).
Luhn algorithm validation.
Handling of redacted and corrupted card inputs.

Card Networks
VISA: 16 digits, starts with 4.
MASTERCARD: 16 digits, starts with 51–55.
AMEX: 15 digits, starts with 34 or 37.

Luhn Algorithm
From the rightmost digit (excluding the check digit), double every second digit.
If a doubled digit > 9, subtract 9.
Sum all digits.
If sum % 10 == 0, the card is valid.

Example
Card: 4532015112830366
Step 1: Double every 2nd from right → 8 5 6 2 0 1 1 1 2 2 7 3 0 3 3 6
Step 2: Sum = 50
Step 3: 50 % 10 = 0 → Valid

Part 1: Basic Visa Validation (Test Cases 1–5)

Input: 16-digit number starting with 4.
Output:
"VISA" if checksum passes.
"INVALID_CHECKSUM" if checksum fails.
Examples

Input: 4532015112830366 → Output: VISA
Input: 4242424242424243 → Output: INVALID_CHECKSUM

Part 2: Multi-Network Validation (Test Cases 6–10)
Input: 15- or 16-digit card number.
Output:

Network name (VISA / MASTERCARD / AMEX) if valid.
"INVALID_CHECKSUM" if checksum fails.
"UNKNOWN_NETWORK" if length or prefix does not match any known network.

Examples
Input: 5482334509943 → Output: UNKNOWN_NETWORK (13 digits)
Input: 4425233430109994 → Output: VISA
Input: 562523343010901 → Output: UNKNOWN_NETWORK (prefix 56)

Part 3: Redacted Cards (Test Cases 11–15)
Input: A card number containing * (1–5 digits redacted).
Output: Count of valid cards per network, sorted alphabetically by network.
Examples
Input: 4242424242424*42 → Output: VISA,1
Input: 3*8282246310005 → Output: AMEX,2
Input: **2424242424242 → Output:MASTERCARD,5 VISA,10


Part 4: Corrupted Cards (Test Cases 16–20)
Input: A card ending with ?, meaning exactly one error occurred:
One digit may have been changed.
Two adjacent digits may have been swapped.
Output: All possible valid original cards, in ascending numeric order.

Format:
card_number,NETWORK
Example
Input: 4344555566660004?
Output (partial):
4342555566660004,VISA
4344555566660004,VISA
4344555566660014,VISA
...
Implementation Notes
Output strings must match exactly.
Sort results numerically for Part 4.
Sort results alphabetically by network for Part 3.
Handle edge cases: wrong lengths, invalid prefixes.
Optimize for large search spaces.

"""
from itertools import product, repeat

from websocket import continuous_frame

card_patterns = {
    "VISA": {
        "prefix": ["4"],
        "len": 16
    },
    "MASTERCARD": {
        "prefix": ["51", "52", "53", "54", "55"],
        "len": 16
    },

    "AMEX": {
        "prefix": ["34", "37"],
        "len": 15
    }
}

def detect_card(card_number: str):
    for network, info, in card_patterns.items():
        if len(card_number) == info["len"] and any(card_number.startswith(p) for p in info["prefix"]):
            return network
    return None

def valid_luhn(candidate:str):
    card_digits = [int(d) for d in candidate]
    total = 0
    for i, d in enumerate(reversed(card_digits)):
        if i % 2 == 1:
            double = d*2
            if double > 9:
                double -= 9
            total += double
        else:
            total += d

    return total % 10 == 0


def payment_validation(card_number):

    # get the star positions
    star_positions = [i for i, ch in enumerate(card_number) if ch == '*']
    network_count  = {network: 0 for network in card_patterns}
    fill_digits = "0123456789"

    for combination in product(fill_digits, repeat = len(star_positions)):
        lst = list(card_number)
        for pos, digit in zip(star_positions, combination):
            lst[pos] = digit
        candidate = "".join(lst)

        if not candidate.isdigit():
            continue

        network = detect_card(candidate)
        if network is not None:
            if valid_luhn(candidate):
                network_count[network] += 1


    non_zero = [[k, v] for k, v in sorted(network_count.items()) if v > 0]
    print(" Matches " + " ".join(f"{k},{v}" for k,v in non_zero))



def part_4(card_number:str):
    if not card_number.endswith("?"):
        raise ValueError("card number must end in ? to indicate exactly one value corruption")
    card_number = card_number[:-1]
    network_count = {network: set() for network in card_patterns}
    digit_fills = "0123456789"
    candidates = []
    for i in range(len(card_number)):
        original = card_number[i]
        for d in digit_fills:
            if d == original:
                continue
            candidate = card_number[:i] + d + card_number[i+1: ]
            candidates.append(candidate)

    # now we need to swap two adjacent digits
    for i in range(len(card_number) - 1):
        lst = list(card_number)
        if lst[i] == lst[i+1]:
            continue
        lst[i], lst[i+1] = lst[i+1], lst[i]
        candidates.append("".join(lst))


    for candidate in candidates:
        network = detect_card(candidate)
        if network is not None:
            if valid_luhn(candidate):
                network_count[network].add(candidate)


    for network, cards in network_count.items():
        for card in sorted(cards):
            print(f"{card},{network}")


part_4("4344555566660004?")
# payment_validation("34*****46310005")




