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


        add(2,3)
        add(4,5)

        items = map(lambda x: x.value, cache.lru)
        items = list(items)

        self.assertEqual(items, [5, 9])
