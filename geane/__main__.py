from geane.p import P


def f(x):
    return x ** 2

L = [n for n in range(-10_000, 10_000)]

p = P({"f": f, "L": L})

assert not p.test("∀n ∈ L, n == 0")
assert p.test("∀n ∈ L, 0 <= f(n) <= f(10000)")
assert p.test("∀n ∈ L, n <= f(n)")

assert p.test("∃e ∈ L, f(e) == e")
assert not p.test("∃!e ∈ L, f(e) == e")
