def rotate_array(arr, k):
    k = k % len(arr)

    arr.reverse()
    arr[:k] = arr[:k][::-1]
    arr[k:] = arr[k:][::-1]
    return arr

print(rotate_array([1,2,3,4,5,6,7], 3))