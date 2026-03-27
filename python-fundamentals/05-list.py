numbers = [1, 2, 3, 4, 5]
letters = ["a", "b", "c"]
mix = [2, "z", True, [1, 3, 5], 3.4, 2, 3, 2]

shopping_cart = ["Laptop", "Silla Gamer", "Café"]

print(type(mix))

# append - agregar
numbers.append(6)
print(numbers)

# remove
numbers.remove(4)
print(numbers)

# count - cuenta cuantas veces aparece algo en la lista
print("el numero 2 aparece : " ,mix.count(2) ," veces")
