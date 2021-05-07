"""Weird functions and decorators"""

def say_hello(name):
    return f"hello {name}"

def  be_cool(name):
    return f"yo {name}, togheter we are cool"

def greet_bob(greeter_func):
    return greeter_func("Bob")

if __name__ == "__main__":
    greet_bob(say_hello)
    greet_bob(be_cool)

