# -*- coding: UTF_8 -*-

from queue import Queue

if __name__ == "__main__":
    names = [
        "Arnaud",
        "Barbara",
        "David",
        "Luc",
        "Romane"
    ]

    print("Test FIFO")

    fifo = Queue(names)

    print(fifo)

    print(fifo.pull())
    print(fifo.pull())

    print(fifo)

    print ("\nTest LIFO")

    lifo = Queue(names, Queue.LIFO)

    lifo.push("Quentin")
    print(lifo)

    print(lifo.pull())

    print(lifo)
