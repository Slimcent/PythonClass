from person import Person
from personMethods import full_name, greet


def run():
    # Create instances of the Person class
    person1 = Person("Alice", "Johnson", 30)
    person2 = Person("Bob", "Smith", 25)

    print(full_name(person1))
    print(greet(person2))
