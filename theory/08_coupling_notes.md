# Coupling in Constraint Field Theory

This note clarifies what *coupling* means in Constraint Field Theory (CFT) and how
it is detected in practice. The goal is to define coupling in the weakest
possible way that remains testable and falsifiable.

---

## Operational definition

In Constraint Field Theory, *coupling* is not assumed a priori and is not defined
by explicit interaction terms, kernels, or field equations.

Instead, coupling is defined operationally.

Two constraints are said to be **coupled** if, under joint stress, the system’s
observed saturation behavior deviates measurably from the behavior predicted by
treating the constraints as independent.

Independence is the null hypothesis. If the combined response matches the envelope
of isolated responses (for example, the maximum, union, or linear superposition
of independent saturation curves), coupling is taken to be zero.

Coupling is therefore detected only through deviation from independence, such as:
- earlier-than-expected saturation onset,
- reduced effective capacity under joint stress,
- or qualitatively steeper or cascading degradation not present in isolated runs.

If no such deviation is observed at a given scale, coupling is not supported at
that scale.

---

## Notes on scope

This note does not assume field equations, interaction kernels, conservation
laws, or specific microscopic mechanisms.

It only asserts that if constraint fields are a useful abstraction, coupling
should be detectable as a deviation from independence in systems where
saturation behavior is otherwise clear.

If saturation occurs without detectable coupling across constraints, the
field-like interpretation weakens accordingly.

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

---

## Falsification implication

If sustained joint stress across multiple constraints consistently produces
responses indistinguishable from independent saturation behavior, then coupling
—as defined here—fails to manifest, and the coupling claim of Constraint Field
Theory is falsified for that system and scale.

