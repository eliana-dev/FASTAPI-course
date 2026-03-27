class Person:
    species = "Humano"

    def __init__(self, name, age):  # lo primero que se ejecuta
        self.name = name
        self.age = age  # atributos de instancia
        self._energy = 100  # protegido
        self.__password = "1234"  # privado - error

    def work(self):  # fn de instancia
        return f"{self.name} esta trabajando duro."

    def _waste_energy(self, quantity):  # protegido
        self._energy -= quantity
        return self._energy

    def __generate_password(self):
        return f"$${self.name}{self.age}"

person1 = Person("Eliana", 21)
person2 = Person("Alejo", 24)

print(person1.work())
print(person2.work())
print(person1._waste_energy(10))
# print(person1.__password)
print(person1._Person__password)
print(person1._Person__generate_password())
# usa metodos para acceder a atributos privados y protegidos, evita acceder directamente