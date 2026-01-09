numbers = [4, 7, 2, 9, 5, 12, 15]


new_list = [num for num in numbers if num > 5]

if new_list:
    average = sum(new_list) / len(new_list)
else:
    average = 0


print("tal fra kugleramme:", new_list)
print("list, og midten:", average)