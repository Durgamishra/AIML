# Fuctions in python
a function is a reusable block of code that performs a particular tasks

```
    Input: 10 and 20

    Function: add() used to perform calculations

    Output: 30
```

# Arguements and Parameter 
arguements are the value that are passed to the function.
and parameters are the variable that holds values or arguements 

```
def greet(name):
    print("Hello", name)

greet("durga")
```

# Positional arguements
valuesa are assigned according to their position 
```
def add(a, b):
    print(a + b)

add(10, 20)
```

# Keyword arguments

Values are passed using parameter names.
```
def introduce(name, age):
    print(name, age)

introduce(age=20, name="Durga")
```

```
Default arguement
def greet(name="Student"):
    print("Hello", name)

greet()
greet("Durga")
```