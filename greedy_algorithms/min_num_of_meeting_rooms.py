

def min_number_of_meeting_rooms(intervals: list[list[int]]) -> int:

        data = []
        for s, e in intervals:
            data.append((s, 1))
            data.append((e, -1))
        data.sort()

        print(data)
        cur = rooms = 0

        for _, val in data:
            cur+= val
            rooms = max(cur, rooms)
        return rooms


#  this was smart thinking fam
print(min_number_of_meeting_rooms([[5,10],[15,20], [0,30]]))
