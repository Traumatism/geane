from geane.p import P


# https://en.wikipedia.org/wiki/Glossary_of_mathematical_symbols

L = [1, 1, 2, 3, 4, 5, 6]

p = P(locals())

assert p.test("∀toto ∈ L, (toto+1) <= 7")
assert not p.test("∀toto ∈ L, (toto+1) < 7")
assert p.test("∀x∈L, x>0")
assert p.test("∃x∈L, x == 5")
assert p.test("∃!x∈L, x == 5")
assert not p.test("∃!x∈L, x == 1")