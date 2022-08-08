#!/usr/bin/python3

"""
Base class testing module
"""

import unittest
import json
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class Test_base(unittest.TestCase):
    """Base class"""
    def test_instance(self):
        """testing isinstance"""
        x = Base(1)
        self.assertIsInstance(x, Base)
    def test_id(self):
        """Testing base instances"""
        # creating instances
        base1 = Base()
        self.assertEqual(base1.id, 1)

        base2 = Base()
        self.assertEqual(base2.id, 2)
        
        base3 = Base()
        self.assertEqual(base3.id, 3)
        self.assertEqual(base3.id, Base._Base__nb_objects)

        base4 = Base("id")
        self.assetEqual(base4.id, "id")

        base5 = Base(float('NaN'))
        self.assertNotEqual(base5.id, base5.id)
        
        base6 = Base(4.4)
        self.assertEqual(base6.id, 4.4)

    def test_to_json_string(self):
        """test to_json_string method"""
        # If the list is empty, return: "[]"
        Base._Base__nb_objects = 0
        r1 = Rectangle(5, 12, 3, 8)
        
        json_dict = Base.to_json_string([r1.to_dictionary()])
        self.assertEqual(type(json_dict), str)
        list_dict = json.loads(json_dict)
        list = [{"x": 2, "width": 10, "id": 1, "height": 7, "y": 8}]
        # to check for an expected result;
        self.assertEqual(list_dict, list)
    def test_from_json_string_diff_dataType(self):
        """test_from_json_string method for testing different datatypes"""
        with self.assertRaises(ValueError):
            Rectangle.from_json_string("x")
        with self.assertRaises(TypeError):
            Rectangle.from_json_string({1})
        with self.assertRaises(TypeError):
            Rectangle.from_json_string(False)
        with self.assertRaises(TypeError):
            Rectangle.from_json_string(True)
        with self.assertRaises(TypeError):
            Rectangle.from_json_string(12.9)
        with self.assertRaises(TypeError):
            Rectangle.from_json_string(8)
        with self.assertRaises(TypeError):
            Rectangle.from_json_string({'key': 1})
