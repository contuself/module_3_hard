data_structure = [ 
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
] #по условию
def calculate_structure_sum(*args): #функция
    sum = 0 #сумматор
    for item in args: #цикл где будем проходиться по значениям
        if isinstance(item, (list, tuple, set)): #условие, если значение относиться к струтуре данных то
             sum += calculate_structure_sum(*item) #применяем рукрсионный вызов
        elif isinstance(item, dict): #если словарь
            for key, value in item.items(): #цикл где передаём значения
                sum += calculate_structure_sum(key) + calculate_structure_sum(value) #значения суммируем
        elif isinstance(item, str): #если строчка, то просто считаем длину
            sum += len(item) #добавляем к сумме
        elif isinstance(item, int): #если целочисленное
            sum += item #добавляем к сумме
    return sum #вернуть сумму всех значений
result = calculate_structure_sum(*data_structure) #переменная с вызовом функции
print(result) #вывод результата на экран
