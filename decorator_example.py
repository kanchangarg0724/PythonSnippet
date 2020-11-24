# ================== One way of calling decorators ============================= #


def decorate_message(fun):  # Decorator accepts a function as an argument
    # Inner function
    def addWelcome(message):  # Value of text argument in display function will copy here
        return "Welcome to " + fun(message)

    # Decorator returns a function
    return addWelcome


@decorate_message
def display(text):
    return text


print(str(display("Python")))

# ================== Other way of calling decorators ============================= #


def decorate_function(fun):  # Decorator accepts a function as an argument
    # Inner function
    def swap(x,y):  # Value of a and b arguments in div function will copy here
        if x < y:
            x,y = y,x
        return fun(x,y)

    # Decorator returns a function
    return swap


def div(a,b):
    return a/b

# You can also add @decorate_function before the definition as well
div1 = decorate_function(div)

print(div1(2,4))
