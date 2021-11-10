def binary_search(sortedList, item):
    low = 0
    high = len(sortedList)-1
    while low <= high:
        mid = (low+high) // 2
        guess = sortedList[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None


my_list = [1, 3, 4, 7, 9]
print(binary_search(my_list, 3))  # 1

print(binary_search(my_list, -1))  # None
