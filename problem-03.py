first = [1, 4, 6, 7, 9]
second = [2, 4, 5, 8, 9]

def only_unique(lst, lst2):
    result = []
    for val in lst:
        if not val in lst2:
            result.append(val)
    return result


unique_items = only_unique(first, second)