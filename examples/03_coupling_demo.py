import numpy as np
import matplotlib.pyplot as plt

# -----------------------------
# Toy saturation model
# -----------------------------

def saturating_response(load, capacity, sharpness=10):
    """
    Simple bounded response:
    approaches capacity as load increases.
    """
    return capacity * (1 - np.exp(-load / sharpness))


# -----------------------------
# Independent components
# -----------------------------

loads = np.linspace(0, 100, 200)

# Component A and B capacities
cap_A = 50
cap_B = 40

resp_A = saturating_response(loads, cap_A)
resp_B = saturating_response(loads, cap_B)

# Independent expectation (max envelope)
independent_expectation = np.maximum(resp_A, resp_B)

# -----------------------------
# Coupled system (intentionally weak)
# -----------------------------

def coupled_response(load):
    """
    Weak coupling:
    effective capacity shrinks once both loads are high.
    """
    coupling_penalty = 0.15 * load
    effective_cap = max(cap_A - coupling_penalty, 10)
    return saturating_response(load, effective_cap)

resp_coupled = np.array([coupled_response(l) for l in loads])

# -----------------------------
# Coupling index (v0)
# -----------------------------

coupling_index = np.mean(independent_expectation - resp_coupled)

print(f"Coupling index (v0): {coupling_index:.3f}")

# -----------------------------
# Plot
# -----------------------------

plt.figure(figsize=(8, 5))
plt.plot(loads, resp_A, label="Component A (isolated)")
plt.plot(loads, resp_B, label="Component B (isolated)")
plt.plot(loads, independent_expectation, "--", label="Independent expectation")
plt.plot(loads, resp_coupled, linewidth=2, label="Coupled system")

plt.xlabel("Load")
plt.ylabel("Response")
plt.title("Minimal Coupling Demonstration")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
