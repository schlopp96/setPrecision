#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from math import floor, log10


def set_sigfigs(number: float | str, precision: int | str = 1) -> float | int:
    """Format value to contain given number of significant digits.

    Example:

    ```python
    >>> from SetPrecision import set_sigfigs
    >>> decimal = set_sigfigs(number=3.1459, precision=3)
    >>> print(decimal)
    '3.15'
    ```

    ---

    :param number: value to be formatted, can be entered as either a :class:`str` or :class:`float` type
    :type number: :class:`float` | :class:`str`
    :param precision: total significant figures for value :param:`number` to contain, attempts to convert :class:`str` to :class:`int`, defaults to 1
    :type precision: :class:`int` | :class:`str`, optional
    :return: value formatted to contain specified amount of significant figures
    :rtype: :class:`float` | :class:`int`
    """

    try:
        number = float(number)
        precision = int(precision)

        return round(number, precision - int(floor(log10(abs(number)))) - 1)

    except Exception as exc:
        return exc.args[0]


def set_precision(number: float | str, precision: int | str = 2) -> float:
    """Format value to contain given amount of decimal places.

    Example:

    ```python
    >>> from SetPrecision import set_precision
    >>> decimal = set_precision(number=3.1459, precision=3)
    >>> print(decimal)
    '3.146'
    ```

    ---

    :param number: value to be formatted, can be entered as either a :class:`float` or :class:`str` type
    :type number: :class:`float` | :class:`str`
    :param precision: number of decimal places for value :param:`number` to contain, attempts to convert :class:`str` to :class:`int`, defaults to 2
    :type precision: :class:`int` | :class:`str`, optional
    :return: value formatted to contain specified amount of decimal places.
    :rtype: :class:`float`
    """

    try:
        number = float(number)
        precision = int(precision)

        return float(f"{number:.{precision}f}")

    except Exception as exc:
        return exc.args[0]
