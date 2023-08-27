from __future__ import annotations

import functools
import logging
from typing import Hashable


def ignore_unhashable(func):
    """
    Sorce: https://stackoverflow.com/a/64111268/21997874 (MIT License maybe)
    Used for caching functions.
    """
    uncached = func.__wrapped__
    attributes = functools.WRAPPER_ASSIGNMENTS + ('cache_info', 'cache_clear')

    @functools.wraps(func, assigned=attributes)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except TypeError as error:
            if 'unhashable type' in str(error):
                problematic_args = [arg for arg in args if not isinstance(arg, Hashable)]
                problematic_kwargs = {key: value for key, value in kwargs.items() if not isinstance(value, Hashable)}

                error_description = ('If one of arguments is unhashable, function cannot be cached. '
                                     'Please do not use caching.\n')
                if problematic_args:
                    error_description += (
                        'problematic argument: ' if len(problematic_args) == 1 else 'problematic arguments: '
                        + ', '.join(map(str, problematic_args))
                    )
                if problematic_args and problematic_kwargs:
                    error_description += '\n'
                if problematic_kwargs:
                    error_description += (
                        ('problematic keyword argument: ' if len(problematic_kwargs) == 1 else 'problematic keyword arguments: ')
                        + ', '.join(f'{item}: {value}' for item, value in problematic_kwargs.items())
                    )

                logging.warning(error_description)
                return uncached(*args, **kwargs)
            raise
    wrapper.__uncached__ = uncached  # type: ignore
    return wrapper
