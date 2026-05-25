"""
    allocate atleast 1 candy to each kid such that, kids with higher ratings get more candy, return
    the total minimum number that would satisfy this condition
"""
def allocate_candy(ratings: list[int]) -> int:
    n = len(ratings)
    candy = [1] * n

    for i in range(1, len(ratings)):
        if ratings[i] > ratings[i - 1]:
            candy[i] = candy[i - 1]  + 1



    for i in range(n - 2, -1, -1):
        if ratings[i] > ratings[i + 1]:
            candy[i] = candy[i + 1] + 1


    return sum(candy)




print(allocate_candy([1,2,2]))

