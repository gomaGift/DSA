def min_candies(kids_ratings: list[int]):
    total_candies = [1] * len(kids_ratings)

    for i in range(1, len(kids_ratings)):
        if kids_ratings[i] > kids_ratings[ i- 1]:
            total_candies[i] += 1


    for i in range(len(kids_ratings) - 2, -1, -1):
        if kids_ratings[i] > kids_ratings[ i + 1]:
            total_candies[i] += 1

    return sum(total_candies)


print(min_candies([1,3,7,1]))


