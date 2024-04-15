import logging

import numpy as np

a = np.arange(10)
logger = logging.getLogger(__name__)


def plus(a: int, b: int) -> int:
    """
    Examples
    --------
    >>> print(plus(4, 5))
    9
    """
    logger.debug(f"a: {a}, b: {b}")
    return a + b


def minus(a: int, b: int) -> int:
    """
    Examples
    --------
    >>> print(minus(4, 5))
    -1
    """
    logger.debug(f"a: {a}, b: {b}")
    return a - b
