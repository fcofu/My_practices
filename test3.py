numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

squared_evens = []
for each_number in numbers:
    if each_number % 2 == 0:
        squared_evens.append(each_number ** 2)

print(squared_evens)




numbers2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

squared_evens2 = list(map(lambda x: x**2, filter(lambda x: x % 2 == 0, numbers2)))

print(squared_evens2)




numbers3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

squared_evens3 = [w**2 for w in numbers3 if w % 2 == 0]

print(squared_evens3)  # [4, 16, 36, 64, 100]