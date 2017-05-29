#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from __future__ import absolute_import

"""
To run the test, run this in the this of repo:
    python -m unittest discover

To run a specific test, run this from the root of repo:
    python -m unittest tests.tests.Number.test1
"""
import logging
from bad import number, filtered, grep, Undeletable

logging.disable(logging.CRITICAL)


LINES = """
Whether you're new to programming or
an experienced developer, it's easy
to learn and use Python.
Checkout jobs.python.org
for Python jobs.
"""


class TestNumber:

    def test_add(self):
        num = number(10)
        num + 3
        assert num == 13

    def test_radd(self):
        num = number(10)
        3 + num
        assert num == 13

    def test_sub(self):
        num = number(10)
        num - 3
        assert num == 7

    def test_rsub(self):
        num = number(10)
        3 - num
        assert num == -7

    def test_mul(self):
        num = number(10)
        num * 3
        assert num == 30

    def test_rmul(self):
        num = number(10)
        3 * num
        assert num == 30

    def test_div(self):
        num = number(10)
        num / 2
        assert num == 5

    def test_rdiv(self):
        num = number(10)
        2 / num
        assert num == .2


class TestFiltered:

    def test_filter(self):
        foo = [1, 2, 3, 5, 6, 7]
        result = filtered(lambda x: x % 3 == 0, foo)
        assert result == [3, 6]

    def test_filter_iter_after_printing(self):
        foo = [1, 2, 3, 5, 6, 7]
        result = filtered(lambda x: x % 3 == 0, foo)
        assert result == [3, 6]
        assert [i for i in result] == [3, 6]


class TestGrep:

    def test_grep(self):
        found = LINES | grep('Python')
        assert found == ['to learn and use python.',
                         'checkout jobs.python.org', 'for python jobs.']

    def test_multi_grep(self):
        found = LINES | grep('Python') | grep('jobs')
        assert found == ['checkout jobs.python.org', 'for python jobs.']


class TestUndeletable:

    def test_delete(self):
        undeletable = Undeletable()
        del undeletable
        assert undeletable

    def test_delete_different_name(self):
        obj = Undeletable()
        del obj
        assert obj

    def test_delete_different_name_inside_another_func(self):
        def doit():
            obj = Undeletable()
            del obj
            assert obj
        doit()
