# QUESTION-FOUR

# ............................................SOLUTION......................................................


#......................................Implementing undoable list......................................................

# Imported the ABCMeta library
from abc import ABCMeta, abstractmethod

# I created a class named ListOpertaion
class ListOperation(object):
    __metaclass__ = ABCMeta

    # Class constructor
    def __init__(self, list_, item):
        self.list_ = list_
        self.item = item

    @abstractmethod
    def __call__(self):
        # When the class object is created then codes that are in __call__ method are going to be executed
        return

    @abstractmethod
    def undo(self):
        """Also, that class will have an undo method that will return something when called"""
        return

# The following class of Insert has inherited the abstract class that I have defined above.

class Insert(ListOperation):
    def __call__(self):
        self.list_.append(self.item)
        self.list_.sort()

    def undo(self):
        self.list_.remove(self.item)
        self.list_.sort()


class Delete(ListOperation):
    def __call__(self):
        self.deleted = False
        if self.item in self.list_:
            self.list_.remove(self.item)
            self.list_.sort()
            self.deleted = True

    def undo(self):
        if self.deleted:
            self.list_.append(self.item)
            self.list_.sort()


""" Creating the class of the UndoableList that will do all that id required. It's constructor is composed of two stacks 
that will store undo commands and the ones of the redo commands."""

# Created a class for undoableList
class UndoableList(object):
    def __init__(self):
        """ The constructor of undoableList object"""
        self.undo_commands = []
        self.redo_commands = []

    def push_undo_command(self, command):
        """ Push the given command to the undo_commands stack."""
        self.undo_commands.append(command)

    def pop_undo_command(self):
        """ Removes the last command from the undo_commands stack and return it. If the command stack is empty, we will
        the user that nothing to undo. """
        try:
            last_undo_command = self.undo_commands.pop()
        except IndexError:
            return "Nothing to undo"
        return last_undo_command

    def push_redo_command(self, command):
        """ Pushes the given command to the redo_commands stack."""
        self.redo_commands.append(command)

    def pop_redo_command(self):
        """ Removes the last command from the redo command stack and return it. If the command stack is empty, then we
        tell the user that there is nothing redo. """
        try:
            last_redo_command = self.redo_commands.pop()
        except IndexError:
            return "Nothing to redo"

        return last_redo_command

    def do(self, command):
        """ It accepts the given command and executes it. """
        command()
        self.push_undo_command(command)
        # clear the redo stack when a new command is executed to avoid it have the oldest edits to redo
        self.redo_commands[:] = []

    def undo(self):
        """Undo the last command. But first we checked if the undo_commands stack has nothing to undo. If there is, then
        call a method that pops out the command from the undo_commands stack. After we append the undone command in the
        redo stack."""
        if len(self.undo_commands) != 0:
            command = self.pop_undo_command()
            command.undo()
            self.push_redo_command(command)
        else:
            print('Nothing to undo')

    def redo(self):
        """Redo the last. Again we check if the redo_commands stack is not empty. If it contains some commands then we
        call the function that pops out the last command of the redo stack. If the stack was empty, then we tell the
        user that there is nothing to redo"""
        if len(self.redo_commands) != 0:
            command = self.pop_redo_command()
            command()
            self.push_undo_command(command)
        else:
            print('Nothing to redo')


# We will test the program using some examples

my_List = [2, 5, 7]
print(f'\nMy_List: {my_List}\n')
L = UndoableList()

L.do(Insert(my_List, 6))
print(f'After insert(6): {my_List}\n')

L.do(Delete(my_List, 5))
print(f'After delete(5): {my_List}\n')

L.undo()
print(f'After undo: {my_List}\n')

L.undo()
print(f'After undo: {my_List}\n')

L.redo()
print(f'After redo: {my_List}\n')

L.do(Insert(my_List, 4))
print(f'After insert(4): {my_List}\n')

L.redo()
print(f'After redo: {my_List}\n')

L.do(Delete(my_List, 3))
print(f'After delete(3): {my_List}\n')

L.undo()
print(f'After undo: {my_List}\n')

L.undo()
print(f'After undo: {my_List}\n')

L.undo()
print(f'After undo: {my_List}\n')

L.redo()
print(f'After redo: {my_List}\n')

L.redo()
print(f'After redo: {my_List}\n')

# ...................................................THANK YOU........................................................