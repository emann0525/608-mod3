In [1]: import random

In [2]: frequency1 = 0

In [3]: frequency2 = 0

In [4]: freqenucy3 = 0

In [5]: frequeny4 = 0

In [6]: frequency5 = 0

In [7]: frequency6 = 0

In [8]: for roll in range(6_000_000)
  File "<ipython-input-8-1011d632a4cd>", line 1
    for roll in range(6_000_000)
                                 ^
SyntaxError: invalid syntax


In [9]: for roll in range(6_000_000)
  File "<ipython-input-9-1011d632a4cd>", line 1
    for roll in range(6_000_000)
                                 ^
SyntaxError: invalid syntax


In [10]: for roll in range(6_000_000):
    ...:     face = random.randrange(1,7)
    ...: 



In [11]: 

In [11]: 

In [11]: if face == 1:
    ...:     frequency1+=1
    ...:     elif face ==2:
    ...:         frequency2 += 1
  File "<ipython-input-11-16d0ce446360>", line 3
    elif face ==2:
    ^
SyntaxError: invalid syntax


In [12]: if face == 1:
    ...:     frequency1 += 1
    ...:     elif face == 2:
    ...:         frequency2 += 1
  File "<ipython-input-12-53549a3ded5f>", line 3
    elif face == 2:
    ^
SyntaxError: invalid syntax
