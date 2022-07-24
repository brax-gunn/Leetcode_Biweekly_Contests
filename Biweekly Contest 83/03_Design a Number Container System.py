from sortedcontainers import SortedList

class NumberContainers:

    def __init__(self):
        self.__index = {}
        self.__number = {}


    def change(self, index: int, number: int) -> None:
        if index in self.__index:
            indexValue = self.__index[index]
            self.__number[indexValue].remove(index)
        
        self.__index[index] = number
        
        if number not in self.__number:
            self.__number[number] = SortedList()
        
        self.__number[number].add(index)


    def find(self, number: int) -> int:
        if number in self.__number and len(self.__number[number]) > 0:
            return self.__number[number][0]
        return -1