from pathlib import Path
import os


SYFT_FLWR_PROJECT_PATH = Path("./simple-classifier")
assert SYFT_FLWR_PROJECT_PATH.exists()

RUN_SIMULATION = True

if RUN_SIMULATION:
    stream = os.popen(f"uv run flwr run {SYFT_FLWR_PROJECT_PATH}")
    output = stream.read()
    print(output)


# !rm -rf {SYFT_FLWR_PROJECT_PATH / "fl_diabetes_prediction" / "__pycache__"}  # clean before submitting
# !rm -rf {"../weights/"}

# if RUN_SIMULATION:
#     print(f"running syft_flwr simulation with mock paths: {mock_paths}")
#     syft_flwr.run(SYFT_FLWR_PROJECT_PATH, mock_paths)