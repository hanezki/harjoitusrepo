class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def set_name(self, name):
        self.name = name

    def set_age(self, age):
        self.age = age

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age


def edit_person(person1, name, age):
    person.set_age(age)
    person.set_name(name)


def hello():
    return "Hello dev!"


if __name__ == "__main__":
    person = Person("hannu", 24)
    print(f"{person.name}, {person.age}")
    edit_person(person, "jyrki", "100")
    print(f"{person.name}, {person.age}")





