# 42 Python Module 00 - Growing Code

Dieses Repository enthält meine Umsetzung des Subjects **"Growing Code - Python Fundamentals Through Garden Data"** (Version 2.1).

## Subject-Basis

- Datei: `_docs/en.subject.pdf`
- Fokus: Python-Grundlagen über 8 Übungen (`ex0` bis `ex7`)
- Abgabeprinzip: pro Exercise nur die geforderte Funktion, kein eigenes `main` in den Abgabedateien

## Lernziele aus dem Subject

- Funktionen definieren und aufrufen
- Ein-/Ausgabe mit `input()` und `print()`
- Typumwandlung mit `int()`
- Bedingungen mit `if` / `elif` / `else`
- Wiederholung mit Iteration (`range`) und Rekursion
- Type Hints in Funktionssignaturen

## Projektstruktur

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

## Umsetzungsstand

| Exercise | Datei(en) | Thema | Authorized (laut Subject) | Status |
|---|---|---|---|---|
| `ex0` | `ex0/ft_hello_garden.py` | Erste Funktion / Ausgabe | `print()` | umgesetzt |
| `ex1` | `ex1/ft_plot_area.py` | Rechteckfläche berechnen | `input(), int(), print()` | umgesetzt |
| `ex2` | `ex2/ft_harvest_total.py` | Summenbildung über 3 Eingaben | `input(), int(), print()` | umgesetzt |
| `ex3` | `ex3/ft_plant_age.py` | Bedingte Ausgabe nach Alter | `input(), int(), print()` | umgesetzt |
| `ex4` | `ex4/ft_water_reminder.py` | Bedingte Erinnerung | `input(), int(), print()` | umgesetzt |
| `ex5` | `ex5/ft_count_harvest_iterative.py` + `ex5/ft_count_harvest_recursive.py` | Iteration vs. Rekursion | `input(), int(), print(), range()` + Helper-Funktion | umgesetzt |
| `ex6` | `ex6/ft_garden_summary.py` | Zusammenfassung aus Eingaben | `input(), print()` | umgesetzt |
| `ex7` | `ex7/ft_seed_inventory.py` | Type Hints + Unit-Handling | `print()` | umgesetzt |

## Lokales Testen

Syntax-Check aller Übungsdateien:

```bash
python3 -m py_compile ex0/ft_hello_garden.py ex1/ft_plot_area.py ex2/ft_harvest_total.py ex3/ft_plant_age.py ex4/ft_water_reminder.py ex5/ft_count_harvest_iterative.py ex5/ft_count_harvest_recursive.py ex6/ft_garden_summary.py ex7/ft_seed_inventory.py
```

Falls `flake8` vorhanden ist:

```bash
python3 -m flake8 ex0 ex1 ex2 ex3 ex4 ex5 ex6 ex7
```

## Hinweise

- Die `>>> ft_function()`-Zeilen im Subject sind Aufrufbeispiele (Interpreter-Prompt), nicht Teil der Funktionsausgabe.
- Für `ex6` wird die Pflanzenanzahl als Eingabe-String weiterverwendet, da laut Subject nur `input()` und `print()` autorisiert sind.
