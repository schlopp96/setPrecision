# setPrecision

## About

- `setPrecision` is a small module providing a simple way to set the precision of a floating point number or decimal to the desired amount of digits following the decimal point.

---

## Installation

### Using PIP _(Recommended)_

- To install `setPrecision` using `pip`, enter the following:

  ```python
  pip install setPrecision
  ```

### Manual Installation _(**NOT** Recommended)_

1. Download the project from [GitHub](https://github.com/schlopp96/setPrecision) and extract to location of choice.

2. Open terminal and navigate to the extracted directory `"./path/to/setPrecision"`.

3. Use `pip install -r requirements.txt` to install necessary dependencies.

- That's all!

---

## Usage

- In order to use `setPrecision`, start by importing the module to your Python environment:

```python
from setPrecision import set
```

- Now, simply call the `set` method and enter your desired number to be formatted as the `digit` parameter, and the level of precision as the `precision` parameter:

```python
>>> myNumber = 3.141592653589793 # Not necessary to set number as variable.
>>> myNumber = set(myNumber, 2)
>>> print(myNumber)
'3.15'
```

> Note that the output is automatically rounded up when `digit >= 5`, and down when `digit < 5`.

- Both params can be entered in string format, and will output successfully assuming that both paramaters can be cast to their appropriate types.
  - This is done automatically.

## Contact the Author

- If you have any questions, comments, issues, complaints, etc that cannot be resolved over GitHub, please feel free to contact me:
  - Email at: `schloppdaddy@gmail.com`.
- Otherwise:
  - Submit an issue through the project's [GitHub repository](https://github.com/schlopp96/setPrecision).
