# COMP10001 Python Teaching Exercises

[![Python syntax check](https://github.com/benthompsondev/comp10001-python-teaching-exercises/actions/workflows/python-check.yml/badge.svg)](https://github.com/benthompsondev/comp10001-python-teaching-exercises/actions/workflows/python-check.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

Beginner-friendly Python examples from my earlier coding and teaching support work as a PASS Leader.

This repo is an instructional archive. The programs are intentionally small and direct because they were meant to help students understand one idea at a time.

## Start Here

| If you want to... | Open this |
| --- | --- |
| See the suggested order for beginners | [Learning Path](docs/learning-path.md) |
| Run a simple first example | `grade_converter.py` |
| Check that the repo still compiles | [Python syntax check](https://github.com/benthompsondev/comp10001-python-teaching-exercises/actions/workflows/python-check.yml) |
| Understand why this is public | [Why This Is Here](#why-this-is-here) |

## Why This Is Here

This is not one of my current flagship build projects. I keep it public because it shows an earlier part of my path: learning Python seriously, explaining beginner programming concepts, writing small examples, and helping students work through logic one step at a time.

For recruiters or technical reviewers, the useful signal is communication. These examples are simpler than my current projects, but they show how I explain technical ideas and make coding less intimidating for beginners.

Some of the code is intentionally preserved as beginner/student work. I would write parts of it differently now, but that is part of the point: this shows the starting point, the teaching habit, and the path into the automation and app work I am building now.

## Teaching Focus

- Console input and output
- Conditional logic
- Functions and return values
- Lists and basic aggregation
- String checks and validation
- Simple problem decomposition

## Repository Structure

| Area | Examples |
| --- | --- |
| Basics | `input_test.py`, `grade_converter.py`, `temperature_function.py`, `miles_function.py` |
| Functions | `basic_my_sum.py`, `basic_my_min.py`, `basic_my_max.py`, `max_function.py`, `no_return_function.py` |
| Lists | `input_list.py`, `list_2.py`, `lists_3.py`, `list_4.py`, `planet_list.py` |
| Strings and validation | `phone_checker.py`, `postal_code.py`, `postal_code_edit_1.py`, `string_comparison.py`, `vowel_checker.py` |
| Exercises and assignments | `assignment_2.py`, `assignment_3.py`, `textbook_3.py`, `top_3.py`, `nested_grades.py` |
| Visual references | `logic_1.png`, `logic_2.png`, `logic_3.png`, `codingbat_lists_1.png`, `codingbat_lists_2.png` |

## How to Run an Example

Install Python 3, open a terminal in this folder, and run any script:

```powershell
python grade_converter.py
```

Many examples are interactive and will ask for input in the terminal.

To check that the examples are syntactically valid:

```powershell
python -m compileall -q .
```

## What This Shows

This project shows teaching experience, early Python practice, and the ability to explain programming concepts with small practice exercises instead of oversized examples.

For my broader GitHub, it also gives context: before the larger PowerShell systems and Ledger app work, I was already drawn to small programs, practical examples, and helping other people understand code.

## License

MIT. These examples are small teaching exercises, so feel free to reuse or adapt them for learning.
