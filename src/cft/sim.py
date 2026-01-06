from __future__ import annotations
from typing import Dict, List, Tuple
from .field import ConstraintField

def simulate(
    field: ConstraintField,
    drive: Dict[str, float],
    steps: int = 50
) -> List[Tuple[int, Dict[str, float], Dict[str, float]]]:
    """
    Returns a trajectory:
      (t, raw_components, saturated_components)
    """
    traj = []
    for t in range(steps):
        field.step(drive)
        traj.append((t, dict(field.components), field.saturated()))
    return traj
