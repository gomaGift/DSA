from collections import defaultdict


def dispute_lifecycle_part1(file):
    seen = {}
    with open(file) as f:
        for x in f:
            x = x.strip()
            id, network, date, amount, reason = x.split(",")
            entry = {"transaction_id": id, "date": date, "amount": int(amount), "reason": reason}
            seen.setdefault(network, []).append(entry)
    return seen

def dispute_lifecycle_part2(file):
    transactions = {}
    with open(file) as f:
        for trans_line in f:
            trans_line = trans_line.strip()
            try:
              id, network, date, amount, reason = trans_line.split(",")
            except:
                continue
            entry = {"transaction_id": id, "date": date, "amount": int(amount), "reason": reason}
            transactions.setdefault(network, []).append(entry)

    return transactions

from collections import defaultdict

def dispute_lifecycle_part3(file):
    valid_trxns = defaultdict(dict)

    with open(file) as f:
        for line in f:
            line = line.strip()
            if not line:  # skip empty lines
                continue
            txn_id, network, date, amount, reason = line.split(",")
            amount = int(amount)

            # Check if transaction already exists
            if txn_id in valid_trxns[network]:
                # Remove transaction if either old or current reason is withdrawn
                if reason == "withdrawn" or valid_trxns[network][txn_id]["reason"] == "withdrawn":
                    del valid_trxns[network][txn_id]
                    continue

            # Add/update transaction
            valid_trxns[network][txn_id] = {
                "transaction_id": txn_id,
                "date": date,
                "amount": amount,
                "reason": reason
            }

    # Convert inner dicts to lists
    return {network: list(txns.values()) for network, txns in valid_trxns.items() if txns}


dispute_lifecycle_part3("part3")

def test_part3_withdrawn_multiple_networks(**kwargs):
    file1 = [
        "txn100,visa,2025-09-01,3000,unauthorized",
        "txn200,mastercard,2025-09-01,2500,duplicate_charge"
    ]
    file2 = {
  "visa": [
    {"transaction_id": "txn300", "date": "2025-09-03", "amount": 4000, "reason": "unauthorized"},
    {"transaction_id": "txn100", "date": "2025-09-01", "amount": 3000, "reason": "unauthorized"}
  ]
}
    expected1 = {
        "visa": [
            {"transaction_id": "txn100", "date": "2025-09-01", "amount": 3000, "reason": "unauthorized"},
            {"transaction_id": "txn300", "date": "2025-09-03", "amount": 4000, "reason": "unauthorized"}
        ]
    }
    expected2 = {

            "visa": [
                {"transaction_id": "txn100", "date": "2025-09-01", "amount": 3000, "reason": "unauthorized"}
            ],
            "amex": [
                {"transaction_id": "txn300", "date": "2025-09-02", "amount": 4000, "reason": "duplicate_charge"}
            ],
        "mastercard": [
            {"transaction_id": "txn500", "date": "2025-09-03", "amount": 2800, "reason": "duplicate_charge"}
        ]

    }

    res1 = dispute_lifecycle_part1(kwargs.get("info1"))
    res2 = dispute_lifecycle_part2(kwargs.get("info2"))
    res3 = dispute_lifecycle_part3(kwargs.get("part3"))
    print(res3)
    print(res1 == expected1)
    print(res3 == file2)
    print(res2 == expected2)

test_part3_withdrawn_multiple_networks(info1 ="info", info2="info2", part3="part3")


