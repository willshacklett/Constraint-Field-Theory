# Coupling Notes (v0)

This note defines "coupling" in Constraint Field Theory (CFT) in the weakest
useful way: as a detectable failure of independence between constraints.

The goal is falsifiability, not completeness.

---

## What coupling means (minimal definition)

Two constraints are **coupled** if stressing one measurably alters the saturation
behavior of the other **beyond what independent behavior would predict**.

Equivalently: coupling exists when joint stress produces a response that is not
well explained by a simple combination of isolated saturation curves.

---

## What coupling is not

Coupling is **not** synonymous with "interaction."

Coupling is also **not** guaranteed by shared resources if the combined behavior
is explainable by linear superposition (e.g., predictable CPU contention).

For CFT to remain falsifiable, some constraints must saturate independently.

---

## Operational viewpoint (domain-agnostic)

Given two constraint dimensions (or components) A and B:

1. Measure A under stress in isolation → get its saturation curve and onset.
2. Measure B under stress in isolation → get its saturation curve and onset.
3. Stress A and B together → measure the combined curve.

If the combined response deviates significantly from the independent expectation,
declare coupling present.

---

## Weak coupling criteria (v0 candidates)

These are deliberately weak and should be tightened only after testing failures.

### Criterion 1 — Earlier-onset deviation
Combined saturation begins earlier than expected from isolated onsets.

### Criterion 2 — Shape deviation
Combined degradation curve is steeper or qualitatively different than expected
(e.g., sudden cliff, hysteresis, cascading failure mode).

### Criterion 3 — Lagged propagation ("constraint echoes")
Saturation (or boundary behavior) in A reliably precedes similar behavior in B
with a detectable delay.

---

## Falsification targets

Evidence against coupling (and therefore against a "field-like" framing) includes:

- A and B saturate under stress, but joint stress produces behavior well explained
  by max/union of isolated curves (coupling index ~ 0).
- Saturation events remain statistically independent across repeated experiments.
- Apparent coupling vanishes after accounting for simple linear resource contention.

---

## Notes on interpretation

This note does not assume field equations, kernels, or conservation laws.
It only asserts that coupling should be detectable as a deviation from independence
in systems where saturation is otherwise clear.
