"""
Catch Me If You Can - Fraud Detection
Background
Stripe processes billions of dollars worth of transactions every day. Our job is to protect customers and legitimate merchants by detecting
and blocking fraudulent transactions. We will build a simplified fraud detection model that marks merchants as fraudulent if too many of their
transactions are suspicious. The problem is split into three parts.

Part 1: Count-Based Fraud Detection
Each merchant has a Merchant Consumer Code (MCC) that represents their industry (e.g., retail, airline). Each MCC has an associated fraud threshold (integer > 1)
that indicates the maximum allowed number of fraudulent transactions before the merchant is marked as fraudulent.
We are given
A comma-separated list of non-fraudulent codes (e.g., "approved,invalid_pin,expired_card").
A comma-separated list of fraudulent codes (e.g., "do_not_honor,stolen_card,lost_card").
A table of MCCs with their fraud thresholds: MCC,threshold (one per line).
A table of merchants with their MCCs: account_id,MCC.
The minimum number of total transactions we must observe before evaluating a merchant (integer ≥ 0).

A table of charges: CHARGE,charge_id,account_id,amount,code

Output
Return a lexicographically sorted, comma-separated list of fraudulent merchants (by account_id).

Part 2: Percentage-Based Fraud Detection

Count-based thresholds can unfairly mark high-volume merchants as fraudulent. Instead, use a percentage threshold:

Each MCC now has a fraction between 0 and 1 indicating the maximum allowed fraction of fraudulent transactions.

If a merchant’s fraud percentage ≥ threshold, mark them as fraudulent.

Merchants stay fraudulent even if their fraud percentage later decreases.

Only evaluate merchants after seeing at least the minimum number of total transactions.

Inputs remain the same as Part 1, except the MCC table now contains fractions.

Part 3: Dispute Resolution

Sometimes transactions are incorrectly marked as fraudulent. We now support disputes which overturn the fraudulent status of a specific transaction.

Input now may include lines like: DISPUTE,charge_id

When a dispute is present, that transaction is treated as not fraudulent for all calculations.
If a merchant was marked fraudulent solely due to disputed transactions, they may return to non-fraudulent status until they cross
the threshold again with new transactions.
# this has to be done inline innit
"""


def detect_fraudulent_merchants_part_1(non_fraud_codes_str, fraud_codes_str, mcc_table, merchant_table, min_transactions,
                                charges):
    """
        Fraud Detection Engine for Stripe OA — Parts 1–3

        :param non_fraud_codes: comma-separated string of non-fraudulent codes
        :param fraud_codes: comma-separated string of fraudulent codes
        :param mcc_thresholds: dict of {MCC: threshold}, can be int (count) or float (fraction)
        :param merchant_mcc: dict of {account_id: MCC}
        :param min_transactions: minimum transactions before evaluating a merchant
        :param records: list of strings, each either a CHARGE or DISPUTE line
        :return: comma-separated string of fraudulent merchants (lexicographically sorted)
        """

    fraudulent_codes = set(fraud_codes_str)
    mcc_thresholds = {mcc: float(threshold) for mcc, threshold in (row.split(",") for row in mcc_table)}
    merchant_table = {acc_id: mcc for acc_id, mcc in (row.split(",") for row in merchant_table)}

    merchant_stats = {}
    charge_info = {}

    for transaction in charges:
        parts = transaction.strip().split(",")

        if parts[0] == "CHARGE":
            _, charge_id,acc_id,_,code = parts
            charge_info[charge_id] = {"acc_id": acc_id, "code": code} # i just want to add stuff to a map
            merchant_stats.setdefault(acc_id, {"total": 0, "fraudulent": 0})
            merchant_stats[acc_id]["total"] += 1
            if code in fraudulent_codes:
                merchant_stats[acc_id]["fraudulent"] += 1

        elif parts[0] == "DISPUTE":
            _, charge_id = parts
            if charge_id in charge_info:
                acc_id = charge_info[charge_id]["acc_id"]
                code = charge_info[charge_id]["code"]
                if code in fraudulent_codes:
                    merchant_stats[acc_id]["fraudulent"] -= 1
                    merchant_stats[acc_id]["dispute"] = True


    fraudulent_transactions = []
    for acc_id, stats in merchant_stats.items():
        total = stats["total"]
        if total < min_transactions:
            continue

        fraudulent = stats["fraudulent"]
        threshold = mcc_thresholds.get(merchant_table.get(acc_id))

        if isinstance(threshold, float):
            if total > 0 and (fraudulent/total) >= threshold:
                fraudulent_transactions.append(acc_id)

        elif fraudulent > threshold:
            fraudulent_transactions.append(acc_id)

    return ",".join(sorted(fraudulent_transactions))



