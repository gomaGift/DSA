def getMaxSubarrayLen(team_a, team_b):
    n = len(team_a)                     # = len(team_b)

    def can_form(length):
        if length == 0:
            return True
        prev = float('-inf')
        for i in range(length):
            cand = []
            if team_a[i] >= prev:
                cand.append(team_a[i])
            if team_b[i] >= prev:
                cand.append(team_b[i])
            if not cand:
                return False
            prev = min(cand)            # smallest feasible choice
        return True

    # binary search
    lo, hi = 0, n
    while lo <= hi:
        mid = (lo + hi + 1) // 2
        if can_form(mid):
            lo = mid + 1
        else:
            hi = mid - 1
    return lo

log = "Y Y N"
log = log.split()

aggregate_log = """
    BEGIN Y Y N Y END
    garbage text here
    BEGIN N N Y Y Y N END
"""


print("**2424242424242".split("*"))