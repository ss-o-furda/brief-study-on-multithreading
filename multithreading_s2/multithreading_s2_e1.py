# Python program to illustrate the concept
# of threading with race condition
# To import the threading module, we do:
import threading

# global variable x
x = 0


def increment():
    """
    function to increment global variable x
    """
    global x
    x += 1


def thread_task():
    """
    task for thread
    calls increment function 100000 times.
    """
    for _ in range(100000):
        increment()


def main_task():
    global x
    # setting global variable x as 0
    x = 0

    """To create a new thread, we create an object of Thread class. 
     It takes following arguments:
         target: the function to be executed by thread
     """
    t1 = threading.Thread(target=thread_task)
    t2 = threading.Thread(target=thread_task)

    # To start a thread, we use start method of Thread class:
    t1.start()
    t2.start()

    """Once the threads start, the current program (you can think of it like a main thread) 
    also keeps on executing. In order to stop execution of current program until 
    a thread is complete, we use join method.
    """
    t1.join()
    t2.join()


if __name__ == "__main__":
    for i in range(10):
        main_task()
        print("Iteration {0}: x = {1}".format(i, x))
