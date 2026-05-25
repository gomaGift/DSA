def day_of_week(day: str, k: int) -> str:
    # WRITE YOUR BRILLIANT CODE HERE
    days_arr = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    number_of_day = (days_arr.index(day) + k) % 7

    return days_arr[number_of_day]


if __name__ == "__main__":
    day = input()
    k = int(input())
    res = day_of_week(day, k)
    print(res)