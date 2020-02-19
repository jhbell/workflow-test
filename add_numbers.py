# Add two numbers and return the result
def add(a, b):
    return a + b

def add_many(*values):
    result = 0
    for value in values:
        result = add(result, value)
    return result
