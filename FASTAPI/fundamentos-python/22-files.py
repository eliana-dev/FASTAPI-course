try:
    with open("test.txt", mode="w") as my_file:
        text = my_file.write(":) ")

    with open("test.txt", mode="r") as my_file:
        print(my_file.readlines())

    with open("test.txt", mode="r+") as my_file:
        print(my_file.readlines())
        text = my_file.write("Hello word ")

    with open("test.txt", mode="a") as my_file: #append
        text = my_file.write("123 ")
        print(text) # posicion de la palabra
        
except FileNotFoundError:
    print("El archivo no existe")
except Exception as e:
    print(f"Ocurrio un error: {e}")
