def max_sub_array_with_strong_team(team_a, team_b):
    max_count = float('-inf')

    def dfs(team, index):
        nonlocal max_count
        if index >= len(team_b):
            return 0
        if team[0] < team[index]:

        a_sub_arr = dfs(team[0], team_a[index + 1:])
        b_sub_arr = dfs(team[0], team_b[index + 1:])
        max_count = max(max_count, 1 + max(a_sub_arr, b_sub_arr))
        return 1 + max_count(a_sub_arr, b_sub_arr)

    dfs(skill, index)