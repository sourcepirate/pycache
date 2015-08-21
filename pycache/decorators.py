
from functools import wraps


def default_decorator(func, *args, **kwargs):

    '''
      Takes in a default decorator
      function
    '''

    return repr((func, args, kwargs))


def cached(cache, kernal=default_decorator):

    '''
      Caches the result of the computation
      based on the function parameters
      available.
    '''


    def decorator(func):


        def inner(*args, **kwargs):

            key = kernal(func, *args, **kwargs)
            return cache.fetch_with_generator(key, func, *args, **kwargs)

        return inner

    return decorator


#
# def verbose(func):
#     '''
#     Decorator to print debug stuff - use it only on python >= 2.5
#     '''
#     def verbose_func(self, *args, **kwargs):
#         print "  " * self.level, "==> Entering: %s(*%r, **%r)" % (func.__name__, args, kwargs)
#         self.level += 1
#         print "  " * self.level, self.lru
#         res = func(self, *args, **kwargs)
#         print "  " * self.level, self.lru
#         self.level -= 1
#         print "  " * self.level, "==> Leaving %s: %r" % (func.__name__, res)
#         return res
#
#     return verbose_func


def synchronized(func):

    '''

      This method is used for locking the current critical section
      method to a  particular shared point.

    '''

    def inner(self, *args, **kwargs):

        self.lock.acquire()
        try:
            return func(self, *args, **kwargs)
        finally:
            self.lock.release()

    return inner
