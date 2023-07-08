waiting_list = ["sen", "ben", "john"]
waiting_list.sort()
sorted_waiting_list = sorted(waiting_list)

for i, name in enumerate(sorted_waiting_list):
    row = f"{i + 1}.{name.capitalize()}"
    print(row)