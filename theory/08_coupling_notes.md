# Coupling Notes (v0)

This note defines **coupling** in Constraint Field Theory (CFT) in the weakest
useful sense: as a detectable failure of independence between constraints.

The purpose of this note is not to introduce new structure, but to specify
what *must* be observed for coupling claims to be justified, and how such
claims can fail.

---

## What coupling means (operational definition)

In Constraint Field Theory, coupling is defined operationally rather than
assumed a priori.

Two constraints are said to be **coupled** if, under joint stress, the system’s
saturation behavior deviates measurably from the behavior predicted by treating
the constraints as independent.

Independence is the null hypothesis. If the combined response is well explained
by the envelope (e.g., max, union, or linear superposition) of isolated
saturation responses, coupling is taken to be zero.

Coupling is therefore detected only through deviation from independence, such as
earlier saturation onset, reduced effective capacity, delayed propagation, or
qualitatively steeper degradation under combined stress.

If no such deviation is observed, the coupling claim fails for that system and
scale.

---

## What coupling is not

Coupling is **not** synonymous with interaction.

The mere presence of shared resources, feedback paths, or simultaneous activity
does not imply coupling if observed behavior remains explainable by independent
constraint saturation.

Coupling is also **not** guaranteed. Some constraints may saturate independently,
and CFT requires this to remain possible for the theory to be falsifiable.

---

## Measurement perspective

Coupling is assessed by comparison, not assumption.

Given two constraint dimensions (or components) A and B:

1. Measure the saturation behavior of A under increasing stress in isolation.
2. Measure the saturation behavior of B under increasing stress in isolation.
3. Apply joint stress to A and B and measure the combined response.

If the combined response deviates significantly from the independent expectation,
coupling is present at the tested scale.

---

## Weak coupling criteria (v0)

These criteria are intentionally weak and should be tightened only after
counterexamples are examined.

### Criterion 1 — Earlier-onset deviation
Combined stress produces saturation at lower load than predicted by isolated
responses.

### Criterion 2 — Shape deviation
The degradation curve under joint stress is steeper or qualitatively different
(e.g., cliffs, hysteresis, cascading failure modes).

### Criterion 3 — Propagated effects ("constraint echoes")
Saturation in one constraint reliably precedes correlated degradation in another
with a detectable delay.

---

## Falsification targets

Evidence against coupling (and therefore against a field-like framing) includes:

- Joint stress behavior fully explained by independent saturation envelopes.
- No statistically significant correlation in saturation onset or shape.
- Apparent coupling that disappears after accounting for linear resource
  contention or trivial dependencies.

If such cases dominate across domains, CFT’s coupling claims are weakened.

---

## Notes on scope

This note does not assume field equations, interaction kernels, or conservation
laws.

It only asserts that if constraint fields are a useful abstraction, coupling
should be detectable as a deviation from independence in systems where
saturation is otherwise clear.

---

## Reference implementation

A minimal, executable demonstration of the coupling criteria defined above is
provided in:

- `examples/03_coupling_demo.py`

The example constructs two saturating constraints, measures their isolated
responses, applies joint stress, and computes a simple coupling index based on
deviation from independent expectations.

This implementation is intentionally simple and exists to support falsification:
if combined behavior matches independent saturation envelopes, the coupling
index approaches zero.
