import argparse
from pathlib import Path
from syft_rds.orchestra import setup_rds_server
import shutil

parser = argparse.ArgumentParser(description="Send job request to a node")
parser.add_argument("node_id", type=int, help="ID of the node (mandatory integer)")
args = parser.parse_args()


DO_EMAIL = f"{args.node_id}@openmined.org"
DS_EMAIL = "ds@openmined.org"
SYFTBOX_DATASET_NAME = "dataset"
SYFT_FLWR_PROJECT_PATH = Path("./simple-classifier")

ds_stack = setup_rds_server(email=DS_EMAIL, root_dir=Path("."), key="local_syftbox_network")
do_guest = ds_stack.init_session(host=DO_EMAIL)


shutil.rmtree(SYFT_FLWR_PROJECT_PATH / ".venv", ignore_errors=True)
shutil.rmtree(SYFT_FLWR_PROJECT_PATH / "simulation_logs", ignore_errors=True)


job = do_guest.job.submit(
    name="simple-classifier-job",
    user_code_path=SYFT_FLWR_PROJECT_PATH,
    dataset_name=SYFTBOX_DATASET_NAME,
    entrypoint="main.py",
)
print("Submitted job:")
print(job)