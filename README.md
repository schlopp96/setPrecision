# setPrecision

## About

- `setPrecision` is a small module providing a simple way to set the precision of a floating point number or decimal to the desired amount of significant digits.

---

## Usage

- In order to use `setPrecision`, start by importing the `setPrecision` module to your Python environment:

```python
import setPrecision
```

- Now, simply call the `setPrecision` method and set your desired number to be formatted as the `x` parameter, and the level of precision as the `y` parameter:

```python
>>> myNumber = 3.141592653589793 # Not necessary to set number as variable.
>>> myNumber = setPrecision(myNumber, 2)
>>> print(myNumber)
'3.15'
```

> Note that the output is automatically rounded up when `digit >= 5`, and down when `digit < 5`.

## Contact

- Please do not hesitate to contact me through my email address:
  - `schloppdaddy@gmail.com`
- Send me a message/check me out at my [GitHub profile](https://github.com/schlopp96)!

---
