from collections import defaultdict

from collections import defaultdict

def compute_fraud_scores(transactions_list, rules_list, merchants_list):

    # Base merchant scores
    fraud_score = {m: int(s) for m, s in (x.split(",") for x in merchants_list)}

    # Parse rules
    parsed_rules = [{
        "min_amount": int(a),
        "mult": int(b),
        "add": int(c),
        "penalty": int(d),
    } for a, b, c, d in (r.split(",") for r in rules_list)]


    # merchant → customer → stats
    stats_map = defaultdict(lambda: defaultdict(lambda: {
        "count": 0,
        "rules": [],
        "hours": defaultdict(lambda: {"count": 0, "rules": []})
    }))

    # ===== PASS 1: MULTIPLICATIVE RULES & RECORD STATS =====
    for idx, entry in enumerate(transactions_list):
        merchant, amount, customer, hour = entry.split(",")
        amount = int(amount)
        hour = int(hour)
        rule = parsed_rules[idx]

        cust_stats = stats_map[merchant][customer]
        cust_stats["count"] += 1
        cust_stats["rules"].append(idx)

        hour_stats = cust_stats["hours"][hour]
        hour_stats["count"] += 1
        hour_stats["rules"].append(idx)

        # multiplicative rule
        if amount > rule["min_amount"]:
            fraud_score[merchant] *= rule["mult"]

    # ===== PASS 2: ADDITIVE + HOURLY RULES =====
    for merchant, customer_map in stats_map.items():
        for customer, cust_stats in customer_map.items():

            # apply add_factor for 3+ transactions
            if cust_stats["count"] >= 3:
                for idx in cust_stats["rules"]:
                    fraud_score[merchant] += parsed_rules[idx]["add"]

            # hourly penalties / bonuses
            for hour, hour_stats in cust_stats["hours"].items():
                if hour_stats["count"] >= 3:
                    for idx in hour_stats["rules"]:
                        rule = parsed_rules[idx]

                        if 12 <= hour <= 17:
                            fraud_score[merchant] += rule["penalty"]
                        elif 9 <= hour <= 11 or 18 <= hour <= 21:
                            fraud_score[merchant] -= rule["penalty"]

    # result
    return [[m, fraud_score[m]] for m in sorted(fraud_score)]


transactions = [
    "merchant1,1200,customer1,10",
    "merchant1,500,customer1,10",
    "merchant2,2400,customer1,15",
    "merchant1,800,customer1,16",
    "merchant1,1000,customer2,17",
    "merchant1,1400,customer1,10",
]

rules = [
    "1000,2,8,15",
    "1400,5,3,19",
    "2300,3,17,3",
    "1800,2,9,6",
    "1000,4,8,2",
    "1200,3,11,7",
]

merchants = [
    "merchant1,10",
    "merchant2,20",
]

print(compute_fraud_scores(transactions, rules, merchants))
