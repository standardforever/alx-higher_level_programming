#!/usr/bin/python3

import importlib_metadata


import turtle
import json
import csv


# from models.rectangle import Rectangle
"""
Base class
"""


class Base:
    """
    Base class for out Classes
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Instantiate the Base"""
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """convert python dict to json"""
        if (list_dictionaries is None):
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """write json string representation of list_objs to file"""
        filename = cls.__name__ + ".json"
        x = []
        if list_objs is not None:
            for i in list_objs:
                x.append(cls.to_dictionary(i))
        with open(filename, 'w') as f:
            f.write(cls.to_json_string(x))

    @staticmethod
    def from_json_string(json_string):
        """It returns the list of json string representation"""
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""
        if cls.__name__ == "Rectangle":
            clas = cls(1, 1)
        elif cls.__name__ == "Square":
            clas = cls(1)
        clas.update(**dictionary)
        return clas

    @classmethod
    def load_from_file(cls):
        """It returns a list of instance"""
        filename = cls.__name__ + ".json"
        lis = []
        try:
            with open(filename, "r") as f:
                lis = cls.from_json_string(f.read())
            for i in range(len(lis)):
                lis[i] = cls.create(**lis[i])
        except:
            pass
        return lis

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """returns an instance with all attributes already set"""
        filename = cls.__name__ + ".csv"
        with open(filename, "w", newline='') as f:
            write = csv.writer(f)
            if cls.__name__ == "Rectangle":
                for obj in list_objs:
                    write.writerow([obj.id, obj.width, obj.height,
                    obj.x, obj.y])
            elif cls.__name__ == "Square":
                for obj in list_objs:
                    write.writerow([obj.id, obj.size, obj.x, obj.y])
    @classmethod
    def load_from_file_csv(cls):
        """serializes a list of Rectangles/Squares in csv"""
        filename = cls.__name__ + ".csv"
        l = []
        try:
            with open(filename, 'r') as f:
                read = csv.reader(f)
                for args in read:
                    if cls.__name__ == "Rectangle":
                        dictionary = {"id": int(args[0]),
                                    "width": int(args[1]),
                                    "height": int(args[2]),
                                    "x": int(args[3]),
                                    "y": int(args[4])
                            }
                    elif cls.__name__ == "Square":
                        dictionary = {"id": int(args[0]), "size": int(args[1]),
                                    "x": int(args[2]), "y": int(args[3])}
                    obj = cls.create(**dictionary)
                    l.append(obj)
        except:
            pass
        return l

    
    @staticmethod
    def draw(list_rectangles, list_squares):
        """opens a window and draws all the Rectangles and Squares"""
        screen_width = 620
        padding = 10
        row_width = padding
        row_height = 0
        screen_height = padding
        color_list = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo',
                      'violet']
        color_size = len(color_list)
        color_index = 0
        for rect in list_rectangles:
            potential_width = row_width + rect.width + rect.x + padding
            if (row_width == padding or potential_width < screen_width):
                row_width += rect.width + rect.x + padding
                if (row_height < rect.height + rect.y):
                    row_height = rect.height + rect.y
            else:
                screen_height += row_height + padding
                row_width = rect.width + rect.x + padding * 2
                row_height = rect.height + rect.y

        for square in list_squares:
            potential_width = row_width + square.size + square.x + padding
            if (row_width == padding or potential_width < screen_width):
                row_width += square.size + square.x + padding
                if (row_height < square.size + square.y):
                    row_height = square.size + square.y
            else:
                screen_height += row_height + padding
                row_width = square.size + square.x + padding * 2
                row_height = square.size + square.y
        turtle.screensize(canvwidth=screen_width, canvheight=screen_height)
        turtle.pu()
        turtle.left(180)
        turtle.forward(screen_width/2 - padding)
        turtle.right(90)
        turtle.forward(screen_height/2 - padding)
        turtle.right(90)
        row_width = padding
        row_height = 0
        for rect in list_rectangles:
            potential_width = row_width + rect.width + rect.x + padding
            if (row_width == padding or potential_width < screen_width):
                row_width += rect.width + rect.x + padding
                if (row_height < rect.height + rect.y):
                    row_height = rect.height + rect.y
            else:
                turtle.pu()
                turtle.left(180)
                turtle.forward(row_width - padding)
                turtle.left(90)
                turtle.forward(row_height + padding)
                turtle.left(90)
                row_width = rect.width + rect.x + padding * 2
                row_height = rect.height + rect.y
            turtle.pd()
            turtle.pencolor(color_list[color_index % color_size])
            for _ in range(4):
                turtle.forward(5)
                turtle.back(5)
                turtle.right(90)
            turtle.pu()
            turtle.forward(rect.x)
            turtle.right(90)
            turtle.forward(rect.y)
            turtle.left(90)
            turtle.pd()
            turtle.pencolor('black')
            turtle.fillcolor(color_list[color_index % color_size])
            turtle.begin_fill()
            for _ in range(2):
                turtle.forward(rect.width)
                turtle.right(90)
                turtle.forward(rect.height)
                turtle.right(90)
            turtle.end_fill()
            color_index += 1
            turtle.pu()
            turtle.forward(rect.width + padding)
            turtle.left(90)
            turtle.forward(rect.y)
            turtle.right(90)

        for square in list_squares:
            potential_width = row_width + square.size + square.x + padding
            if (row_width == padding or potential_width < screen_width):
                row_width += square.size + square.x + padding
                if (row_height < square.size):
                    row_height = square.size + square.y
            else:
                turtle.pu()
                turtle.left(180)
                turtle.forward(row_width - padding)
                turtle.left(90)
                turtle.forward(row_height + padding)
                turtle.left(90)
                row_width = square.size + square.x + padding * 2
                row_height = square.size + square.y
            turtle.pd()
            turtle.pencolor(color_list[color_index % color_size])
            for _ in range(4):
                turtle.forward(5)
                turtle.back(5)
                turtle.right(90)
            turtle.pu()
            turtle.forward(square.x)
            turtle.right(90)
            turtle.forward(square.y)
            turtle.left(90)
            turtle.pd()
            turtle.pencolor('black')
            turtle.fillcolor(color_list[color_index % color_size])
            turtle.begin_fill()
            for _ in range(4):
                turtle.forward(square.size)
                turtle.right(90)
            turtle.end_fill()
            color_index += 1
            turtle.pu()
            turtle.forward(square.size + padding)
            turtle.left(90)
            turtle.forward(square.y)
            turtle.right(90)

        turtle.getscreen()._root.mainloop()

    