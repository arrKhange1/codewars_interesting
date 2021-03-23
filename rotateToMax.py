def max_rot(n):
    arr = list(str(n))
    max1 = n
    for i in range(len(arr)-1):
        k = i
        while (k < len(arr)-1):
            temp = arr[k]
            arr[k] = arr[k+1]
            arr[k+1] = temp
            k += 1
        if (int(''.join(arr)) >= max1):
            max1 = int(''.join(arr))
        print(arr)
    return max1
print(max_rot(56789))
