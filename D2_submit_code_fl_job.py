import os
import syft_rds as sy
from pathlib import Path
os.environ["SYFT_FLWR_MSG_TIMEOUT"] = "120"
import argparse

parser = argparse.ArgumentParser(description="Submit FL job to a DO (data owner)")
parser.add_argument("do", type=str, help="DO email/host (e.g. k9o3t7dyx@mozmail.com)")
args = parser.parse_args()

DO = args.do

SYFTBOX_DATASET_NAME = "synthetic-dataset"
client = sy.init_session(host=DO, start_rds_server=True)

dataset = client.dataset.get(name=SYFTBOX_DATASET_NAME)

print(
    f"Client {client.host}'s dataset name: {dataset.name}. {dataset.mock_path}"
    )
print(f"Dataset description: {dataset.summary}")


SYFT_FLWR_PROJECT_PATH = Path("./simple-classifier")
#print(f"sending job to {do1_guest.host}")

print(os.getcwd())
job = client.job.submit(
    name="simple_classifier",
    user_code_path=SYFT_FLWR_PROJECT_PATH,
    dataset_name=SYFTBOX_DATASET_NAME,
    entrypoint="main.py",
)
print(job)
