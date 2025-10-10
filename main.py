import syft_flwr
from pathlib import Path
import os

SYFT_FLWR_PROJECT_PATH = Path("./simple-classifier")
assert SYFT_FLWR_PROJECT_PATH.exists()

DS = "ds@openmined.org"
DO1 = "1@openmined.org"
DO2 = "2@openmined.org"
do_emails = [DO1, DO2]

try:
    os.remove(SYFT_FLWR_PROJECT_PATH / "main.py")  # clean before submitting
    # !rm -rf {SYFT_FLWR_PROJECT_PATH / "main.py"}
    syft_flwr.bootstrap(SYFT_FLWR_PROJECT_PATH, aggregator=DS, datasites=do_emails)
    print("Bootstrapped project successfully ✅")
except Exception as e:
    print(e)