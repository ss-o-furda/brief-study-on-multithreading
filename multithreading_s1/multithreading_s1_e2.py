# Python program to illustrate the concept
# of threading
# To import the threading module, we do:
import threading
# Also we will need os module, to use system features
import os


def task1():
    # We use the threading.current_thread() function to get the current thread object.
    print("Task 1 assigned to thread: {}".format(
        threading.current_thread().name))

    # We use os.getpid() function to get ID of current process.
    print("ID of process running task 1: {}".format(os.getpid()))


def task2():
    # We use the threading.current_thread() function to get the current thread object.
    print("Task 2 assigned to thread: {}".format(
        threading.current_thread().name))

    # We use os.getpid() function to get ID of current process.
    print("ID of process running task 2: {}".format(os.getpid()))


def task3():
    # We use the threading.current_thread() function to get the current thread object.
    print("Task 3 assigned to thread: {}".format(
        threading.current_thread().name))

    # We use os.getpid() function to get ID of current process.
    print("ID of process running task 3: {}".format(os.getpid()))


if __name__ == "__main__":

    # We use os.getpid() function to get ID of current process.
    print("ID of process running main program: {}".format(os.getpid()))

    """We use threading.main_thread() function to get the main thread object. 
    In normal conditions, the main thread is the thread from which 
    the Python interpreter was started. name attribute of thread object is used 
    to get the name of thread.
    """
    print("Main thread name: {}".format(threading.current_thread().name))

    # creating threads
    t1 = threading.Thread(target=task1, name='t1')
    t2 = threading.Thread(target=task2, name='t2')
    t3 = threading.Thread(target=task3, name='t3')

    # To start a thread, we use start method of Thread class:
    t1.start()
    t2.start()
    t3.start()

    """Once the threads start, the current program (you can think of it like a main thread) 
    also keeps on executing. In order to stop execution of current program until 
    a thread is complete, we use join method.
    """
    t1.join()
    t2.join()
    t3.join()
