# while True:
#     print("No se detiene lol")
counter = 1

while counter <= 5:
    print(f"Number: {counter}")
    counter += 1
else:
    print("------fin")


response = ""

while response.lower() != "bye":
    response = input("escribe 'bye' para salir: ")
else:
    print("Fin")

while response.upper() != "HELP":
    pass
