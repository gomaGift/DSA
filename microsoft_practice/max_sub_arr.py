def get_max_subarray_len(team_a, team_b):
    n = len(team_a)
    dp_a = dp_b = 1  # longest strong subarray ending at i if we pick from team_a or team_b
    res = 1
    for i in range(1, n):
        new_dp_a = new_dp_b = 1  # reset for current index

        # If we choose team_a[i]
        if team_a[i] >= team_a[i - 1]:
            new_dp_a = max(new_dp_a, dp_a + 1)
        if team_a[i] >= team_b[i - 1]:
            new_dp_a = max(new_dp_a, dp_b + 1)

        # If we choose team_b[i]
        if team_b[i] >= team_a[i - 1]:
            new_dp_b = max(new_dp_b, dp_a + 1)
        if team_b[i] >= team_b[i - 1]:
            new_dp_b = max(new_dp_b, dp_b + 1)

        dp_a, dp_b = new_dp_a, new_dp_b
        res = max(res, dp_a, dp_b)

    #     this is like the simplest approach i can have, you remember i was thinking about having a_count and b count
    # but there is a need for an index to track where we are innit

    return res
print(get_max_subarray_len([5,2], [2, 3]))