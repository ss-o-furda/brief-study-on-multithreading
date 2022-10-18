# Python program to illustrate the concept
# of threading
# To import the threading module, we do:
import threading


def print_cube(*args):
    # function to print cube of given numbers
    for arg in args:
        print(f"Cube for {arg}: {arg * arg * arg}")


def print_square(*args):
    # function to print square of given numbers
    for arg in args:
        print(f"Square for {arg}: {arg * arg}")


if __name__ == "__main__":
    """To create a new thread, we create an object of Thread class. 
    It takes following arguments:
        target: the function to be executed by thread
        args: the arguments to be passed to the target function
    """
    t1 = threading.Thread(target=print_square, args=(10, 20, 30, 40))
    t2 = threading.Thread(target=print_cube, args=(10, 20, 30, 40))

    # To start a thread, we use start method of Thread class:
    t1.start()
    t2.start()

    """Once the threads start, the current program (you can think of it like a main thread) 
    also keeps on executing. In order to stop execution of current program until 
    a thread is complete, we use join method.
    """
    t1.join()
    t2.join()

    # As a result, the current program will first wait for the completion of t1 and then t2.
    # Once, they are finished, the remaining statements of current program are executed.
    print("Done!")
