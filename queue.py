# -*- coding: UTF_8 -*-

class Queue:

    def __init__(self, l=[]):
        """
        An object which implement the queue logic from a list.

        :param l: The base list to use with this queue
        :type l: list object that is empty by default.
        """
        self.list = l

    def push(self, e):
        """
        Push the param at the end of the queue.

        :param e: The element to insert in the queue.
        """
        self.list.append(e)

    def pull(self):
        # TODO: need to implement as FIFO or LIFO
        return

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
