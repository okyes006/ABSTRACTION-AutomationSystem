# ABSTRACTION-Automation-System

## Overview
This repository is a solution to a case study activity on abstraction and
polymorphism in Object-Oriented Programming, set in the context of UMaT's
new auditorium and its automated systems.

## Task Summary
The auditorium contains several automated systems (air conditioning,
lighting, security, and a fire alarm) that each perform different tasks,
but must all support a common set of operations: `start()`, `stop()`,
and `status()`.

To model this, the solution defines:

- An **abstract base class** `BuildingSystem` with three abstract
  methods: `start()`, `stop()`, and `status()`.
- **Concrete child classes** `AirConditioningSystem`, `LightingSystem`,
  `SecuritySystem`, and `FireAlarmSystem`, each implementing all three
  abstract methods in their own way.
- A single processing function, `process_systems()`, that takes a list
  of system objects and calls `start()`, `status()`, and `stop()` on
  each — demonstrating **polymorphism**, since the same method call
  produces different behaviour depending on the actual object type.
- The script first runs `process_systems()` with only the original
  three systems (air conditioning, lighting, security). **After** that
  run, `FireAlarmSystem` is defined and appended to the list, and
  `process_systems()` is called again — with its code completely
  untouched. This proves the design is open for extension but closed
  for modification (the Open/Closed Principle): new automated systems
  can be added at any time without rewriting the existing processing
  logic.

## Files
- `building_automation.py` — full implementation and demo run.

## How to Run
```bash
python3 building_automation.py
```
