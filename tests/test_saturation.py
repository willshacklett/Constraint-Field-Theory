from cft.field import ConstraintField
from cft.gv import gv_projection

def test_saturation_is_bounded():
    f = ConstraintField({"load": 0.0})
    for _ in range(100):
        f.step({"load": 1.0})
        g = gv_projection(f)
        assert 0.0 <= g <= 1.0
