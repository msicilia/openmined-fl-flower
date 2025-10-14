from pathlib import Path
import os
import syft_flwr

SYFT_FLWR_PROJECT_PATH = Path("./simple-classifier")
assert SYFT_FLWR_PROJECT_PATH.exists()

RUN_SIMULATION = True

try:
    os.remove(SYFT_FLWR_PROJECT_PATH / "simple-classifier" / "__pycache__")  # clean before submitting
except OSError:
    pass
# !rm -rf {SYFT_FLWR_PROJECT_PATH / "fl_diabetes_prediction" / "__pycache__"}  # clean before submitting
# !rm -rf {"../weights/"}

mock_paths = []
for client in range(1, 3):
    #dataset = client.dataset.get(name=SYFTBOX_DATASET_NAME)
    mock_paths.append(f"./data/node_{client}/mock")

if RUN_SIMULATION:
    print(f"running syft_flwr simulation with mock paths: {mock_paths}")
    syft_flwr.run(SYFT_FLWR_PROJECT_PATH, mock_paths)


# if RUN_SIMULATION:
#     stream = os.popen(f"uv run flwr run {SYFT_FLWR_PROJECT_PATH}")
#     output = stream.read()
#     print(output)
