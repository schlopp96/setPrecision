#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def set(digit: float | str, precision: int | str = 1) -> str | Exception:
    """Returns a string representation of a number :float:`digit` formatted to the given precision of :int:`precision` significant digits.

    Example:

    ```python
    >>> from SetPrecision import set
    >>> x = 3.1459 # Not necessary to set number as variable.
    >>> y = set(digit=x, precision=2)
    >>> print(y)
    '3.15'
    ```

    ---

    :param digit: float/decimal to be formatted. Will attempt to convert strings to floats.
    :type digit: float | str
    :param precision: number of decimal places to which `digit` is set to contain. Will attempt to convert strings to integers, defaults to 1.
    :type precision: int | str
    :return: final string representation of formatted float/decimal `digit`.
    :rtype: str
    """
    try:
        digit = float(digit)
        precision = int(precision)
        return f"{digit:.{precision}f}"
    except Exception as exc:
        return exc