class Person:
    def __init__(self, name, age):  # lo primero que se ejecuta
        self.name = name
        self.age = age  # atributos de instancia

    def work(self):  # fn de instancia
        return f"{self.name} esta trabajando duro."


person1 = Person("Eliana", 21)
person2 = Person("Alejo", 24)

print(person1.work())
print(person2.work())
print(person2.age, person2.name)