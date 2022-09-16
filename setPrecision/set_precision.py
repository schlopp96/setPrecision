#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from math import floor, log10


def set_sigfigs(number: float | str, precision: int | str = 1) -> float | int:
    """Set number of significant figures :param:`precision` in given value :param:`number`.

    Example:

    ```python
    >>> from SetPrecision import set_sigfigs
    >>> decimal = set_sigfigs(number=3.1459, precision=3)
    >>> print(decimal)
    '3.15'
    ```

    ---

    :param number: starting value. Can be either :class:`str` or :class:`float` type.
    :type number: :class:`float` | :class:`str`
    :param precision: total significant figures to be assigned to starting value :param:`number`. Will attempt to convert :class:`str` to :class:`int`, defaults to 1
    :type precision: :class:`int` | :class:`str`, optional
    :return: value with matching specified amount :param:`precision` of significant figures.
    :rtype: :class:`float` | :class:`int`
    """

    try:
        number = float(number)
        precision = int(precision)

        return round(number, precision - int(floor(log10(abs(number)))) - 1)

    except Exception as exc:
        return exc.args[0]


def set_precision(number: float | str, precision: int | str = 2) -> float:
    """Returns floating-point digit :param:`number` formatted with given amount :param:`precision` of decimal places.

    Example:

    ```python
    >>> from SetPrecision import set_precision
    >>> decimal = set_precision(number=3.1459, precision=3)
    >>> print(decimal)
    '3.146'
    ```

    ---

    :param number: float/decimal to be formatted, attempts to convert :class:`str` to :class:`float`
    :type number: :class:`float` | :class:`str`
    :param precision: number of decimal places to which :param:`number` is set to contain. Will attempt to convert strings to integers, defaults to 1
    :type precision: :class:`int` | :class:`str`, optional
    :return: float/decimal :param:`number` with given number of decimal places :param:`decimals`.
    :rtype: :class:`float`
    """

    try:
        number = float(number)
        precision = int(precision)

        return float(f"{number:.{precision}f}")

    except Exception as exc:
        return exc.args[0]

print(set_sigfigs(3.15625, 3))
print(set_precision(3.15625, 3))