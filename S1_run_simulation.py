from pathlib import Path
import os
import syft_flwr
import shutil
import tempfile

SYFT_FLWR_PROJECT_PATH = Path("./simple-classifier")
assert SYFT_FLWR_PROJECT_PATH.exists()

# Clean up previous cache and model files
try:
    os.remove(SYFT_FLWR_PROJECT_PATH / "simple-classifier" / "__pycache__")  
    os.remove("logreg_model.pkl")
except OSError:
    pass

# Clean up stale RPC request files from previous runs
temp_dir = Path(tempfile.gettempdir()) / "simple-classifier"
if temp_dir.exists():
    print(f"Cleaning up stale messages from {temp_dir}")
    shutil.rmtree(temp_dir, ignore_errors=True)

mock_paths = []
for client in range(1, 3):
    mock_paths.append(f"./data/node_{client}/mock")


print(f"running syft_flwr simulation with mock paths: {mock_paths}")
syft_flwr.run(SYFT_FLWR_PROJECT_PATH, mock_paths)



