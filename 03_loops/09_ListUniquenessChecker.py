item = ["apple", "banana", "orange", "apple", "mango"]
unique_set = set()
for item in item:
    if item in unique_set:
        print("Duplicate: ", item)
        break
    unique_set.add(item)