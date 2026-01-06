from cft.field import ConstraintField
from cft.sim import simulate
from cft.gv import gv_projection

if __name__ == "__main__":
    f = ConstraintField({"load": 0.0, "stability": 0.0, "entropy": 0.0}, coupling=0.10)

    traj = simulate(f, drive={"load": 0.25}, steps=30)

    print("t  load_raw  load_sat  gv")
    for (t, raw, sat) in traj:
        g = gv_projection(f)
        print(f"{t:2d} {raw['load']:8.3f} {sat['load']:8.3f} {g:6.3f}")
