#!/usr/bin/env python3


def quick_sort(data, start, end):
    if start < end:
        partition_position = partition(data, start, end)
        quick_sort(data, start, partition_position - 1)
        quick_sort(data, partition_position + 1, end)


def partition(data, start, end):
    pivot = data[start]
    left = start + 1
    right = end
    flag = False

    while not flag:
        while left <= right and data[left] <= pivot:
            left += 1
        while data[right] >= pivot and right >= left:
            right -= 1

        if right < left:
            flag = True
        else:
            temp = data[left]
            data[left] = data[right]
            data[right] = temp
    temp = data[start]
    data[start] = data[right]
    data[right] = temp
    return right


def quick_sort_alternative(data):
    if len(data) < 2:
        return data
    else:
        pivot = data[0]
        smallers = [i for i in data[1:] if i <= pivot]
        greatests = [i for i in data[1:] if i > pivot]
        return (
            quick_sort_alternative(smallers)
            + [pivot]
            + quick_sort_alternative(greatests)
        )


data = [31, 19, 30, 64, 1, 0, 74, 15, 99, 7]
quick_sort(data, 0, len(data) - 1)
print(data)

# print(quick_sort_alternative(data))
