# The first part of the research on multithreading

## Some theory

### Process

In computing, a **process** is an instance of a computer program that is being executed. Any process has 3 basic components:

- An executable program.
- The associated data needed by the program (variables, work space, buffers, etc.)
- The execution context of the program (State of process)

### Thread

A **thread** is an entity within a process that can be scheduled for execution. Also, it is the smallest unit of processing that can be performed in an OS (Operating System). In simple words, a **thread** is a sequence of such instructions within a program that can be executed independently of other code. For simplicity, you can assume that a thread is simply a subset of a process! A thread contains all this information in a **Thread Control Block (TCB)**:

- **Thread Identifier:** Unique id (TID) is assigned to every new thread
- **Stack pointer:** Points to thread’s stack in the process. Stack contains the local variables under thread’s scope.
- **Program counter:** a register which stores the address of the instruction currently being executed by thread.
- **Thread state:** can be running, ready, waiting, start or done.
- **Thread’s register set:** registers assigned to thread for computations.
- **Parent process Pointer:** A pointer to the Process control block (PCB) of the process that the thread lives on.

**Multi-threading:** Multiple threads can exist within one process where:

- Each thread contains its own **register set** and **local variables (stored in stack)**.
- All threads of a process share **global variables (stored in heap)** and the **program code**.

**Multithreading** is defined as the ability of a processor to execute multiple threads concurrently.

> In a simple, single-core CPU, it is achieved using frequent switching between threads. This is termed as context switching. In context switching, the state of a thread is saved and state of another thread is loaded whenever any interrupt (due to I/O or manually set) takes place. Context switching takes place so frequently that all the threads appear to be running parallels (this is termed as multitasking).

## Some results

### multithreading_s1_e1.py

As a result of the execution of the file [multithreading_s1_e1.py](multithreading_s1_e1.py) we will get:

```
» python multithreading_s1_e1.py
Square for 10: 100
Square for 20: 400
Square for 30: 900
Square for 40: 1600
Cube for 10: 1000
Cube for 20: 8000
Cube for 30: 27000
Cube for 40: 64000
Done!
```

The execution result will be the same in most cases because the square operation is faster than the cube operation.

### multithreading_s1_e2.py

As a result of the execution of the file [multithreading_s1_e2.py](multithreading_s1_e2.py) we will get:

```
» python multithreading_s1_e2.py
ID of process running main program: 13238
Main thread name: MainThread
Task 1 assigned to thread: t1
ID of process running task 1: 13238
Task 2 assigned to thread: t2
ID of process running task 2: 13238
Task 3 assigned to thread: t3
ID of process running task 3: 13238
```

In this case, the process IDs will be different for your system and for each run, but it will be the same for all threads because all threads run inside the same process.
