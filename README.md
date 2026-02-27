*This project has been created as part of the 42 curriculum by fschnorr.*

# 42 Python Module 00 - Growing Code

## Description
This repository contains my implementation of **Python Module 00** based on the subject
**"Growing Code - Python Fundamentals Through Garden Data"** (version 2.1).

The goal of this project is to practice core Python syntax and control flow through
small, focused exercises. The module covers:
- standard output with `print()`
- user input with `input()`
- integer conversion with `int()`
- arithmetic and conditional logic
- iteration and recursion
- simple type-annotated function signatures

Project reference:
- Subject file: `_docs/en.subject.pdf`

## Instructions
### Requirements
- Python 3.10+
- flake8-compliant style

### Repository Structure
```text
ex0/ft_hello_garden.py
ex1/ft_plot_area.py
ex2/ft_harvest_total.py
ex3/ft_plant_age.py
ex4/ft_water_reminder.py
ex5/ft_count_harvest_iterative.py
ex5/ft_count_harvest_recursive.py
ex6/ft_garden_summary.py
ex7/ft_seed_inventory.py
_docs/en.subject.pdf
```

### Run Exercises
Run each exercise file directly:
```bash
cp _docs/main.py ex0 && python3 ex0/main.py
cp _docs/main.py ex1 && python3 ex1/main.py
cp _docs/main.py ex2 && python3 ex2/main.py
cp _docs/main.py ex3 && python3 ex3/main.py
cp _docs/main.py ex4 && python3 ex4/main.py
cp _docs/main.py ex5 && python3 ex5/main.py
cp _docs/main.py ex6 && python3 ex6/main.py
cp _docs/main.py ex7 && python3 ex7/main.py
```

Use the helper runner if needed:
```bash
python3 _docs/main.py
```

### Optional Checks
Syntax check:
```bash
python3 -m py_compile ex0/ft_hello_garden.py ex1/ft_plot_area.py ex2/ft_harvest_total.py ex3/ft_plant_age.py ex4/ft_water_reminder.py ex5/ft_count_harvest_iterative.py ex5/ft_count_harvest_recursive.py ex6/ft_garden_summary.py ex7/ft_seed_inventory.py
```

Style check:
```bash
python3 -m flake8 ex0 ex1 ex2 ex3 ex4 ex5 ex6 ex7
```

## Resources
### Classic References
- Python Tutorial: https://docs.python.org/3/tutorial/
- Python Functions (built-ins): https://docs.python.org/3/library/functions.html
- Python Control Flow: https://docs.python.org/3/tutorial/controlflow.html
- PEP 8 Style Guide: https://peps.python.org/pep-0008/
- Real Python (beginner-friendly tutorials): https://realpython.com/

### AI Usage in This Project
AI assistance was used for:
- clarifying Python fundamentals (e.g. `f`-strings, `range()`, method scope, class basics)
- debugging specific mistakes (syntax issues, method calls, formatting, function signatures)
- reviewing exercise compliance against the subject (expected outputs and authorized usage)
- improving tooling/workflow (flake8 checks, editor indentation setup, README drafting)

All final code decisions and submitted implementations were manually reviewed and
validated.
