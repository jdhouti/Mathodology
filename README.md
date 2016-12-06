# Library Description
A library of math modules that perform mathematical computations on lists and numbers using self developed algorithms.

# Old Algorithms
### list_eq(l1, l2) --version 1.0
```python
k = 0

while k < len(l1):
    if l1[k] == l2[k]:
        k += 1

    else:
        return False
return True
```
### list_reverse(l) --version 1.0
```python
i, tlist = -1, []

try:
    while i >= -1 * len(l):
        tlist.append(l[i])
        i -= 1

    return tlist

except IndexError:
    return "Index Error!"
```
### some_even(l) --version 1.0
```python
c = 0

while c < len(l):
    if l[c] % 2 == 0:
        return True

    else:
        c += 1
return False
```
### all_even(l) --version 1.0
```python
c = 0

while c < len(l):
    if l[c] % 2 == 0:
        c += 1

    else:
        return False
return True
```
### list_convert(l, func) --version 1.0
```python
i, newList = 0, []

try:
    while i < len(l1):
        newList.append(func(l1[i]))
        i += 1
    return newList

except:
    return "Given function cannot be applied to an integer!"
```        
### append_lists(l1, l2) --version 1.0
```python
i = 0

while i != len(l2):
    l1.append(l2[i])
    i += 1
```
