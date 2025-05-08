def get_name():
    name = "Alice"
    return name

def greet():
    person = get_name()  # Call the function to get the variable
    print("Hello", person)

greet()