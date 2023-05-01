# Add a few lines of code to do something ONLY under your own
# function name.
# When you run this whole .py file, it should print out the names
# of all the functions and run them one at a time.

def roche():
    for _ in range(5):
        for space in range(10):
            print(" "*space, "@@@@")
        for i in reversed(range(10)):
            print(" "*i, ":-(")

def m250420():
    # YOUR CODE HERE!
    pass

def m250522():
    # YOUR CODE HERE!
    pass

def m250996():
    x = int(input('Gimme a number fool: '))
    for i in range (0,10000):
        if i < x:
            print('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
        else:
            print('0123456789')
    pass

def m251632():
    for x in range(1,20):
        print('Hola!','x'+str(x))
    pass

def m252016():
    # YOUR CODE HERE!
    pass

def m252310():
    # YOUR CODE HERE!
    pass

def m252994():
    # YOUR CODE HERE!
    pass

def m253036():
    # YOUR CODE HERE!
    pass

def m253120():
    # YOUR CODE HERE!
    pass

def m253306():
    # YOUR CODE HERE!
    pass

def m253384():
    for _ in range(2):
        for space in range(10):
            print(" "*space, "<3")
        for i in reversed(range(10)):
            print(" "*i, "</3")
    pass

def m254860():
    # YOUR CODE HERE!
    pass

def m254932():
    for x in range(1,100):
        print("Shai is Better than CP3")
    pass

def m255748():
    print("this is cool")
    pass


if __name__ == '__main__':
    import sys
    import inspect
    for fname, func in inspect.getmembers(sys.modules[__name__], inspect.isfunction):
        print(f'======== CALLING {fname}() ==========')
        func()
