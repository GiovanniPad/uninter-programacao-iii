#!/usr/bin/env python3

def bubble_sort(data):
    data_len = len(data)
    count = 0
    while count < len(data):
        for i in range(0, data_len - 1, 1):
            if data[i] > data[i + 1]:
                aux = data[i]
                data[i] = data[i + 1]
                data[i + 1] = aux
        count += 1

data = [7, 19, 30, 64, 1, 0, 74, 98, 99, 7]
bubble_sort(data)
print(data)