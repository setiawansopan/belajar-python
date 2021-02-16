def terbesar(arr):
    max = 0

    for i in range(1, len(arr)):
        if arr[i] > max:
            max = arr[i]
    return max

arr = [1,2,3,4,5,6,7,8,9,0]
print('nilai terbesar : ', terbesar(arr))
