# PLP Python Week 6 - Safe Functions

## Files

* `safe_tools.py` — Contains three functions that handle division errors, invalid number conversions, and missing dictionary keys.
* `README.md` — Describes the assignment files and explains why exception handling is necessary.

## Why can't an if check catch `abc` on its own?

An `if` statement can check conditions, but converting `"abc"` to an integer using `int()` raises a `ValueError` before a normal numeric check can be performed. Using `try` and `except ValueError` catches the conversion error and allows the program to return `"Not a number"` instead of crashing.
