import time

_cache = {}
TTL = 60 * 5  # 5 minutos

def get(key: str):
    entry = _cache.get(key)
    if entry:
        value, expires = entry
        if expires > time.time():
            return value
        else:
            del _cache[key]  # expira
    return None

def set(key: str, value):
    _cache[key] = (value, time.time() + TTL)
