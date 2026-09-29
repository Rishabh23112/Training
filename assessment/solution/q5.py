"""Implement cache below so that repeated calls with arguments it has already seen skip recomputation.

def cache(fn):
    Decorator that avoids recomputing fn for arguments already seen.
    ...
    
"""

from functools import wraps


def cache(fn):
    """Decorator that avoids recomputing fn for arguments already seen."""
    result = {}

    @wraps(fn)
    def wrapper(*args, **kwargs):
        try:
            key = (args, tuple(sorted(kwargs.items())))
            hash(key)
        except TypeError as exc:
            raise TypeError(
                "requires all positional and keyword arguments "
            ) from exc

        if key not in result:
            result[key] = fn(*args, **kwargs)

        return result[key]

    return wrapper