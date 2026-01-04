# my_list = [1, 2, 3, 4, 5]
# addition = 0

# for number in my_list:
#     print(number)
#     addition += number

# print(addition)

# for number in list(range(100)): # no hay indice
#     print(number)

for index, number in enumerate(list(range(100))):  # no hay indice
    print(index, number*2)
