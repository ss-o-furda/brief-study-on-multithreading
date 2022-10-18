# A brief study on multithreading

Research is based on articles [**Multithreading in Python | Set 1**](https://www.geeksforgeeks.org/multithreading-python-set-1/) and [**Multithreading in Python | Set 2 (Synchronization)**](https://www.geeksforgeeks.org/multithreading-in-python-set-2-synchronization/)

<br/>

## The first part

The first part of the study can be seen in the [The first part of the research on multithreading](multithreading_s1/README.md).

This describes a basic multi-threaded program that does not require access to the same data and can run in multi-threaded mode without any problems. And some theory about the concepts of process and thread.

**To run these files and verify the correctness of the programs yourself, you can use the following commands**:

### First program

on **macOS**/**linux**:

```
python3 multithreading_s1/multithreading_s1_e1.py
```

on **windows**:

```
python multithreading_s1/multithreading_s1_e1.py
```

### Second program

on **macOS**/**linux**:

```
python3 multithreading_s1/multithreading_s1_e2.py
```

on **windows**:

```
python multithreading_s1/multithreading_s1_e2.py
```

## The second part

The second part of the study can be seen in the [The second part of the research on multithreading](multithreading_s2/README.md).

Basic information about primitive synchronization is described here.

**To run these files and verify the correctness of the programs yourself, you can use the following commands**:

### First program

on **macOS**/**linux**:

```
python3 multithreading_s2/multithreading_s2_e1.py
```

on **windows**:

```
python multithreading_s2/multithreading_s2_e1.py
```

### Second program

on **macOS**/**linux**:

```
python3 multithreading_s2/multithreading_s2_e2.py
```

on **windows**:

```
python multithreading_s2/multithreading_s2_e2.py
```

## Conclusions

**Finally, here are a few advantages and disadvantages of multithreading**:

**Advantages**:

- It doesn’t block the user. This is because threads are independent of each other.
- Better use of system resources is possible since threads execute tasks parallels.
- Enhanced performance on multi-processor machines.
- Multi-threaded servers and interactive GUIs use multithreading exclusively.

**Disadvantages**:

- As number of threads increase, complexity increases.
- Synchronization of shared resources (objects, data) is necessary.
- It is difficult to debug, result is sometimes unpredictable.
- Potential deadlocks which leads to starvation, i.e. some threads may not be served with a bad design
- Constructing and synchronizing threads is CPU/memory intensive.
