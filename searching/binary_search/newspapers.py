"""
You have a stack of newspapers in a fixed order. Each newspaper has a read time. You want to assign all newspapers to a group of at most num_coworkers workers.
Each worker is assigned a consecutive section of newspapers from the stack, and all workers read their assigned sections in parallel.

The constraint: you cannot reorder newspapers. If you assign newspapers at positions 1, 2, 3 to worker A, you cannot then assign newspaper 2 to worker B.
Each worker gets a consecutive block from the original stack.

Find the minimum time needed to read all newspapers. Since workers read in parallel, the total time equals the time taken by the slowest worker.

For example, with newspapers [7,2,5,10,8] and 2 workers, you could assign [7,2,5] to worker A (14 minutes total) and [10,8] to worker B (18 minutes total). Worker B finishes last, so the answer is 18 minutes.
Constraints

1 <= newspapers_read_times.length <= 10^5

1 <= newspapers_read_times[i] <= 10^5

1 <= num_coworkers <= 10^5
Examples
Example 1:
Input: newspapers_read_times = [7,2,5,10,8], num_coworkers = 2
Output: 18
Explanation:

Assign first 3 newspapers to one coworker then assign the rest to another. The time it takes for the first 3 newspapers is 7 + 2 + 5 = 14 and for the last 2 is 10 + 8 = 18.
Example 2:
Input: newspapers_read_times = [2,3,5,7], num_coworkers = 3
Output: 7
Explanation:

Assign [2, 3], [5], and [7] separately to workers. The minimum time is 7.

this is an nlogn problem, we find the time limit with binary search but linear in traversal
"""


def assign_news_papers(total_workers:int, read_time: int, news_papers: list[int]) -> bool:
    used_time = news_papers[0]
    used_workers = 1

    for news_paper_read_time in news_papers[1:]:
        if used_time + news_paper_read_time <= read_time:
            used_time += news_paper_read_time

        else:
            used_workers += 1
            used_time = news_paper_read_time


    return used_workers <= total_workers


def min_newspaper_read_time(newspapers: list[int], num_workers: int):
    min_read_time = max(newspapers)
    max_read_time = sum(newspapers)

    res_min_read_time = max_read_time

    while min_read_time <= max_read_time:
        mid_read_time = (min_read_time + max_read_time) // 2

        if assign_news_papers(num_workers, mid_read_time, news_papers=newspapers):
            max_read_time = mid_read_time - 1
            res_min_read_time = mid_read_time
        else:
            min_read_time = mid_read_time + 1

    return res_min_read_time




if __name__ == "__main__":
    newspapers = [int(num) for num in input("enter newspaper read times: ").split()]
    num_workers = int(input("enter the the number of readers: "))
    min_read_time = min_newspaper_read_time(newspapers, num_workers)
    print(min_read_time)





