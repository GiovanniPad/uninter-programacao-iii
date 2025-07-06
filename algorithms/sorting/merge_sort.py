#!/usr/bin/env python3


def merge_sort(data):
    if len(data) > 1:
        middle = len(data) // 2
        left = data[:middle]
        right = data[middle:]

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0
        while (len(left) > i) and (len(right) > j):
            if right[j] > left[i]:
                data[k] = left[i]
                i += 1
            else:
                data[k] = right[j]
                j += 1
            k += 1

        while len(left) > i:
            data[k] = left[i]
            i += 1
            k += 1
        while len(right) > j:
            data[k] = right[j]
            j += 1
            k += 1


data = [7, 19, 30, 64, 1, 0, 74, 98, 99, 7]
merge_sort(data)
print(data)
