# 0x04. Python - More Data Structures: Set, Dictionary

0-square_matrix_simple.py -  a function that computes the square value of all integers of a matrix Prototype: def square_matrix_simple(matrix=[]):

1-search_replace.py - a function that replaces all occurrences of an element by another in a new list. Prototype: def search_replace(my_list, search, replace):

2-uniq_add.py - a function that adds all unique integers in a list (only once for each integer). Prototype: def uniq_add(my_list=[])

3-common_elements.py -  a function that returns a set of common elements in two sets. Prototype: def common_elements(set_1, set_2):

4-only_diff_elements.py - a function that returns a set of all elements present in only one set. Prototype: def only_diff_elements(set_1, set_2):

5-number_keys.py - a function that returns the number of keys in a dictionary. Prototype: def number_keys(a_dictionary):

6-print_sorted_dictionary.py - a function that prints a dictionary by ordered keys. Prototype: def print_sorted_dictionary(a_dictionary):

7-update_dictionary.py - a function that replaces or adds key/value in a dictionary. Prototype: def update_dictionary(a_dictionary, key, value):

8-simple_delete.py - a function that deletes a key in a dictionary. Prototype: def simple_delete(a_dictionary, key=""):

9-multiply_by_2.py -  a function that returns a new dictionary with all values multiplied by 2 Prototype: def multiply_by_2(a_dictionary):

10-best_score.py - a function that returns a key with the biggest integer value. Prototype: def best_score(a_dictionary):

11-multiply_list_map.py - a function that returns a list with all values multiplied by a number without using any loops. Prototype: def multiply_list_map(my_list=[], number=0):

12-roman_to_int.py - a function def roman_to_int(roman_string): that converts a Roman numeral to an integer. 
You can assume the number will be between 1 to 3999.
def roman_to_int(roman_string) must return an integer
If the roman_string is not a string or None, return 0
100-weight_average.py - a function that returns the weighted average of all integers tuple (<score>, <weight>) Prototype: def weight_average(my_list=[]):

101-square_matrix_map.py -  a function that computes the square value of all integers of a matrix using map
Prototype: def square_matrix_map(matrix=[]):
matrix is a 2 dimensional arra

102-complex_delete.py - a function that deletes keys with a specific value in a dictionary.
Prototype: def complex_delete(a_dictionary, value):

103-python.c - two C functions that print some basic info about Python lists and Python bytes objects. Prototype: void print_python_list(PyObject *p);

```bash
 $ cat 103-tests.py
```

```python

cat 103-tests.py 
import ctypes

lib = ctypes.CDLL('./libPython.so')
lib.print_python_list.argtypes = [ctypes.py_object]
lib.print_python_bytes.argtypes = [ctypes.py_object]
s = b"Hello"
lib.print_python_bytes(s);
b = b'\xff\xf8\x00\x00\x00\x00\x00\x00';
lib.print_python_bytes(b);
b = b'What does the \'b\' character do in front of a string literal?';
lib.print_python_bytes(b);
l = [b'Hello', b'World']
lib.print_python_list(l)
del l[1]
lib.print_python_list(l)
l = l + [4, 5, 6.0, (9, 8), [9, 8, 1024], b"Holberton", "Betty"]
lib.print_python_list(l)
l = []
lib.print_python_list(l)
l.append(0)
lib.print_python_list(l)
l.append(1)
l.append(2)
l.append(3)
l.append(4)
lib.print_python_list(l)
l.pop()
lib.print_python_list(l)
l = ["Holberton"]
lib.print_python_list(l)
lib.print_python_bytes(l);
julien@ubuntu:~/CPython$ python3 103-tests.py 
[.] bytes object info
  size: 5
  trying string: Hello
  first 6 bytes: 48 65 6c 6c 6f 00
[.] bytes object info
  size: 8
  trying string: �
  first 9 bytes: ff f8 00 00 00 00 00 00 00
[.] bytes object info
  size: 60
  trying string: What does the 'b' character do in front of a string literal?
  first 10 bytes: 57 68 61 74 20 64 6f 65 73 20
[*] Python list info
[*] Size of the Python List = 2
[*] Allocated = 2
Element 0: bytes
[.] bytes object info
  size: 5
  trying string: Hello
  first 6 bytes: 48 65 6c 6c 6f 00
Element 1: bytes
[.] bytes object info
  size: 5
  trying string: World
  first 6 bytes: 57 6f 72 6c 64 00
[*] Python list info
[*] Size of the Python List = 1
[*] Allocated = 2
Element 0: bytes
[.] bytes object info
  size: 5
  trying string: Hello
  first 6 bytes: 48 65 6c 6c 6f 00
[*] Python list info
[*] Size of the Python List = 8
[*] Allocated = 8
Element 0: bytes
[.] bytes object info
  size: 5
  trying string: Hello
  first 6 bytes: 48 65 6c 6c 6f 00
Element 1: int
Element 2: int
Element 3: float
Element 4: tuple
Element 5: list
Element 6: bytes
[.] bytes object info
  size: 9
  trying string: Holberton
  first 10 bytes: 48 6f 6c 62 65 72 74 6f 6e 00
Element 7: str
[*] Python list info
[*] Size of the Python List = 0
[*] Allocated = 0
[*] Python list info
[*] Size of the Python List = 1
[*] Allocated = 4
Element 0: int
[*] Python list info
[*] Size of the Python List = 5
[*] Allocated = 8
Element 0: int
Element 1: int
Element 2: int
Element 3: int
Element 4: int
[*] Python list info
[*] Size of the Python List = 4
[*] Allocated = 8
Element 0: int
Element 1: int
Element 2: int
Element 3: int
[*] Python list info
[*] Size of the Python List = 1
[*] Allocated = 1
Element 0: str
[.] bytes object info
  [ERROR] Invalid Bytes Object
```

