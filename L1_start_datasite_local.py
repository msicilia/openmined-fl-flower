import os
from pathlib import Path
import argparse
from syft_rds.orchestra import setup_rds_server


parser = argparse.ArgumentParser(description="Start datasite with node ID")
parser.add_argument("node_id", type=str, help="ID of the node (mandatory)")
args = parser.parse_args()


DO_EMAIL = f"{args.node_id}@openmined.org"
NODE_PATH = Path(f"./data/node_{args.node_id}")
do_stack = setup_rds_server(
    email=DO_EMAIL, root_dir=Path("."), key="local_syftbox_network"
)

os.environ["SYFTBOX_CLIENT_CONFIG_PATH"] = str(do_stack.client.config_path)

do = do_stack.init_session(host=DO_EMAIL)

dataset = do.dataset.create(
    name="dataset",
    path=NODE_PATH / "private",
    mock_path=NODE_PATH / "mock",
    description_path=NODE_PATH / "README.md",
)

