# Bad Ideas
### *It is a good idea to install bad ideas!*

Bad ideas include a collection of bad Python ideas.
This package is prepared for PyCon 2017 talk: [Magic Method, on the wall, who, now, is the `__fairest__` one of all?](https://us.pycon.org/2017/schedule/presentation/486/)

# Disclaimer

This code is for educational purposes ONLY. Use it at your own risk.

# Install

`pip install bad_ideas`

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

```py
>>> from bad import Undeletable
>>> obj = Undeletable()
>>> del obj
You can't delete me!
>>> obj
blah blah
```

# Contribute

## Have a bad idea? Let me know!

Make a PR or open a ticket!
