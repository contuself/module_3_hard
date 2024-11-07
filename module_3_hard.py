data_structure = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]
def calculate_structure_sum(*args):
    sum = 0
    for item in args:
        if isinstance(item, (list, tuple, set)):
             sum += calculate_structure_sum(*item)
        elif isinstance(item, dict):
            for key, value in item.items():
                sum += calculate_structure_sum(key) + calculate_structure_sum(value)
        elif isinstance(item, str):
            sum += len(item)
        elif isinstance(item, int):
            sum += item
    return sum
result = calculate_structure_sum(*data_structure)
print(result)