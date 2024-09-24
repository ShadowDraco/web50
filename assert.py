# assert function is used to test if a function works

def square(x):
    return x + x

# manual testing 
print(square(10) == 100)

# use assert function to test
# Does not output anything if the assertion is true.
assert square(10) == 100 
