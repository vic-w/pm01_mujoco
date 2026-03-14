import mujoco
import mujoco.viewer
from pathlib import Path

SCENE_PATH = Path(__file__).parent / "robot/pm01.xml"

model = mujoco.MjModel.from_xml_path(str(SCENE_PATH))
data = mujoco.MjData(model)

mujoco.viewer.launch(model, data)