import mujoco
import mujoco.viewer
from pathlib import Path

MODEL_PATH = Path(__file__).with_name("robot") / "pm01.urdf"

model = mujoco.MjModel.from_xml_path(str(MODEL_PATH))
data = mujoco.MjData(model)
mujoco.mj_forward(model, data)

mujoco.viewer.launch(model, data)