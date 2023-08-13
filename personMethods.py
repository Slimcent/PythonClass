def full_name(person):
    return f"{person.first_name} {person.last_name}"


def greet(person):
    return f"Hello, my name is {full_name(person)} and I'm {person.age} years old."
