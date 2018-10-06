# -*- coding: UTF_8 -*-

class Queue:

    FIFO = 0
    LIFO = 1

    def __init__(self, l=[], t=FIFO):
        """
            An object which implement the queue logic from a list.

            :param l: The base list to use with this queue. The list is empty by default.
            :param t: The type of the queue FIFO or LIFO. FIFO by default
            :type l: list
            :type t: int
        """
        self.list = l
        self.__type = t

    def push(self, e):
        """
            Push the param at the end of the queue.

            :param e: The element to insert in the queue.
        """
        self.list.append(e)

    def pull(self):
        """
            Pull the element as the type of the queue

            :raise ValueError: If the queue type is not provided.
            :return: The element to pull as the logic of the queue
        """
        if self.__type == self.__class__.FIFO:
            return self.list.pop(0)
        elif self.__type == self.__class__LIFO:
            return self.list.pop(len(self.list) - 1)
        else:
            raise ValueError("The type must be set to FIFO or LIFO. See the documentation")
            return None

    def clear(self):
        """
            Clear the queue to be empty.
        """
        count = len(self.list)
        while count > 0:
            self.list.pop(0)
            count -= 1

    def is_empty(self):
        """
            Check if the queue is empty or not.

            :return: True if the queue is empty False otherwise
            :rtype: bool
        """
        return len(self.list) == 0
