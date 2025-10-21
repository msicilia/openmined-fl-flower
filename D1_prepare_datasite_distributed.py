from pathlib import Path
import argparse
import syft_rds as sy
from syft_core import Client

parser = argparse.ArgumentParser(description="Prepare datasite with partition ID")
parser.add_argument("partition_id", type=str, help="Data partition of the node (mandatory)")
args = parser.parse_args()


do_email = Client.load().email
print(f"DO email: {do_email}")
do = sy.init_session(host=do_email, start_rds_server=True)

DATASET_PATH = Path(f"./data/node_{args.partition_id}")
try:
    dataset = do.dataset.create(
        name="synthetic-dataset",
        path=DATASET_PATH / "private",
        mock_path=DATASET_PATH / "mock",
        description_path=DATASET_PATH / "README.md",
    )
    dataset.describe()
except ValueError as e:
    print(f"Dataset already exists: {e}")
    dataset = do.dataset.get(name="synthetic-dataset")
    dataset.describe()
except Exception as e:
    print(f"An unexpected error occurred: {e}")

