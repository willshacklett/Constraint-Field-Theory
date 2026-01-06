from __future__ import annotations
from dataclasses import dataclass
from typing import Dict, Callable
import math

def logistic(x: float, k: float = 3.0, x0: float = 0.0) -> float:
    """Bounded saturation in (0, 1)."""
    return 1.0 / (1.0 + math.exp(-k * (x - x0)))

@dataclass
class ConstraintField:
    """
    Minimal constraint field model.

    components: named constraint dimensions (e.g., 'load', 'stability', 'entropy')
    coupling: how strongly constraints affect each other
    """
    components: Dict[str, float]
    coupling: float = 0.15
    sat_fn: Callable[[float], float] = logistic

    def step(self, drive: Dict[str, float]) -> "ConstraintField":
        """
        Apply a drive vector and update components with mild coupling.
        This is a toy dynamical rule: not 'truth', just a minimal demonstration.
        """
        keys = list(self.components.keys())

        # Apply direct drive
        next_c = {k: self.components[k] + float(drive.get(k, 0.0)) for k in keys}

        # Apply coupling: each component nudges others (weak, averaged)
        for i in keys:
            for j in keys:
                if i == j:
                    continue
                next_c[j] += self.coupling * (next_c[i] - self.components[i])

        self.components = next_c
        return self

    def saturated(self) -> Dict[str, float]:
        """Return saturated components in (0,1)."""
        return {k: self.sat_fn(v) for k, v in self.components.items()}
