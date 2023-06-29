#!/usr/bin/python3

# 100-singly_linked_list.py
"""creates a class NOde that defines a node of a
singly linked list by data and next node"""


class Node:
    """defining a class called Node"""

    def __init__(self, data, next_node=None):
        """initializing the class with data and next_node"""
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        """retrives the data"""
        return self.__data

    @data.setter
    def data(self, value):
        """sets the data"""
        if not isinstance(value, int):
            raise TypeError('data must be an integer')
        self.__data = value

    @property
    def next_node(self):
        """retrieves the next node"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """sets the next_node"""
        if not isinstance(value, Node) and value is not None:
            raise TypeError('next_node must be a Node object')
        self.__next_node = value


class SinglyLinkedList:
    """defines a class called SinglyLinkedList"""
    def __init__(self):
        """initializes the list"""
        self.__head = None

    def sorted_insert(self, value):
        """sorts the list"""
        newNode = Node(value)
        if not self.__head:
            self.__head = newNode
        elif self.__head.data > value:
            newNode.next_node = self.__head
            self.__head = newNode
        else:
            temp = self.__head
            while temp.next_node is not None and temp.next_node.data < value:
                temp = temp.next_node
            newNode.next_node = temp.next_node
            temp.next_node = newNode

    def __str__(self):
        """make list printable"""
        temp = self.__head
        link = ""
        while temp:
            link += str(temp.data) + "\n"
            temp = temp.next_node
        return link
