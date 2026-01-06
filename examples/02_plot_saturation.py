import matplotlib.pyplot as plt
from cft.field import ConstraintField
from cft.sim import simulate

f = ConstraintField({"load": 0.0})
traj = simulate(f, drive={"load": 0.3}, steps=50)

t = [x[0] for x in traj]
raw = [x[1]["load"] for x in traj]
sat = [x[2]["load"] for x in traj]

plt.plot(t, raw, label="raw load")
plt.plot(t, sat, label="saturated load")
plt.xlabel("time step")
plt.ylabel("value")
plt.legend()
plt.title("Constraint saturation under constant drive")
plt.tight_layout()
plt.savefig("paper/figures/saturation_demo.png", dpi=200)
plt.close()

