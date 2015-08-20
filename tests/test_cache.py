__author__ = 'plasmashadow'

import unittest

from pycache import cached
from pycache import Cache


class TestCache(unittest.TestCase):

    def test_caching(self):

        cache = Cache()

        @cached(cache)
        def add(x,y):
            return x+y

        print cache
        add(2,3)
        print cache

        self.assertEqual(1,1)