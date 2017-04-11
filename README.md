# Bad Ideas
### *It is a good idea to install bad ideas!*

Bad ideas include a collection of bad Python 3 ideas. This package is not compatible with Python 2.

Bad Ideas are prepared for PyCon 2017 talk: [Magic Method, on the wall, who, now, is the `__fairest__` one of all?](https://us.pycon.org/2017/schedule/presentation/486/). If you have any bad ideas that you want to be added here, let me know!

# Disclaimer

This code is for educational purposes ONLY. Use it at your own risk.

# Install

`pip install bad-ideas`

# Usage

## Type less by in-place editing of numbers
Avoid the carpal tunnels

```py
>>> from bad import number
>>> num = number(10)
>>> num + 3
13
>>> num
13
>>> 3 - num
-10
>>> num
-10
>>> 2 / num
-0.2
>>> num
-0.2
```

## Filter that returns list instead of generator when printed

```py
>>> from bad import filtered
>>> foo = [1, 2, 3, 5, 6, 7]
>>> filtered(lambda x: x % 3 == 0, foo)
[3, 6]
```

## Pipe and grep

```py
>>> from bad import grep
>>> LINES = """
... Whether you're new to programming or
... an experienced developer, it's easy
... to learn and use Python.
... Checkout jobs.python.org
... for Python jobs.
... """
>>> LINES | grep('Python')
['to learn and use python.', 'checkout jobs.python.org', 'for python jobs.']
>>> LINES | grep('Python') | grep('jobs')
['checkout jobs.python.org', 'for python jobs.']
```

## Undeletable
Need some memory leaking? Subclass the Undeletable to introduce "persistent" objects that won't go away!

```py
>>> from bad import Undeletable
>>> obj = Undeletable()
>>> del obj
You can't delete me!
>>> obj
<undeletable:4127530384>
```

Note that you can have many references to the same object. You can still delete all the references except the last one:

```py
>>> obj2 = obj
>>> del obj2
>>> obj2
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'obj2' is not defined
>>> obj
<undeletable:4127530384>
```

# Contribute

## Have a bad idea? Let me know!

Make a PR or open a ticket!
