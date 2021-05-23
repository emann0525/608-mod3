In [1]: In [1]: def maximum(value1, value2, value3):
   ...:     """Return the Maximum of three values."""
   ...:     max_value = value1
   ...:     if value2 > max_value:
   ...:         max_value = value2
   ...:         if value3 > max_value:
   ...:             max_value = value3
   ...:             return max_value
   ...: 

In [2]: maximum(12, 27, 36)
Out[2]: 36
In [1]: max(12, 27, 36)
Out[1]: 36

In [2]: min(15, 9,27, 14)
Out[2]: 9
