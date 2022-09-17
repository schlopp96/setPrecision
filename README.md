# SetPrecision

## About

- _**`SetPrecision`**_ is a small module containing two methods centered around decimal precision and significant figures:
  
  - `set_precision`: sets the precision of a floating point number or decimal to the desired amount of digits following the decimal point.
  
  - `set_sigfigs`: sets the _total_ amount of desired significant digits in a given value.

---

## Installation

### Using PIP _(Recommended)_

> _Easiest_ method. Highly recommended over manual installation.

- To install _**`SetPrecision`**_ using `pip`, enter the following:

  ```python
  python -m pip install SetPrecision
  ```

- Done!

---

### Manual Installation

> _Not_ recommended.

1. Before use, navigate to the intended installation location, and create a new directory.

2. Clone the repository with the git client of your preference using the following command:

   - ```bash
     git clone https://github.com/schlopp96/SetPrecision/releases/latest
     ```

3. Install all dependencies for this package using the following command within the directory:

   - ```bash
     pip install -r requirements.txt
     ```

- **(Optional)**: move the installation directory to `"path/to/Python/Libs/site_packages"` to be able to import this package to a Python program like any other importable package.

- Done!

---

## Usage

- Start by importing the `SetPrecision` module to your Python environment:

  - ```python
    import SetPrecision as sp
    ```

### Using `SetPrecision.set_precision`

- Call the `set_precision` method and enter your desired number to be formatted as the `number` parameter, and the level of precision as the `precision` parameter:

    - ```python

      >>> testA = 3.141592653589793 # Not necessary to set number as variable.

      >>> testA = sp.set_precision(number=testA, precision=3)

      >>> print(testA)

      3.142

      >>> testB = 3.141592653589793

      >>> testB = sp.set_precision(number=testB, precision=5)

      >>> print(testB)

      3.14159
      ```

---

### Using `SetPrecision.set_sigfigs`

- Call the `set_sigfigs` method and enter your desired number to be formatted as the `number` parameter, and the desired number of significant figures as the `precision` parameter:

  - ```python
    >>> testA = 3.141592653589793 # Not necessary to set number as variable.

    >>> testA = sp.set_sigfigs(number=testA, precision=3)

    >>> print(testA)

    3.15

    >>> testB = 3.141592653589793

    >>> testB = sp.set_sigfigs(number=testB, precision=5)

    >>> print(testB)

    3.1416
    ```

- Note that the output is automatically rounded up when `number >= 5`, and down when `number < 5` in both examples.

- Both params can be filled in with string values and will still output successfully assuming that both parameters can be cast to their appropriate types; this is done automatically.

---

## Contact the Author

- If you notice any bugs or issues that need to be addressed, please submit your findings to the [issues](https://github.com/schlopp96/SetPrecision/issues) tab.

- If you have any questions, comments, or concerns that _cannot_ be alleviated through the project's [GitHub repository](https://github.com/schlopp96/SetPrecision), please feel free to contact me through my email address:
  - `schloppdaddy@gmail.com`
