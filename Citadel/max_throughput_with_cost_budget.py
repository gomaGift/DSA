def maximize_throughput(throughputs, costs, budget):
    """
    Maximize the minimum throughput across all services within budget.

    Args:
        throughputs: List of initial throughputs for each service
        costs: List of scaling costs for each service
        budget: Maximum budget available

    Returns:
        Maximum achievable minimum throughput
    """
    n = len(throughputs)

    def can_achieve_throughput(target):
        """Check if we can achieve target throughput within budget"""
        total_cost = 0

        for i in range(n):
            # Calculate how many scales needed for service i to reach target
            if throughputs[i] >= target:
                # Already meets target, no scaling needed
                continue

            # Need to scale: throughputs[i] * (1 + k_i) >= target
            # So: k_i >= target / throughputs[i] - 1
            scales_needed = (target + throughputs[i] - 1) // throughputs[i] - 1

            # Cost for this service
            service_cost = scales_needed * costs[i]
            total_cost += service_cost

            # Early termination if budget exceeded
            if total_cost > budget:
                return False

        return total_cost <= budget

    # Binary search on the answer
    left = min(throughputs)  # Minimum possible throughput
    right = min(throughputs) + budget  # Upper bound estimate

    # Refine upper bound - maximum possible if we spend all budget on cheapest service
    if costs:
        max_possible_scales = budget // min(costs)
        right = min(throughputs) + max_possible_scales * max(throughputs)

    result = left

    while left <= right:
        mid = (left + right) // 2

        if can_achieve_throughput(mid):
            result = mid
            left = mid + 1
        else:
            right = mid - 1

    return result


def test_solution():
    """Test the solution with provided test cases"""
    test_cases = [
        {
            'throughputs': [4, 2, 7],
            'costs': [3, 5, 6],
            'budget': 32,
            'expected': 10
        },
        {
            'throughputs': [5],
            'costs': [1],
            'budget': 0,
            'expected': 5
        },
        {
            'throughputs': [3],
            'costs': [2],
            'budget': 10,
            'expected': 21
        },
        {
            'throughputs': [1, 10],
            'costs': [1, 100],
            'budget': 5,
            'expected': 6
        },
        {
            'throughputs': [2, 3],
            'costs': [4, 5],
            'budget': 100,
            'expected': 18
        },
        {
            'throughputs': [1, 2, 1],
            'costs': [10, 20, 10],
            'budget': 0,
            'expected': 1
        },
        {
            'throughputs': [100],
            'costs': [1],
            'budget': 0,
            'expected': 100
        }
    ]

    for i, test in enumerate(test_cases, 1):
        result = maximize_throughput(
            test['throughputs'],
            test['costs'],
            test['budget']
        )
        status = "✓" if result == test['expected'] else "✗"
        print(f"Test {i}: {status} Got {result}, Expected {test['expected']}")

        if result != test['expected']:
            print(f"  Input: throughputs={test['throughputs']}, costs={test['costs']}, budget={test['budget']}")


if __name__ == "__main__":
    print("Testing Binary Search Solution:")
    test_solution()

    print("\nExample walkthrough:")
    throughputs = [4, 2, 7]
    costs = [3, 5, 6]
    budget = 32
    result = maximize_throughput(throughputs, costs, budget)
    print(f"Input: throughputs={throughputs}, costs={costs}, budget={budget}")
    print(f"Maximum throughput: {result}")