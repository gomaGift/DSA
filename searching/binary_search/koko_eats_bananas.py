"""
Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.

Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile.
If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.

Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

Return the minimum integer k such that she can eat all the bananas within h hours.

Example 1:
Input: piles = [3,6,7,11], h = 8
Output: 4

Example 2:
Input: piles = [30,11,23,4,20], h = 5
Output: 30

Example 3:
Input: piles = [30,11,23,4,20], h = 6
Output: 23

Constraints:

    1 <= piles.length <= 104
    piles.length <= h <= 109
    1 <= piles[i] <= 109

"""
import math


def can_eat_n_bananas(eating_speed, bananas: list[int], eating_hours_limit ):
    eating_time = 0
    for pile in bananas:
        eating_time += math.ceil(float(pile)/eating_speed)

    return eating_time <= eating_hours_limit



def koko_eats_bananas(arr: list[int], eating_hours: int) -> int:

    min_eating_speed = min(arr)
    max_eating_spead = max(arr)

    res_eating_speed = eating_hours

    while min_eating_speed <= max_eating_spead:
        mid = (min_eating_speed + max_eating_spead)//2

        if can_eat_n_bananas(mid, arr, eating_hours):
            max_eating_spead = mid - 1
            res_eating_speed = mid

        else:
            min_eating_speed = mid + 1

    return res_eating_speed


if __name__ == "__main__":
    bananas = [int(num) for num in input("enter an array of piles of bananas: ").split()]
    max_eating_hours = int(input("enter max eating hours: "))
    res = koko_eats_bananas(bananas, max_eating_hours)
    print(res)


