from __future__ import annotations
from typing import Dict, Optional
from .field import ConstraintField

def gv_projection(field: ConstraintField, weights: Optional[Dict[str, float]] = None) -> float:
    """
    A simple scalar observable projection:
    - saturate each component
    - weighted average in [0,1]
    """
    sat = field.saturated()
    if not sat:
        return 0.0

    if weights is None:
        weights = {k: 1.0 for k in sat}

    wsum = sum(weights.get(k, 0.0) for k in sat)
    if wsum <= 0:
        return 0.0

    return sum(sat[k] * (weights.get(k, 0.0) / wsum) for k in sat)
