items = [1,2,3,4,5]

try:
    item = items[6]
    print(item)
except IndexError as e:
    print(e, "\nItem does not exist in the list")