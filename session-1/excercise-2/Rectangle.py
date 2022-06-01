# Our code to be tested
class Rectangle:
    def __init__(self, width, length):
        self.width = width
        self.length = length

    def get_area(self):
        return self.width * self.length

# r = Rectangle(2, 3)

# print(r.get_area())


# -----------second phase--------------------------------
# class Rectangle:
#     def __init__(self, width, length):
#         if not isinstance(width, int) or not isinstance(length, int):
#             raise TypeError('Invalid Type Entered, Int type Expected')
#         if (isinstance(width, int) and width <= 0) or \
#            (isinstance(length, int) and length <= 0):
#             raise ValueError('Invalid Value Entered, Value greater than 0 Expected')
#         self.width = width
#         self.length = length

#     def get_area(self):
#         return self.width * self.length



# -----------third phase--------------------------------
# class Rectangle:
#     def __init__(self, width, length):
#         self.width = width
#         self.length = length

#     def get_area(self):
#         return self.width * self.length

#     @property
#     def width(self):
#         return self._width
    
#     @width.setter
#     def width(self, width):
#         if not isinstance(width, int):
#             raise TypeError('Invalid Type Entered, Int type Expected')
#         if isinstance(width, int) and width <= 0:
#             raise ValueError('Invalid Value Entered, Value greater than 0 Expected')
#         self._width = width

#     @property
#     def length(self):
#         return self._length
    
#     @length.setter
#     def length(self, length):
#         if not isinstance(length, int):
#             raise TypeError('Invalid Type Entered, Int type Expected')
#         if isinstance(length, int) and length <= 0:
#             raise ValueError('Invalid Value Entered, Value greater than 0 Expected')
#         self._length = length


