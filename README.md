# Geane

Some dumb Python library thats uses Maths notation for writing conditions.

Notes:
- this is still in development !

- this is vulnerable to code execution through predicate field

## Examples:

```python
from geane.p import P

L = [1, 1, 2, 3, 4, 5, 6]

p = P(locals())  # or P({'L': L})

assert p.test("∀toto ∈ L, (toto+1) <= 7")
assert not p.test("∀toto ∈ L, (toto+1) < 7")

assert p.test("∀x ∈ L, x>0")
assert p.test("∃x ∈ L, x == 5")

assert p.test("∃!x ∈ L, x == 5")
assert not p.test("∃!x∈L, x == 1")
```