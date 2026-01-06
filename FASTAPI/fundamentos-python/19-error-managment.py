def divide_numbers():
    try:
        a = int(input("Ingresa el numerador: "))
        b = int(input("Ingresa el numerador: "))

        result = a / b
        print(result)
        return result
    except ValueError:
        print("Por favor ingresa solo numeros loc0000o")
    except ZeroDivisionError:
        print("No divide entre 0")
    except Exception as errorcito:
        print(type(errorcito))
    else: # se ejecuta si no hay fallos
        pass
    finally: # se ejecuta aunque falle o no
        print("gracias por usar la calculadora")

divide_numbers()
