# Add a few lines of code to do something ONLY under your own
# function name.
# When you run this whole .py file, it should print out the names
# of all the functions and run them one at a time.

def m250072():
    # YOUR CODE HERE!
    d = 30
    print('1 + 1 =', str(d))
    pass

def m252130():
    x = 10
    for i in range(10):
        x += 1
    print(x)
    pass

def m252670():
    bennett = 10
    olivia = 5
    if bennett > olivia:
        print('Seems Accurate')
    # YOUR CODE HERE!
    pass

def m253762():
    donuts=0
    for i in range (1000):
        donuts+=1
        workout=0
    print('Aiden has eaten',donuts,"donuts....and worked out",workout,'times')

    pass

def m253828():
    # YOUR CODE HERE!
    pass

def m254542():
    # YOUR CODE HERE!
    pass

def m255172():
    # YOUR CODE HERE!
    pass

def m255514():
    # YOUR CODE HERE!
    pass

def m255994():
    # YOUR CODE HERE!
    pass

def m256168():
    # YOUR CODE HERE!
    pass

def m256258():
    # YOUR CODE HERE!
    pass

def m256264():
    print(".")
    pass

def m256294():
    # YOUR CODE HERE!
    pass

def m256354():
    # YOUR CODE HERE!
    pass

def m256774():
    # YOUR CODE HERE!
    pass


if __name__ == '__main__':
    import sys
    import inspect
    for fname, func in inspect.getmembers(sys.modules[__name__], inspect.isfunction):
        print(f'======== CALLING {fname}() ==========')
        func()
