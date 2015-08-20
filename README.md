##PyCache


Pycache is a LRU Implemented with Linked Stack.
https://en.wikipedia.org/wiki/Cache_algorithms#LRU


###Installation:

```
git clone https://github.com/plasmashadow/pycache

cd pycache

python setup.py install

```

###Usage:

You can use pycache as both object as well as a decorator


```
from pycache import cached
from pycache import Cache

cache = Cache()

@cached(cache)
def add(x,y):
    return x+y

#operation will be computed and stored on cache
print add(2,3)

#will be retrived from cache
add(2,3)


# As a cache object
c = Cache()

c.insert(key, value)
c.update(key, value)
c.fetch(key)

```

###License

MIT
