#!/usr/bin/python3
'''
godzilla vs king kong
'''


class Node:
    '''
    Docstring for Node
    '''
    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if value is not None and not isinstance(value, (Node)):
            print(f"{type(value)}")
            raise TypeError("next_node must be a Node object")
        self.__next_node = value

    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    def list(self):
        str_list = f"{self.data}\n"
        if self.next_node is not None:
            next_val = self.next_node.list()
            str_list += f"{next_val}"
        return str_list

    def insert(self, value):
        print(f"type: {type(self.next_node)}")
        if self.next_node is None:
            self.next_node = Node(value)
        elif self.next_node.data >= value:
            self.next_node = Node(value, self.next_node)
        else:
            self.next_node.insert(value)


class SinglyLinkedList:
    '''
    Docstring for SinglyLinkedList
    '''
    __head = None

    def __init__(self):
        pass

    def __str__(self):
        if self.__head is None:
            return ""
        return self.__head.list()

    def sorted_insert(self, value):
        if self.__head is None:
            self.__head = Node(value)
        elif self.__head.data > value:
            self.__head = Node(value, self.__head)
        else:
            self.__head.insert(value)
